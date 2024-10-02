# This is last step. Combine the TTS Audio with Timestamps
import os
from pydub import AudioSegment
import librosa, soundfile as sf
from .stt import get_transcribed
from .tts import get_speech_google, get_voice_over_speech, load_tts_model
from .translator import translate_text

def combine(trnascrided_result, original_audio_path, output_audio_path, voice_over=False, voice_sample="", multi_speaker_sample=[]):
    # Load the original audio to get duration and match timing
    original_audio = AudioSegment.from_mp3(original_audio_path)

    # Create an empty audio file to merge everything
    output_audio = AudioSegment.silent(duration=len(original_audio))

    segments = trnascrided_result['segments']
    language = trnascrided_result['language']
    text = trnascrided_result['text']

    if voice_over and language in ['en', 'hi', 'fr', 'es', 'it', 'run', 'ko', 'tr', 'ar', 'zh-cn', 'ja', 'de']:
        model = load_tts_model()

    print("Segment lenth: "+str(len(segments)))
    
    full_sentence = ""
    full_sentence_start_time = 0
    time_set = True 
    duration = 0

    for segment in segments:
        start_time = segment['start'] * 1000  # Convert seconds to milliseconds
        end_time = segment['end'] * 1000
        segment_text = segment['text']

        # skip if not text
        if segment_text == "":
            continue
        if not "." in segment_text:
            full_sentence += segment_text
            if time_set:
                full_sentence_start_time = start_time
                time_set = False
            continue
        else:
            full_sentence += segment_text
            duration = end_time - full_sentence_start_time
            if time_set:
                full_sentence_start_time = start_time
                
        print(f"{segment['id']} {full_sentence_start_time} | {end_time} --> {duration} : {full_sentence}")     
        
        # Generate TTS for the segment
        if voice_over and language in ['en', 'hi', 'fr', 'es', 'it', 'run', 'ko', 'tr', 'ar', 'zh-cn', 'ja', 'de']:

            if len(multi_speaker_sample) > 0:      # finding correct voice for cloning
                for file in multi_speaker_sample:
                    try:
                        if segment['speaker'] in file:
                            voice_sample = file
                        else:
                            voice_sample = multi_speaker_sample[0]        
                    except Exception as e:
                        print(e)       

            tts_audio, pth = get_voice_over_speech(model=model, text=full_sentence, lang=language, sample_wav=voice_sample, path=output_audio_path, id=segment['id'])
        else:    
            tts_audio, pth = get_speech_google(full_sentence, lang=language, path=output_audio_path, id=segment['id'])

        # Insert the TTS audio at the correct timestamp position
        original_duration = len(tts_audio)
        print("Audio duration: ", original_duration, " Desire: ", duration)
        if original_duration == 0:
            print("Original audio duration is Zero (0)")
            continue
        speed_factor = original_duration / duration
        print(speed_factor)
        
        # Adjust the speed of the audio 
        if speed_factor > 1:
            tts_audio.export(output_audio_path+"/audioCombiner/temp_speed_output.mp3", format="mp3", parameters=["-filter:a", f"atempo={speed_factor}"])
            adjusted_audio = AudioSegment.from_mp3(output_audio_path+"/audioCombiner/temp_speed_output.mp3")  
        else:
            adjusted_audio = tts_audio    
        output_audio = output_audio.overlay(adjusted_audio, position=full_sentence_start_time)
        full_sentence = ""
        time_set = True

    # Save the final result
    output_audio.export(output_audio_path+"/audioCombiner/output_with_speech.mp3", format="mp3")
    return output_audio_path+"/audioCombiner/output_with_speech.mp3"
