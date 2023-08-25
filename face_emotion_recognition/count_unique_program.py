import os

def count_subdirectories(folder_path):
    subdirectory_count = 0
    unique = set()
    # 폴더 내부 아이템 탐색
    for item in os.listdir(folder_path):
        unique.add(item.split('_')[0])
        # item_path = os.path.join(folder_path, item)
        # if os.path.isdir(item_path):  # 폴더인 경우
        #     subdirectory_count += 1

    return unique

# 폴더 경로 지정
folder_path = '/home2/intern4/project/ListenerGeneration/face_emotion_recognition/original_result'

# 서브폴더 개수 계산
subdirectory_count = count_subdirectories(folder_path)
print(f"서브폴더 개수: {(subdirectory_count)}")
