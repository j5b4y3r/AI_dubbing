# Main file for dubbing
from moviepy.editor import AudioFileClip, VideoFileClip
from pydub import AudioSegment
import numpy as np
import os, string, random

from extentions.downloader import download_video
from extentions.vocalSeparator import separator
from extentions.audioSeparator import separate_audio
from extentions.translator import translate_text
from extentions.stt import get_transcribed, get_text
from extentions.tts import get_speech_google
from extentions.audioCombiner import combine
from extentions.asignSpeakers import assign_speakers_to_transcript
from extentions.saveSpeakersVoice import save_speaker_sample
from extentions.speakerDiarization import detect_speekers

def download(url, path):
    try:
        return download_video(url, path)
    except Exception as e:
        print(e)
        return False

def separate_video_and_audio(video_file_path, a, v):
    file = separate_audio(video_file_path, a, v)
    if not file == False:
        return file
    else:
        return False

def separate_vocals_and_music(a, out):
    return separator(a, out)

def transcribe(a):
    result = get_transcribed(a)
    try:
        with open("temp/stt/transcribe.txt", "w+") as f:
            f.write(result)
    except:
        pass        
    return result

def translate(segments, from_lang, to_lang):
# Translate each segment and maintain the timestamps
    translated_segments = []
    for segment in segments:
        translated_segment = translate_text(segment['text'], from_language=from_lang,target_language=to_lang)
        translated_segments.append({
            'id': segment['id'],
            'start': segment['start'],
            'end': segment['end'],
            'text': translated_segment
        })
    
    return translated_segments

def text_to_speech(text, lang, pth):
    return get_speech_google(text, lang, pth)

def dub_audio(transcribed, original_audio, output_path, voice_over=False, voice_sample='', multi_speaker_sample=[]):   
    return combine(transcribed, original_audio, output_path, voice_over, voice_sample=voice_sample, multi_speaker_sample=multi_speaker_sample)

def add_music_to_vocal(music_path, vocal_path):
    output_path = "temp/output.mp3"
    music_file = AudioSegment.from_wav(music_path)
    vocal_audio = AudioSegment.from_mp3(vocal_path)
    audio = vocal_audio.overlay(music_file)
    audio.export(output_path, format="mp3")
    return output_path

def export_video(video_path, audio_path):
    video_clip = VideoFileClip(video_path)
    adjusted_audio = AudioFileClip(audio_path)
    video_with_adjusted_audio = video_clip.set_audio(adjusted_audio)

    file_name = "dubbed/output_video_with_synced_audio.mp4"

    if os.path.exists(file_name):
        file_name = f'dubbed/output_video_with_synced_audio_{str("".join(random.choices(string.ascii_letters, k=5)))}.mp4'

    # Export the final video
    video_with_adjusted_audio.write_videofile(file_name, codec="libx264", audio_codec="aac")
    return file_name

def multispeaker_control(audio_file_path, transcribed_segments, output_path):
    labels, times = detect_speekers(audio_file_path)
    segments = assign_speakers_to_transcript(transcribed_segments, labels, times)
    files = save_speaker_sample(audio_file_path, segments, output_path)
    return files
