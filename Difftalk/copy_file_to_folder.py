import os
import shutil

def copy_files_in_folder(source_folder, destination_folder):
    # 폴더를 생성하거나 이미 존재하는지 확인
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # source_folder 내의 모든 파일들을 반복하여 복사
    for root, _, files in os.walk(source_folder):
        for file in files:
            source_path = os.path.join(root, file)
            destination_path = os.path.join(destination_folder, file)
            shutil.copy2(source_path, destination_path)  # 파일을 복사합니다

# 폴더 내부의 파일을 복사할 source_folder와 복사될 destination_folder를 설정합니다
audio_smooth_destination_folder = "/home2/intern4/project/Difftalk/data/HDTF/audio_smooth2"
images_destination_folder = "/home2/intern4/project/Difftalk/data/HDTF/images2"
land_mark_destination_folder = "/home2/intern4/project/Difftalk/data/HDTF/landmarks2"

for i in range(0,80):
    # audio_smooth_source_folder = "/home2/intern4/project/Difftalk/data/preprocessing/new_audio_smooth/{}".format(i)
    # copy_files_in_folder(audio_smooth_source_folder, audio_smooth_destination_folder)

    images_source_folder = "/home2/intern4/project/Difftalk/data/preprocessing/images/{}".format(i)
    copy_files_in_folder(images_source_folder, images_destination_folder)

    land_mark_source_folder = "/home2/intern4/project/Difftalk/data/preprocessing/landmarks/{}".format(i)
    copy_files_in_folder(land_mark_source_folder, land_mark_destination_folder)

