'''print("Initializing...")
from dubbing import *
print("Loading...")

#video_file = "C:/Users/user/Downloads/Video/A HERO FOR FUN 🗿- SAITAMA EDIT #onepunchman_2.mp4"
output_path = "C:\\Users\\user\\Desktop\\Project\\Ai_dubbing\\temp"
print("working...")
url = "https://www.youtube.com/shorts/eL_vhPmSZfM"
video_file = download(url, "temp/downloads")

#video_file_path, audio_file_path = separate_video_and_audio(video_file, output_path, output_path)
print("Video and Audio is separated")
#path = separate_vocals_and_music(audio_file_path, "C:/Users/user/Desktop/Project/Ai_dubbing/temp/vocalSeparator/outputs")
print("Vocal and Music is separated")
vocal_file = "C:/Users/user/Desktop/Project/Ai_dubbing/temp/vocalSeparator/outputs/htdemucs/audio/vocals.wav" # path['vocals']
music_file = "C:/Users/user/Desktop/Project/Ai_dubbing/temp/vocalSeparator/outputs/htdemucs/audio/no_vocals.wav" # path['no_vocals']
#print(path)

print("Transcribing...")
result = trancribe(vocal_file)
print("Trancrided language: ", result['language'])

do_translate = True
lang = "fr"

if do_translate:
    translate_segments = translate(result['segments'], from_lang=result['language'], to_lang=lang)

    transcribed = {
        'segments': translate_segments,
        'language': lang,
        'text': result['text'],
    }
    print(transcribed)
else:
    transcribed = result

output = dub_audio(transcribed, vocal_file, output_path, voice_sample=vocal_file)
print(output)
output_path_dubb = add_music_to_vocal(music_file, output)
#print(output_path_dubb)
export_video(video_file, output_path_dubb)
#text_to_speech()

'''
from flask import Flask, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename
import os

from dubbing import *

from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Set upload folder
UPLOAD_FOLDER = 'temp/downloads'
OUTPUT_FOLDER = 'temp'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Route for rendering the HTML UI
@app.route('/')
def index():
    return render_template('test.html')  # Render the HTML file

# Route for processing dubbing requests
@app.route('/dubbing', methods=['POST'])
def dubbing():
    # Retrieve form data
    contains_music = request.form.get('contains_music') == 'true'
    language = request.form.get('language')
    translate_text = request.form.get('translate') == 'true'
    speaker = request.form.get('speaker')

    # Process either a file or a URL
    file = request.files.get('file')
    url = request.form.get('url')

    video_file_path = None

    # Handle file upload
    if file:
        filename = secure_filename(file.filename)
        video_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(video_file_path)

    # Handle URL input (download the video)
    if url:
        # Replace this function with your video downloading logic
        video_file_path = download_video(url, app.config['UPLOAD_FOLDER'])

    if not video_file_path:
        return jsonify({'error': 'No valid video file or URL provided.'}), 400

    print(video_file_path)
    video_file_path, audio_file_path = separate_video_and_audio(video_file_path, OUTPUT_FOLDER, OUTPUT_FOLDER)

    # Example: Separate vocal/music if required
    if contains_music:
        # Call function to separate vocals and music
        path = separate_vocals_and_music(audio_file_path, OUTPUT_FOLDER)
        vocal_file = path['vocals']
        music_file = path['no_vocals']
    else:
        vocal_file = audio_file_path

    print("Transcribing...")
    result = transcribe(vocal_file)
    print("Translating text...")
    if translate_text and language != result['language']:
        # Example translation logic
        translated_segments = translate(result['segments'], from_lang=result['language'], to_lang=language)
        transcribed = {
            'segments': translated_segments,
            'language': language,
            'text': result['text'],
        }
    else:
        transcribed = result 

    if int(speaker) > 1:
        speaker_sample_path_list = multispeaker_control(vocal_file, transcribed['segments'], OUTPUT_FOLDER)
    else:
        speaker_sample_path_list = []
    print("Dubbing audio...")
    # Example: Dubbing logic (using translated or transcribed audio)
    dubbed_audio_path = dub_audio(transcribed, vocal_file, app.config['OUTPUT_FOLDER'], voice_over=True, voice_sample=vocal_file, multi_speaker_sample=speaker_sample_path_list)

    # Example: Combine music and dubbed audio if music is separated
    if contains_music:
        output_video_path = add_music_to_vocal(music_file, dubbed_audio_path)
    else:
        output_video_path = dubbed_audio_path

    # Example: Export the final dubbed video
    final_video_path = export_video(video_file_path, output_video_path)

    return jsonify({'output_video': final_video_path})

# Route to download the dubbed video
@app.route('/download')
def download():
    file_path = request.args.get('file')
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
