import os
import cv2

from moviepy.editor import ImageSequenceClip, AudioFileClip

def images_with_audio_to_video(image_folder, audio_path, video_name, fps):
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    images.sort()  # Make sure images are in the correct order

    audio_clip = AudioFileClip(audio_path)
    video_clip = ImageSequenceClip([os.path.join(image_folder, img) for img in images], fps=fps)

    video_clip = video_clip.set_audio(audio_clip)

    video_clip.write_videofile(video_name, codec="libx264")

    video_clip.close()

# 이미지들이 저장된 폴더 경로
image_folder = '/home2/intern4/project/Difftalk/result/11_without_high_epoch_20'

# 오디오 파일 경로
audio_path = '/home2/intern4/project/Difftalk/data/preprocessing/video_audio/32/32_000_mono.wav'

# 생성할 동영상 파일명과 FPS 설정
video_name = '32_without_high_epoch_20_0806.avi'
fps = 25

# 이미지들을 동영상으로 변환
images_with_audio_to_video(image_folder, audio_path, video_name, fps)
