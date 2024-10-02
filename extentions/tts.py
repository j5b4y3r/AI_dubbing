from gtts import gTTS
import os
from TTS.api import TTS
from pydub import AudioSegment
from pydub.silence import split_on_silence
import subprocess


def get_speech_google(text="", lang="en", path="", id=""):
    if not os.path.exists(path+"/tts/"):
        os.mkdir(path+"/tts/") 
    tts = gTTS(text=text, lang=lang)
    tts.save(path+"/tts/temp_segment"+str(id)+".mp3")
    
    convert_mp3_to_wav(path+"/tts/temp_segment"+str(id)+".mp3", path+"/tts/temp_segment"+str(id)+".wav")

    os.remove(path+"/tts/temp_segment"+str(id)+".mp3")
    return AudioSegment.from_wav(path+"/tts/temp_segment"+str(id)+".wav"), path+"/tts/temp_segment"+str(id)+".wav"

def load_tts_model():
# load the tts model
    tts = TTS("tts_models/multilingual/multi-dataset/your_tts", gpu=False)
    return tts

def get_voice_over_speech(model, text="", lang="en", sample_wav="", path="", id=""):

    langlist = ['en', 'fr-fr', 'pt-br']
    if lang not in langlist:
        lang = "en"

    if not os.path.exists(path+"/tts/"):
        os.mkdir(path+"/tts/")    
    
    # generate speech by cloning a voice using default settings
    model.tts_to_file(text=text,
                file_path=path+"/tts/temp_segment"+str(id)+".mp3",
                speaker_wav=sample_wav,
                language=lang
                )

    
    convert_mp3_to_wav(path+"/tts/temp_segment"+str(id)+".mp3", path+"/tts/temp_segment"+str(id)+".wav")

    os.remove(path+"/tts/temp_segment"+str(id)+".mp3")
    return AudioSegment.from_wav(path+"/tts/temp_segment"+str(id)+".wav"), path+"/tts/temp_segment"+str(id)+".wav"

    

def verify_mp3_file(file_path):
    command = ['ffmpeg', '-v', 'error', '-i', file_path, '-f', 'null', '-']
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode != 0:
        print(f"Error in MP3 file: {result.stderr.decode('utf-8')}")
        return False
    else:
        return True


def convert_mp3_to_wav(input_file, output_file):
    if os.path.exists(output_file):
        os.remove(output_file)

    command = ['ffmpeg', '-i', input_file, output_file]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode == 0:
        print(f"Successfully converted {input_file} to WAV format.")
    else:
        print(f"Failed to convert: {result.stderr.decode('utf-8')}")


  
