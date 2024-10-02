import sys
import os

# Add the parent directory (Ai_dubbing) to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
'''
from extentions.downloader import download_video

video_url = "https://example.com/video.mp4"  # Direct URL
youtube_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # YouTube link
tiktok_url = "https://www.tiktok.com/@someuser/video/1234567890"  # TikTok link

#download_video(video_url, "./downloads")  # Direct video
#download_video(youtube_url, "./downloads", download_audio=False)  # YouTube video
#download_video(tiktok_url, "./downloads", download_audio=False)  # TikTok video
#w = "C:\\Users\\user\\Desktop\\Project\\Ai_dubbing\\downloads\\Rick Astley - Never Gonna Give You Up (Official Music Video).webm"            
#mp4_file = os.path.splitext(w)[0] + '.mp4'


from extentions.audioSeparator import separate

input_path = "C:\\Users\\user\\Desktop\\Project\\Ai_dubbing\\downloads\\Hello I'm Cristiano Ronaldo (Original Video).mkv"
audio_path = "./downloads/audio.mp3"
video_path = "./downloads/video.mp4"

separate(input_video_path=input_path, audio_output_path=audio_path, video_output_path=video_path)

# <FAILED

from extentions.vocalSeparator import separator

input_path = "C:\\Users\\user\\Desktop\\Project\\Ai_dubbing\\downloads\\audio.mp3"
output_path = "C:\\Users\\user\\Desktop\\Project\\Ai_dubbing\\temp\\vocalSeparator\\outputs"

separator(input_path, output_path)

# FAILED>



from extentions.stt import get_text

wav_path = "C:\\Users\\user\\Desktop\\Project\\Ai_dubbing\\downloads\\audio.mp3"
print(get_text(wav_path))



from extentions.translator import translate_text

# Example usage
text_to_translate = "The tradition of Bengali language and literature is more than thousand years old. Charyapad, a collection of Buddhist scriptures written in the 7th century, is recognized as the oldest exemplar of the Bengali language. Poetry, folk songs and palagan became popular in the Bengali language during the Middle Ages. Bengali poetry and prose literature developed extensively in the nineteenth and twentieth centuries. Kazi Nazrul Islam, the national poet of Bangladesh, enriched literature in the Bengali language. Folk literature of Bengal is also rich; Its identity is found in Mymensingh Gitika."  # Text in Spanish
text = translate_text(text_to_translate, from_language='en', target_language='bn')  # Translate to English
# Use 'utf-8' encoding when writing to the file
with open('C:\\Users\\user\\Desktop\\Project\\Ai_dubbing\\temp\\translate\\translated_text.txt', 'w', encoding='utf-8') as f:
    f.write(text)


from extentions.tts import get_speech

os.system("start "+get_speech())

from extentions.tts import get_voice_over_speech, load_tts_model

sample_wav = "C:\\Users\\user\\Downloads\\Music\\Cristiano Ronaldo Sounds.mp3"
model=load_tts_model()
get_voice_over_speech(text="Hello, I am Cristiano Ronaldo and top jurnalist, i am here in Canada ", sample_wav=sample_wav, path="./", model=model)



from extentions.stt import get_transcribed

wav_path = "C:\\Users\\user\\Desktop\\Project\\Ai_dubbing\\downloads\\audio.mp3"
print(get_transcribed(wav_path))


from pydub import AudioSegment

audio = AudioSegment.from_mp3("C:\\Users\\user\\Desktop\\Project\\Ai_dubbing\\dubbed\\temp_segment.mp3")
audio.play()


output_directory = "C:/Users/user/Desktop/Project/Ai_dubbing/temp/vocalSeparator/outputs"

def a():
    return {
            'vocals': os.path.join(output_directory, 'htdemucs/audio', 'vocals.wav').replace("\\","/"),
            'no_vocals': os.path.join(output_directory, 'htdemucs/audio', 'no_vocals.wav')
        }
print(a())'''

