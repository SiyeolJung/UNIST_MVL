import os

def count_files_in_folder(folder_path):
    # 해당 폴더 내의 파일 리스트를 가져옴
    files = os.listdir(folder_path)
    # 파일의 개수를 반환
    return len(files)

def delete_last_modified_file(folder_path):
    # 해당 폴더 내의 파일 리스트를 가져옴
    files = os.listdir(folder_path)
    
    # 파일 리스트를 수정 시간을 기준으로 내림차순으로 정렬
    sorted_files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(folder_path, x)), reverse=True)
    
    if sorted_files:
        # 가장 마지막으로 수정된 파일의 경로
        last_modified_file = os.path.join(folder_path, sorted_files[0])
        
        # 파일 삭제
        os.remove(last_modified_file)
        print("가장 마지막으로 수정된 파일을 삭제했습니다:", last_modified_file)
        print(last_modified_file)
    else:
        print("폴더가 비어있습니다.")    

# 비교할 두 개의 폴더 경로
folder_path1 = "/path/to/folder1"
folder_path2 = "/path/to/folder2"
for i in range(0,80):
    folder_path1 = '/home2/intern4/project/Difftalk/data/preprocessing/images/{}/'.format(i)
    folder_path2 = '/home2/intern4/project/Difftalk/data/preprocessing/new_audio_smooth/{}/'.format(i)
    # delete_last_modified_file(folder_path2)
    # 폴더1과 폴더2의 파일 개수를 세어 비교
    num_files_folder1 = count_files_in_folder(folder_path1)
    num_files_folder2 = count_files_in_folder(folder_path2)

    # print(num_files_folder1)
    # print(num_files_folder2)
    # 결과 출력
    # print("폴더1 파일 개수:", num_files_folder1)
    # print("폴더2 파일 개수:", num_files_folder2)
    
    # 비교
    # if num_files_folder1 == num_files_folder2:
        # print("두 폴더의 파일 개수가 같습니다.")
    if num_files_folder1 > num_files_folder2:
        print("{}의 파일 개수가 더 많습니다.".format(folder_path1))
    elif num_files_folder1 < num_files_folder2:
        print("{}의 파일 개수가 더 많습니다.".format(folder_path2))
    else:
        pass
