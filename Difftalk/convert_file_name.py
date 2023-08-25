import os

def rename_files(folder_path, folder_name):
    file_list = os.listdir(folder_path)  # 폴더 내의 파일 목록 가져오기

    for i, filename in enumerate(file_list):
        # 파일의 확장자 추출
        file_ext = os.path.splitext(filename)[1]
        
        # 새로운 파일 이름 생성
        new_filename = f"{folder_name}_{i}{file_ext}"
        
        # 파일의 현재 경로와 새로운 경로 생성
        current_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)
        
        # 파일 이름 변경
        os.rename(current_path, new_path)
        
        print(f"{filename} -> {new_filename}")

for i in range(0,80):
    folder_path = "/home2/intern4/project/Difftalk/data/preprocessing/new_audio_smooth/{}".format(i)  # 대상 폴더 경로로 변경해야 함
    # 파일 이름 변경 함수 호출
    rename_files(folder_path, i)