'''
from extentions.speakerDiarization import detect_speekers
from extentions.saveSpeakersVoice import save_speaker_sample
from dubbing import assign_speakers_to_transcript
from pydub import AudioSegment
print("labeling speakers")
a = "C:\\Users\\user\\Desktop\\Project\\Ai_dubbing\\temp\\htdemucs\\audio\\vocals.wav"
labels, times = detect_speekers("C:\\Users\\user\\Desktop\\Project\\Ai_dubbing\\temp\\htdemucs\\audio\\vocals.wav")
#transcribed_audio = transcribe("C:\\Users\\user\\Desktop\\Project\\Ai_dubbing\\temp\\htdemucs\\audio\\vocals.wav")
transcribed_audio = {'text': " As the days pass, my emotions grow more distant. Fear, tension, joy, anger, the film none of them anymore. In exchange for power, maybe I've lost something that's essential for being human. Before, I have all kinds of emotions whirling inside me when I fought. Dread, panic, rage. But now, all I needed one punch, Dan. It!'s enough... Don't you think the emotion right now, Dan?", 'segments': [{'id': 0, 'seek': 0, 'start': 0.0, 'end': 4.02, 'text': ' As the days pass, my emotions grow more distant.', 'tokens': [50364, 1018, 264, 1708, 1320, 11, 452, 8462, 1852, 544, 17275, 13, 50614], 'temperature': 0.0, 'avg_logprob': -0.24412218729654947, 'compression_ratio': 1.4929577464788732, 'no_speech_prob': 0.5709728598594666, 'words': [{'word': ' As', 'start': 0.0, 'end': 1.14, 'probability': 0.42341989278793335}, {'word': ' the', 'start': 1.14, 'end': 1.28, 'probability': 0.9894163012504578}, {'word': ' days', 'start': 1.28, 'end': 1.5, 'probability': 0.9425926208496094}, {'word': ' pass,', 'start': 1.5, 'end': 1.94, 'probability': 0.9811850190162659}, {'word': ' my', 'start': 2.62, 'end': 2.64, 'probability': 0.9239098429679871}, {'word': ' emotions', 'start': 2.64, 'end': 2.98, 'probability': 0.9880443215370178}, {'word': ' grow', 'start': 2.98, 'end': 3.34, 'probability': 0.9547764658927917}, {'word': ' more', 'start': 3.34, 'end': 3.6, 'probability': 0.9953951239585876}, {'word': ' distant.', 'start': 3.6, 'end': 4.02, 'probability': 0.8754667043685913}]}, {'id': 1, 'seek': 0, 'start': 4.879999999999999, 'end': 9.96, 'text': ' Fear, tension, joy, anger, the film none of them anymore.', 'tokens': [50614, 28054, 11, 8980, 11, 6258, 11, 10240, 11, 264, 2007, 6022, 295, 552, 3602, 13, 50864], 'temperature': 0.0, 'avg_logprob': -0.24412218729654947, 'compression_ratio': 1.4929577464788732, 'no_speech_prob': 0.5709728598594666, 'words': [{'word': ' Fear,', 'start': 4.879999999999999, 'end': 5.48, 'probability': 0.9599068760871887}, {'word': ' tension,', 'start': 5.96, 'end': 6.24, 'probability': 0.9953906536102295}, {'word': ' joy,', 'start': 6.94, 'end': 7.16, 'probability': 0.9980170726776123}, {'word': ' anger,', 'start': 7.7, 'end': 8.04, 'probability': 0.9985989928245544}, {'word': ' the', 'start': 8.5, 'end': 8.78, 'probability': 0.8274589776992798}, {'word': ' film', 'start': 8.78, 'end': 9.0, 'probability': 0.9113739132881165}, {'word': ' none', 'start': 9.0, 'end': 9.22, 'probability': 0.9758138060569763}, {'word': ' of', 'start': 9.22, 'end': 9.38, 'probability': 0.9979098439216614}, {'word': ' them', 'start': 9.38, 'end': 9.5, 'probability': 0.9626871943473816}, {'word': ' anymore.', 'start': 9.5, 'end': 9.96, 'probability': 0.9641185998916626}]}, {'id': 2, 'seek': 0, 'start': 10.6, 'end': 15.04, 'text': " In exchange for power, maybe I've lost something that's essential for being human.", 'tokens': [50864, 682, 7742, 337, 1347, 11, 1310, 286, 600, 2731, 746, 300, 311, 7115, 337, 885, 1952, 13, 51114], 'temperature': 0.0, 'avg_logprob': -0.24412218729654947, 'compression_ratio': 1.4929577464788732, 'no_speech_prob': 0.5709728598594666, 'words': [{'word': ' In', 'start': 10.6, 'end': 10.8, 'probability': 0.6145931482315063}, {'word': ' exchange', 'start': 10.8, 'end': 11.06, 'probability': 0.9646806120872498}, {'word': ' for', 'start': 11.06, 'end': 11.42, 'probability': 0.9949647188186646}, {'word': ' power,', 'start': 11.42, 'end': 11.9, 'probability': 0.9947142004966736}, {'word': ' maybe', 'start': 12.4, 'end': 12.54, 'probability': 0.546798825263977}, {'word': " I've", 'start': 12.54, 'end': 12.82, 'probability': 0.9408747255802155}, {'word': ' lost', 'start': 12.82, 'end': 12.96, 'probability': 0.9990418553352356}, {'word': ' something', 'start': 12.96, 'end': 13.52, 'probability': 0.9982989430427551}, {'word': " that's", 'start': 13.52, 'end': 13.8, 'probability': 0.9846116602420807}, {'word': ' essential', 'start': 13.8, 'end': 14.22, 'probability': 0.998150646686554}, {'word': ' for', 'start': 14.22, 'end': 14.44, 'probability': 0.9915749430656433}, {'word': ' being', 'start': 14.44, 'end': 14.64, 'probability': 0.9977816939353943}, {'word': ' human.', 'start': 14.64, 'end': 15.04, 'probability': 0.9855003952980042}]}, {'id': 3, 'seek': 0, 'start': 15.68, 'end': 19.1, 'text': ' Before, I have all kinds of emotions whirling inside me when I fought.', 'tokens': [51114, 4546, 11, 286, 362, 439, 3685, 295, 8462, 35706, 278, 1854, 385, 562, 286, 11391, 13, 51314], 'temperature': 0.0, 'avg_logprob': -0.24412218729654947, 'compression_ratio': 1.4929577464788732, 'no_speech_prob': 0.5709728598594666, 'words': [{'word': ' Before,', 'start': 15.68, 'end': 16.02, 'probability': 0.794825553894043}, {'word': ' I', 'start': 16.32, 'end': 16.38, 'probability': 0.9572603106498718}, {'word': ' have', 'start': 16.38, 'end': 16.56, 'probability': 0.9538009762763977}, {'word': ' all', 'start': 16.56, 'end': 16.72, 'probability': 0.9971222281455994}, {'word': ' kinds', 'start': 16.72, 'end': 17.06, 'probability': 0.9973045587539673}, {'word': ' of', 'start': 17.06, 'end': 17.24, 'probability': 0.9993698000907898}, {'word': ' emotions', 'start': 17.24, 'end': 17.56, 'probability': 0.9984933137893677}, {'word': ' whirling', 'start': 17.56, 'end': 18.1, 'probability': 0.7713062465190887}, {'word': ' inside', 'start': 18.1, 'end': 18.44, 'probability': 0.7440532445907593}, {'word': ' me', 'start': 18.44, 'end': 18.62, 'probability': 0.6967713832855225}, {'word': ' when', 'start': 18.62, 'end': 18.76, 'probability': 0.9425510168075562}, {'word': ' I', 'start': 18.76, 'end': 18.88, 'probability': 0.9976388216018677}, {'word': ' fought.', 'start': 18.88, 'end': 19.1, 'probability': 0.8386908173561096}]}, {'id': 4, 'seek': 0, 'start': 19.9, 'end': 21.84, 'text': ' Dread, panic, rage.', 'tokens': [51314, 413, 2538, 11, 14783, 11, 20133, 13, 51464], 'temperature': 0.0, 'avg_logprob': -0.24412218729654947, 'compression_ratio': 1.4929577464788732, 'no_speech_prob': 0.5709728598594666, 'words': [{'word': ' Dread,', 'start': 19.9, 'end': 20.1, 'probability': 0.6053729504346848}, {'word': ' panic,', 'start': 20.7, 'end': 21.0, 'probability': 0.648383617401123}, {'word': ' rage.', 'start': 21.64, 'end': 21.84, 'probability': 0.9994383454322815}]}, {'id': 5, 'seek': 0, 'start': 22.76, 'end': 25.76, 'text': ' But now, all I needed one punch, Dan.', 'tokens': [51464, 583, 586, 11, 439, 286, 2978, 472, 8135, 11, 3394, 13, 51664], 'temperature': 0.0, 'avg_logprob': -0.24412218729654947, 'compression_ratio': 1.4929577464788732, 'no_speech_prob': 0.5709728598594666, 'words': [{'word': ' But', 'start': 22.76, 'end': 23.16, 'probability': 0.9928251504898071}, {'word': ' now,', 'start': 23.16, 'end': 23.5, 'probability': 0.9882498979568481}, {'word': ' all', 'start': 24.18, 'end': 24.42, 'probability': 0.9956116080284119}, {'word': ' I', 'start': 24.42, 'end': 24.56, 'probability': 0.9977288842201233}, {'word': ' needed', 'start': 24.56, 'end': 24.8, 'probability': 0.6888183355331421}, {'word': ' one', 'start': 24.8, 'end': 25.1, 'probability': 0.6573509573936462}, {'word': ' punch,', 'start': 25.1, 'end': 25.52, 'probability': 0.9474850296974182}, {'word': ' Dan.', 'start': 25.58, 'end': 25.76, 'probability': 0.4010493755340576}]}, {'id': 6, 'seek': 3000, 'start': 46.1, 'end': 46.4, 'text': " It!'s enough...", 'tokens': [50414, 467, 13840, 82, 1547, 485, 50514], 'temperature': 1.0, 'avg_logprob': -3.152486627752131, 'compression_ratio': 0.9076923076923077, 'no_speech_prob': 0.3738541901111603, 'words': [{'word': " It!'s", 'start': 46.1, 'end': 46.38, 'probability': 0.3302035679853361}, {'word': ' enough...', 'start': 46.38, 'end': 46.4, 'probability': 0.007755625119898468}]}, {'id': 7, 'seek': 3000, 'start': 46.4, 'end': 46.54, 'text': " Don't you think the emotion right now, Dan?", 'tokens': [50614, 1468, 380, 291, 519, 264, 8913, 558, 586, 11, 3394, 30, 50864], 'temperature': 1.0, 'avg_logprob': -3.152486627752131, 'compression_ratio': 0.9076923076923077, 'no_speech_prob': 0.3738541901111603, 'words': [{'word': " Don't", 'start': 46.4, 'end': 46.54, 'probability': 0.36353308777324855}, {'word': ' you', 'start': 46.54, 'end': 46.54, 'probability': 0.08085539191961288}, {'word': ' think', 'start': 46.54, 'end': 46.54, 'probability': 0.23761112987995148}, {'word': ' the', 'start': 46.54, 'end': 46.54, 'probability': 0.01860957033932209}, {'word': ' emotion', 'start': 46.54, 'end': 46.54, 'probability': 5.326165774022229e-05}, {'word': ' right', 'start': 46.54, 'end': 46.54, 'probability': 0.0008186291088350117}, {'word': ' now,', 'start': 46.54, 'end': 46.54, 'probability': 0.35216885805130005}, {'word': ' Dan?', 'start': 46.54, 'end': 46.54, 'probability': 0.0011925711296498775}]}], 'language': 'en'}

u = assign_speakers_to_transcript(transcribed_audio['segments'], labels, times)

files = save_speaker_sample(a,u, "temp")
print(files)
'''
from pydub import AudioSegment

