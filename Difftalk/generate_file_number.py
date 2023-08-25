import os

folder_path = "/home2/intern4/project/Difftalk/data/HDTF/audio_smooth"  # 대상 폴더 경로로 변경해야 함
output_file_path = "/home2/intern4/project/Difftalk/data/data_test.txt"  # 출력 파일 경로와 파일명으로 변경해야 함

def save_file_names_to_txt(folder_path, output_file_path):
    file_list = os.listdir(folder_path)  # 폴더 내의 파일 목록 가져오기

    with open(output_file_path, "w") as f:
        for filename in file_list:
            f.write(filename.split('.')[0] + "\n")
            print(filename)

    print("File names saved to", output_file_path)

# 폴더의 모든 파일 이름을 출력하여 텍스트 파일로 저장하는 함수 호출
save_file_names_to_txt(folder_path, output_file_path)
