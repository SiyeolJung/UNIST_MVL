import os
import glob
import numpy as np
import wave
from pydub import AudioSegment

def get_wav_file_paths(folder_path):
    """
    주어진 폴더 경로에서 wav 파일들의 경로를 추출합니다.

    Parameters:
        folder_path (str): wav 파일들이 있는 폴더 경로

    Returns:
        List[str]: 폴더 안의 wav 파일들의 경로를 담고 있는 리스트
    """
    wav_file_paths = glob.glob(os.path.join(folder_path, "*.wav"))
    return wav_file_paths

def convert_to_mono(wav_file, output_file):
    # 오디오 파일 불러오기
    sound = AudioSegment.from_wav(wav_file)

    # 채널 수 변경 (모노로 변환)
    sound = sound.set_channels(1)

    # 샘플 레이트 변경 (16kHz로 변환)
    desired_sample_rate = 16000
    sound = sound.set_frame_rate(desired_sample_rate)

    # WAV 파일로 내보내기
    sound.export(output_file, format = "wav")

for i in range(0,80):
    folder_path = "/home2/intern4/project/Difftalk/data/preprocessing/video_audio/{}".format(i)
    wav_file = get_wav_file_paths(folder_path)[0]
    output_file, ext = os.path.splitext(wav_file)
    output_file = output_file + "_mono"+ ext
    convert_to_mono(wav_file, output_file)