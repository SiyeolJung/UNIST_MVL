import os
import librosa
import numpy as np

def process_audio(audio_file, video_frame_rate = 25):
    audio, sr = librosa.load(audio_file, sr=None)
    
    # frame_size = sr // 20
    # frame_size = audio // (sr*25) 
    # frame_size = audio // sr
    # hop_size = frame_size // 16

    frame_size =  
    hop_size =  vg

    # # Divide the audio into overlapping windows
    audio_windows = librosa.util.frame(audio, frame_length=frame_size, hop_length=hop_size)
    
    print(audio_windows.shape)
    # for i, window in enumerate(audio_windows):
    #     numpy_feature = np.array(window)
    #     output_file_path = output_path + '{}_{}.npy'.format(video_sequence,i)
    #     np.save(output_file_path,numpy_feature)
    print(audio.shape)
    print(sr)

audio_path = '/home2/intern4/project/Difftalk/data/preprocessing/video_audio/2/2_000.wav'
process_audio(audio_path)