# Load the audio file
audio_file = AudioSegment.from_file("C:\\Users\\user\\Desktop\\Project\\Ai_dubbing\\temp\\htdemucs\\audio\\vocals.wav")

# Change the playback speed (e.g., 1.5x faster)
#audio_file_speed_changed = audio_file._spawn(audio_file.raw_data, overrides={"frame_rate": int(audio_file.frame_rate * 1.0)})

# Export the audio file with the new playback speed
audio_file.export("output.mp3", format="mp3", parameters=["-filter:a", "atempo=1.5"])       

#obj = assign_speakers_to_transcript(transcribed_audio['segments'], labels, times)
#print(obj)
'''
t = {'text': " As the days pass, my emotions grow more distant. Fear, tension, joy, anger, the film none of them anymore. In exchange for power, maybe I've lost something that's essential for being human. Before, I have all kinds of emotions whirling inside me when I fought. Dread, panic, rage. But now, all I needed one punch, Dan. It!'s enough... Don't you think the emotion right now, Dan?", 'segments': [{'id': 0, 'seek': 0, 'start': 0.0, 'end': 4.02, 'text': ' As the days pass, my emotions grow more distant.', 'tokens': [50364, 1018, 264, 1708, 1320, 11, 452, 8462, 1852, 544, 17275, 13, 50614], 'temperature': 0.0, 'avg_logprob': -0.24412218729654947, 'compression_ratio': 1.4929577464788732, 'no_speech_prob': 0.5709728598594666, 'words': [{'word': ' As', 'start': 0.0, 'end': 1.14, 'probability': 0.42341989278793335}, {'word': ' the', 'start': 1.14, 'end': 1.28, 'probability': 0.9894163012504578}, {'word': ' days', 'start': 1.28, 'end': 1.5, 'probability': 0.9425926208496094}, {'word': ' pass,', 'start': 1.5, 'end': 1.94, 'probability': 0.9811850190162659}, {'word': ' my', 'start': 2.62, 'end': 2.64, 'probability': 0.9239098429679871}, {'word': ' emotions', 'start': 2.64, 'end': 2.98, 'probability': 0.9880443215370178}, {'word': ' grow', 'start': 2.98, 'end': 3.34, 'probability': 0.9547764658927917}, {'word': ' more', 'start': 3.34, 'end': 3.6, 'probability': 0.9953951239585876}, {'word': ' distant.', 'start': 3.6, 'end': 4.02, 'probability': 0.8754667043685913}]}, {'id': 1, 'seek': 0, 'start': 4.879999999999999, 'end': 9.96, 'text': ' Fear, tension, joy, anger, the film none of them anymore.', 'tokens': [50614, 28054, 11, 8980, 11, 6258, 11, 10240, 11, 264, 2007, 6022, 295, 552, 3602, 13, 50864], 'temperature': 0.0, 'avg_logprob': -0.24412218729654947, 'compression_ratio': 1.4929577464788732, 'no_speech_prob': 0.5709728598594666, 'words': [{'word': ' Fear,', 'start': 4.879999999999999, 'end': 5.48, 'probability': 0.9599068760871887}, {'word': ' tension,', 'start': 5.96, 'end': 6.24, 'probability': 0.9953906536102295}, {'word': ' joy,', 'start': 6.94, 'end': 7.16, 'probability': 0.9980170726776123}, {'word': ' anger,', 'start': 7.7, 'end': 8.04, 'probability': 0.9985989928245544}, {'word': ' the', 'start': 8.5, 'end': 8.78, 'probability': 0.8274589776992798}, {'word': ' film', 'start': 8.78, 'end': 9.0, 'probability': 0.9113739132881165}, {'word': ' none', 'start': 9.0, 'end': 9.22, 'probability': 0.9758138060569763}, {'word': ' of', 'start': 9.22, 'end': 9.38, 'probability': 0.9979098439216614}, {'word': ' them', 'start': 9.38, 'end': 9.5, 'probability': 0.9626871943473816}, {'word': ' anymore.', 'start': 9.5, 'end': 9.96, 'probability': 0.9641185998916626}]}, {'id': 2, 'seek': 0, 'start': 10.6, 'end': 15.04, 'text': " In exchange for power, maybe I've lost something that's essential for being human.", 'tokens': [50864, 682, 7742, 337, 1347, 11, 1310, 286, 600, 2731, 746, 300, 311, 7115, 337, 885, 1952, 13, 51114], 'temperature': 0.0, 'avg_logprob': -0.24412218729654947, 'compression_ratio': 1.4929577464788732, 'no_speech_prob': 0.5709728598594666, 'words': [{'word': ' In', 'start': 10.6, 'end': 10.8, 'probability': 0.6145931482315063}, {'word': ' exchange', 'start': 10.8, 'end': 11.06, 'probability': 0.9646806120872498}, {'word': ' for', 'start': 11.06, 'end': 11.42, 'probability': 0.9949647188186646}, {'word': ' power,', 'start': 11.42, 'end': 11.9, 'probability': 0.9947142004966736}, {'word': ' maybe', 'start': 12.4, 'end': 12.54, 'probability': 0.546798825263977}, {'word': " I've", 'start': 12.54, 'end': 12.82, 'probability': 0.9408747255802155}, {'word': ' lost', 'start': 12.82, 'end': 12.96, 'probability': 0.9990418553352356}, {'word': ' something', 'start': 12.96, 'end': 13.52, 'probability': 0.9982989430427551}, {'word': " that's", 'start': 13.52, 'end': 13.8, 'probability': 0.9846116602420807}, {'word': ' essential', 'start': 13.8, 'end': 14.22, 'probability': 0.998150646686554}, {'word': ' for', 'start': 14.22, 'end': 14.44, 'probability': 0.9915749430656433}, {'word': ' being', 'start': 14.44, 'end': 14.64, 'probability': 0.9977816939353943}, {'word': ' human.', 'start': 14.64, 'end': 15.04, 'probability': 0.9855003952980042}]}, {'id': 3, 'seek': 0, 'start': 15.68, 'end': 19.1, 'text': ' Before, I have all kinds of emotions whirling inside me when I fought.', 'tokens': [51114, 4546, 11, 286, 362, 439, 3685, 295, 8462, 35706, 278, 1854, 385, 562, 286, 11391, 13, 51314], 'temperature': 0.0, 'avg_logprob': -0.24412218729654947, 'compression_ratio': 1.4929577464788732, 'no_speech_prob': 0.5709728598594666, 'words': [{'word': ' Before,', 'start': 15.68, 'end': 16.02, 'probability': 0.794825553894043}, {'word': ' I', 'start': 16.32, 'end': 16.38, 'probability': 0.9572603106498718}, {'word': ' have', 'start': 16.38, 'end': 16.56, 'probability': 0.9538009762763977}, {'word': ' all', 'start': 16.56, 'end': 16.72, 'probability': 0.9971222281455994}, {'word': ' kinds', 'start': 16.72, 'end': 17.06, 'probability': 0.9973045587539673}, {'word': ' of', 'start': 17.06, 'end': 17.24, 'probability': 0.9993698000907898}, {'word': ' emotions', 'start': 17.24, 'end': 17.56, 'probability': 0.9984933137893677}, {'word': ' whirling', 'start': 17.56, 'end': 18.1, 'probability': 0.7713062465190887}, {'word': ' inside', 'start': 18.1, 'end': 18.44, 'probability': 0.7440532445907593}, {'word': ' me', 'start': 18.44, 'end': 18.62, 'probability': 0.6967713832855225}, {'word': ' when', 'start': 18.62, 'end': 18.76, 'probability': 0.9425510168075562}, {'word': ' I', 'start': 18.76, 'end': 18.88, 'probability': 0.9976388216018677}, {'word': ' fought.', 'start': 18.88, 'end': 19.1, 'probability': 0.8386908173561096}]}, {'id': 4, 'seek': 0, 'start': 19.9, 'end': 21.84, 'text': ' Dread, panic, rage.', 'tokens': [51314, 413, 2538, 11, 14783, 11, 20133, 13, 51464], 'temperature': 0.0, 'avg_logprob': -0.24412218729654947, 'compression_ratio': 1.4929577464788732, 'no_speech_prob': 0.5709728598594666, 'words': [{'word': ' Dread,', 'start': 19.9, 'end': 20.1, 'probability': 0.6053729504346848}, {'word': ' panic,', 'start': 20.7, 'end': 21.0, 'probability': 0.648383617401123}, {'word': ' rage.', 'start': 21.64, 'end': 21.84, 'probability': 0.9994383454322815}]}, {'id': 5, 'seek': 0, 'start': 22.76, 'end': 25.76, 'text': ' But now, all I needed one punch, Dan.', 'tokens': [51464, 583, 586, 11, 439, 286, 2978, 472, 8135, 11, 3394, 13, 51664], 'temperature': 0.0, 'avg_logprob': -0.24412218729654947, 'compression_ratio': 1.4929577464788732, 'no_speech_prob': 0.5709728598594666, 'words': [{'word': ' But', 'start': 22.76, 'end': 23.16, 'probability': 0.9928251504898071}, {'word': ' now,', 'start': 23.16, 'end': 23.5, 'probability': 0.9882498979568481}, {'word': ' all', 'start': 24.18, 'end': 24.42, 'probability': 0.9956116080284119}, {'word': ' I', 'start': 24.42, 'end': 24.56, 'probability': 0.9977288842201233}, {'word': ' needed', 'start': 24.56, 'end': 24.8, 'probability': 0.6888183355331421}, {'word': ' one', 'start': 24.8, 'end': 25.1, 'probability': 0.6573509573936462}, {'word': ' punch,', 'start': 25.1, 'end': 25.52, 'probability': 0.9474850296974182}, {'word': ' Dan.', 'start': 25.58, 'end': 25.76, 'probability': 0.4010493755340576}]}, {'id': 6, 'seek': 3000, 'start': 46.1, 'end': 46.4, 'text': " It!'s enough...", 'tokens': [50414, 467, 13840, 82, 1547, 485, 50514], 'temperature': 1.0, 'avg_logprob': -3.152486627752131, 'compression_ratio': 0.9076923076923077, 'no_speech_prob': 0.3738541901111603, 'words': [{'word': " It!'s", 'start': 46.1, 'end': 46.38, 'probability': 0.3302035679853361}, {'word': ' enough...', 'start': 46.38, 'end': 46.4, 'probability': 0.007755625119898468}]}, {'id': 7, 'seek': 3000, 'start': 46.4, 'end': 46.54, 'text': " Don't you think the emotion right now, Dan?", 'tokens': [50614, 1468, 380, 291, 519, 264, 8913, 558, 586, 11, 3394, 30, 50864], 'temperature': 1.0, 'avg_logprob': -3.152486627752131, 'compression_ratio': 0.9076923076923077, 'no_speech_prob': 0.3738541901111603, 'words': [{'word': " Don't", 'start': 46.4, 'end': 46.54, 'probability': 0.36353308777324855}, {'word': ' you', 'start': 46.54, 'end': 46.54, 'probability': 0.08085539191961288}, {'word': ' think', 'start': 46.54, 'end': 46.54, 'probability': 0.23761112987995148}, {'word': ' the', 'start': 46.54, 'end': 46.54, 'probability': 0.01860957033932209}, {'word': ' emotion', 'start': 46.54, 'end': 46.54, 'probability': 5.326165774022229e-05}, {'word': ' right', 'start': 46.54, 'end': 46.54, 'probability': 0.0008186291088350117}, {'word': ' now,', 'start': 46.54, 'end': 46.54, 'probability': 0.35216885805130005}, {'word': ' Dan?', 'start': 46.54, 'end': 46.54, 'probability': 0.0011925711296498775}]}], 'language': 'en'}

import librosa
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

audio_path = 'C:\\Users\\user\\Desktop\\Project\\Ai_dubbing\\temp\\htdemucs\\audio\\vocals.wav'
audio, sr = librosa.load(audio_path, sr=None)
mfccs = librosa.feature.mfcc(y=audio, sr=sr)
scaler = StandardScaler()
mfccs_scaled = scaler.fit_transform(mfccs.T)
kmeans = KMeans(n_clusters=2)  # Adjust based on the expected number of speakers
speaker_labels = kmeans.fit_predict(mfccs_scaled)
for i, label in enumerate(speaker_labels):
    print(f"Time Segment {i}: Speaker {label}")'''