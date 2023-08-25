# import os
# import numpy as np

# def are_npy_files_equal(file_path1, file_path2):
#     data1 = np.load(file_path1)
#     data2 = np.load(file_path2)
#     return np.array_equal(data1, data2)

# def check_npy_files_in_folders(folder_path1, folder_path2):
#     npy_files1 = [file for file in os.listdir(folder_path1) if file.endswith(".npy")]
#     npy_files2 = [file for file in os.listdir(folder_path2) if file.endswith(".npy")]

#     if len(npy_files1) != len(npy_files2):
#         print("The number of npy files in the two folders does not match.")
#         return

#     for file1, file2 in zip(npy_files1, npy_files2):
#         file_path1 = os.path.join(folder_path1, file1)
#         file_path2 = os.path.join(folder_path2, file2)

#         if are_npy_files_equal(file_path1, file_path2):
#             print(f"{file1} and {file2} match.")
#         else:
#             print(f"{file1} and {file2} do not match.")

# # 두 개의 폴더 경로
# folder_path1 = "/home2/intern4/project/Difftalk/data/preprocessing/audio_smooth/0"
# folder_path2 = "/home2/intern4/project/Difftalk/data/preprocessing/audio_smooth/2"

# # 두 폴더 속 npy 파일 일치 여부 확인
# check_npy_files_in_folders(folder_path1, folder_path2)


import os

# 폴더 경로 설정
folder_path = '/home2/intern4/project/Difftalk/data/preprocessing/images/32'

# 파일 목록을 가져옴
file_list = os.listdir(folder_path)

# 파일 이름에서 확장자 제거
file_names = [os.path.splitext(file)[0] for file in file_list]

# 파일 이름을 텍스트 파일로 저장
output_file = '/home2/intern4/project/Difftalk/data/data_real_test3.txt'
with open(output_file, 'w') as f:
    for name in file_names:
        f.write(name + '\n')

print(f"File names saved to {output_file}")
