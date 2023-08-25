import os

def save_file_names_to_txt(folder_path, output_file):
    # 폴더 내부의 파일명을 읽어옵니다
    with open(output_file, "a") as f:
        for filename in os.listdir(folder_path):
            # 디렉토리나 하위 폴더 등을 제외하고 파일명만 저장합니다
            if os.path.isfile(os.path.join(folder_path, filename)):
                f.write(filename.split('.')[0] + "\n")

# 폴더 내부의 파일명을 저장할 폴더 경로와 저장될 txt 파일명을 설정합니다
output_file = "data_test5.txt"

for i in range(20,30):
    folder_path = "/home2/intern4/project/Difftalk/data/preprocessing/new_audio_smooth/{}".format(i)
    save_file_names_to_txt(folder_path, output_file)
