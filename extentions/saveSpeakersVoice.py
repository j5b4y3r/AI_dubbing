import librosa
import soundfile as sf

def save_speaker_sample(audio_file_path, transcript_segments, output_path):
    audio, sr = librosa.load(audio_file_path, sr=None)
    
    # Dictionary to track the longest segment for each speaker
    longest_segments = {}

    # Iterate through each segment in the transcript
    for segment in transcript_segments:
        
        if segment['speaker'] != "unkhown":
            speaker = segment['speaker']
        else:
            continue

        start_time = float(segment['start'])
        end_time = float(segment['end'])
        duration = end_time - start_time
        
        # Check if this is the longest segment for this speaker
        if speaker not in longest_segments or duration > longest_segments[speaker]['duration']:
            longest_segments[speaker] = {'start_time': start_time, 'end_time': end_time, 'duration': duration}

    # Extract and save the longest segment for each speaker
    file_path = []
    for speaker, segment in longest_segments.items():
        start_sample = int(segment['start_time'] * sr)
        end_sample = int(segment['end_time'] * sr)
        speaker_audio = audio[start_sample:end_sample]

        # Save the extracted audio
        output_file = f'{output_path}/speakersample/speaker_{speaker}.wav'
        sf.write(output_file, speaker_audio, sr)
        file_path.append(output_file)
        
    return file_path    