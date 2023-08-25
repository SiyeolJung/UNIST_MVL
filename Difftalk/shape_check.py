# import os
# import numpy as np

# folder_path = "/home2/intern4/project/Difftalk/data/HDTF/landmarks"  # 폴더 경로 설정
# previous_shape = None  # 이전의 shape 초기화

# # 폴더 내부의 파일들을 반복하여 처리
# for filename in os.listdir(folder_path):
#     file_path = os.path.join(folder_path, filename)
    
#     # npy 파일인지 확인
#     if filename.endswith(".npy"):
#         # Numpy npy 파일 로드
#         array = np.load(file_path)
        
#         # 이전의 shape와 현재 shape 비교
#         if previous_shape is None:
#             previous_shape = array.shape
#         elif array.shape != previous_shape:
#             print(f"File: {filename}, Previous shape: {previous_shape}, Current shape: {array.shape}")
        
#         # 이전의 shape 업데이트
#         previous_shape = array.shape

# import os
# import cv2

# folder_path = "/home2/intern4/project/Difftalk/data/HDTF/images"  # 폴더 경로 설정
# previous_shape = None  # 이전의 shape 초기화

# # 폴더 내부의 파일들을 반복하여 처리
# for filename in os.listdir(folder_path):
#     file_path = os.path.join(folder_path, filename)
    
#     # 이미지 파일인지 확인
#     if filename.endswith((".png", ".jpg", ".jpeg")):
#         # 이미지 파일 로드
#         image = cv2.imread(file_path)
        
#         # 이미지 shape 확인
#         current_shape = image.shape[:2]  # (높이, 너비)
        
#         # 이전의 shape와 현재 shape 비교
#         if previous_shape is None:
#             previous_shape = current_shape
#         elif current_shape != previous_shape:
#             print(f"File: {filename}, Previous shape: {previous_shape}, Current shape: {current_shape}")
        
#         # 이전의 shape 업데이트
#         previous_shape = current_shape


import os
import numpy as np

def count_shape_mismatches(folder_path):
    prev_shape = None
    num_mismatches = 0

    for filename in os.listdir(folder_path):
        if filename.endswith('.npy'):
            file_path = os.path.join(folder_path, filename)
            current_array = np.load(file_path)

            if prev_shape is not None and current_array.shape != prev_shape:
                num_mismatches += 1
            
            prev_shape = current_array.shape

    return num_mismatches

def update_shapes(folder_path):
    prev_shape = None

    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith('.npy'):
            file_path = os.path.join(folder_path, filename)
            current_array = np.load(file_path)

            if prev_shape is not None and current_array.shape != prev_shape:
                print(f"Shape mismatch detected: Overwriting {filename} with the previous file.")
                np.save(file_path, prev_array)
                current_array = prev_array  # Update current_array to the previous array

            prev_shape = current_array.shape
            prev_array = current_array

update_shapes('/home2/intern4/project/Difftalk/data/HDTF/landmarks2')
# print(mismatch_count)
