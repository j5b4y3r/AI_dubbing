import os
import requests
import re
import yt_dlp
from moviepy.editor import VideoFileClip

# Define the characters not allowed in Windows filenames
INVALID_CHARACTERS = r'[<>:"/\\|?#*]'

# Limits
MAX_FILESIZE_MB = 10  # 10 MB limit
MAX_DURATION_SECONDS = 60  # 1 minutes (60 seconds)

def sanitize_filename(filename):
    """
    Removes or replaces invalid characters from the filename.
    """
    return re.sub(INVALID_CHARACTERS, '', filename)

def ensure_directory_exists(path):
    """Ensure the directory exists, if not, create it."""
    if not os.path.exists(path):
        os.makedirs(path)

def download_from_direct_url(url, path):
    ensure_directory_exists(path)  # Ensure path exists
    file_name = url.split("/")[-1]

    # Sanitize the filename to remove forbidden characters
    sanitized_file = sanitize_filename(file_name)
    sanitized_path = f"{path}/{sanitized_file}".replace("\\", "/")

    # Download the file
    response = requests.get(url, stream=True)
    with open(sanitized_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
    
    print(f"Direct URL File downloaded to {sanitized_path}")
    return sanitized_path        

def download_from_social_platform(url, path, download_audio=False):
    ensure_directory_exists(path)  # Ensure the directory exists

    # Use yt-dlp to get video metadata without downloading
    ydl_opts_info = {
        'quiet': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'format': 'bestvideo+bestaudio/best',  # Fetch the best video + audio formats
    }
    
    with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
        info_dict = ydl.extract_info(url, download=False)  # Extract info without downloading
    
    # Extract available formats
    available_formats = info_dict.get('formats', [])
    
    # Filter out formats based on file size, duration constraints, and ensure audio is present
    filtered_formats = []
    for format_info in available_formats:
        format_filesize = format_info.get('filesize', None)  # In bytes, could be None
        format_duration = info_dict.get('duration', None)  # In seconds, could be None

        # Ensure the format contains both video and audio (acodec must not be 'none')
        has_audio = format_info.get('acodec', 'none') != 'none'
        has_video = format_info.get('vcodec', 'none') != 'none'
        
        # Convert filesize to MB, ensure we handle None
        filesize_mb = (format_filesize / (1024 * 1024)) if format_filesize else 0
        
        # Ensure both filesize, duration are valid, and format contains audio before adding
        if (format_filesize is not None and filesize_mb <= MAX_FILESIZE_MB) and \
           (format_duration is not None and format_duration <= MAX_DURATION_SECONDS) and \
           has_audio and has_video:
            filtered_formats.append(format_info)
            
    # If no formats match the constraints, exit
    if not filtered_formats:
        print(f"No available formats with audio under {MAX_FILESIZE_MB} MB and {MAX_DURATION_SECONDS / 60} minutes.")
        return None
    
    # Sort the filtered formats by quality (bitrate or resolution)
    best_format = sorted(filtered_formats, key=lambda f: f.get('tbr', 0), reverse=True)[0]

    # Create custom filename: sanitize and force lowercase
    original_title = info_dict['title']
    sanitized_title = sanitize_filename(original_title).lower()
    ext = best_format['ext']
    custom_filename = f"{sanitized_title}.{ext}"

    # Define yt-dlp options with controlled filename and specific format
    ydl_opts = {
        'outtmpl': os.path.join(path, custom_filename),
        'format': best_format['format_id'],  # Specify the best format by ID
        'noplaylist': True,
        'quiet': True,  # Suppress output
        'nocheckcertificate': True,  # Skip SSL certificate verification
    }

    # Download the video using the selected format
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])  # Download the file

    full_path = os.path.join(path, custom_filename)

    # Convert WebM to MP4 if needed
    if ext == 'webm':
        mp4_file = os.path.splitext(full_path)[0] + '.mp4'
        convert_webm_to_mp4(full_path, mp4_file)
        os.remove(full_path)  # Optionally remove original WebM
        return mp4_file
    else:
        print(f"Downloaded: {full_path}")
        return full_path

def convert_webm_to_mp4(webm_path, mp4_path):
    video = VideoFileClip(webm_path)
    video.write_videofile(mp4_path, codec='libx264')

def download_video(url, path, download_audio=False):
    ensure_directory_exists(path)  # Ensure the directory exists
    
    if url.endswith(('.mp4', '.mkv', '.avi', '.mov', '.mp3', '.wav')):
        # Direct URL Download
        file_path = download_from_direct_url(url, path)
    else:
        # Social Media Download (e.g., YouTube)
        file_path = download_from_social_platform(url, path, download_audio)
        
    return file_path
