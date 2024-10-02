import librosa
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def detect_speekers(audio_file_path):
    audio, sr = librosa.load(audio_file_path, sr=None)
    mfccs = librosa.feature.mfcc(y=audio, sr=sr)
    scaler = StandardScaler()
    mfccs_scaled = scaler.fit_transform(mfccs.T)
    kmeans = KMeans(n_clusters=2)  # Adjust based on the expected number of speakers
    speaker_labels = kmeans.fit_predict(mfccs_scaled)
    # Calculate the time (in seconds) for each MFCC frame
    frame_times = librosa.frames_to_time(np.arange(mfccs.shape[1]), sr=sr, hop_length=512)
    return speaker_labels, frame_times