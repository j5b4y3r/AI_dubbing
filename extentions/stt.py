import speech_recognition as sr
from pydub import AudioSegment
import os
import whisper

# Initialize the recognizer
recognizer = sr.Recognizer()

def get_text(audio_file_path):
    if audio_file_path.endswith(".mp3"):
        audio_file_path = to_wav(audio_file_path)

    # Load the audio file
    with sr.AudioFile(audio_file_path) as source:
        audio = recognizer.record(source)  # Read the entire audio file

    try:
        # Using Google Web Speech API for recognition
        text = recognizer.recognize_google(audio)
        print("Transcription: " + text)
        return text
    
    except ValueError:
        audio_file_path = to_wav(audio_file_path)
        # Load the audio file
        with sr.AudioFile(audio_file_path) as source:
            audio = recognizer.record(source)  # Read the entire audio file

        try:
            # Using Google Web Speech API for recognition
            text = recognizer.recognize_google(audio)
            print("Transcription: " + text)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        finally:
            # Delete the temporary audio file if it was converted
            if os.path.exists(audio_file_path):
                os.remove(audio_file_path) 

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    finally:
        # Delete the temporary audio file if it was converted
        if os.path.exists(audio_file_path):
            os.remove(audio_file_path)


# Using wishper, advanced, use for dubbing video.
def get_transcribed(audio_path):

    # Load Whisper model
    model = whisper.load_model("base")

    # Transcribe the audio file
    result = model.transcribe(audio_path, word_timestamps=True)

    return result


def to_wav(audio_file_path):
    # Convert MP3 to WAV
    audio = AudioSegment.from_mp3(audio_file_path)

    # Define the output path
    wav_file_path = "output_audio.wav"

    # Export the audio as a WAV file
    audio.export(wav_file_path, format="wav")

    return wav_file_path

