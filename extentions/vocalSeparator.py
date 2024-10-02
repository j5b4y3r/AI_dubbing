# Separate Vocal and Music from a Audio.
import subprocess, os
import torchaudio

def separator(input_audio, output_directory):
    # Set the audio backend to soundfile
    torchaudio.set_audio_backend("soundfile")

    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Run Demucs to separate the audio
    command = ['demucs', '--two-stems=vocals', input_audio, '-o', output_directory]
    
    try:
        # Run the command and wait for it to finish
        subprocess.run(command, check=True)  # Using check=True to raise an error if command fails
        print(f"Separation complete! Check the output at: {output_directory}")
        
        # Return paths of the separated audio files
        return {
            'vocals': os.path.join(output_directory, 'htdemucs/audio', 'vocals.wav').replace("\\","/"),
            'no_vocals': os.path.join(output_directory, 'htdemucs/audio', 'no_vocals.wav').replace("\\","/")
        }
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while separating audio: {e}")
        return None

# This will save two files:
# 1. vocals.wav - contains only the vocals
# 2. no_vocals.wav - contains all music and instruments without vocals
