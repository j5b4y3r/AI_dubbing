# Separate Audio and Video from a Video.

from moviepy.editor import VideoFileClip
import threading

# Function to extract audio
def extract_audio(video_clip, audio_output):
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_output+"/audioSeparator/audio.mp3")
    audio_clip.close()

# Function to mute audio and save video
def save_video_without_audio(video_clip, video_output):
    video_clip = video_clip.volumex(0)  # Mute the audio
    video_clip.write_videofile(video_output+"/audioSeparator/video.mp4", codec='libx264')
    video_clip.close()

def separate_audio(input_video_path, audio_output_path, video_output_path):
    # Load the video
    video_clip = VideoFileClip(input_video_path)
    audio_clip = VideoFileClip(input_video_path)

    # Create threads for audio extraction and video saving
    audio_thread = threading.Thread(target=extract_audio, args=(audio_clip, audio_output_path))
    video_thread = threading.Thread(target=save_video_without_audio, args=(video_clip, video_output_path))

    # Start both threads
    audio_thread.start()
    video_thread.start()

    # Wait for both threads to finish
    audio_thread.join()
    video_thread.join()

    print("Audio and video have been separated successfully!")
    return video_output_path+"/audioSeparator/video.mp4", audio_output_path+"/audioSeparator/audio.mp3"
