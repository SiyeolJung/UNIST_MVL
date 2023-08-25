import os
import matplotlib.pyplot as plt

def read_txt_files_in_subfolders(parent_folder):
    listener_txt_files = []
    speaker_txt_files = []

    for root, dirs, filedomg in os.walk(parent_folder):
        for dir in dirs:
            if dir.split('.')[1] == 'listener':
                listener_dir_path = os.path.join(root, dir)
                for file in os.listdir(listener_dir_path):
                    # file_path = os.path.join(root, dir, file)
                    if file.endswith(".txt"):
                        file_path = os.path.join(root, dir, file)
                        with open(file_path, "r") as f:
                            content = [f.read().strip().split('\n')]
                            listener_txt_files.append((file_path, content))
            elif dir.split('.')[1] == 'speaker':
                speaker_dir_path = os.path.join(root, dir)
                for file in os.listdir(speaker_dir_path):
                    if file.endswith(".txt"):
                        file_path = os.path.join(root, dir, file)
                        with open(file_path, "r") as f:
                            content = [f.read().strip().split('\n')]
                            speaker_txt_files.append((file_path, content))
    
    return listener_txt_files, speaker_txt_files

def count_each_emotion(emotion_list):
    count_emotion = {
        'Anger': 0,
        'Contempt': 0,
        'Disgust': 0,
        'Fear': 0,
        'Happiness': 0,
        'Neutral': 0,
        'Sadness': 0,
        'Surprise': 0
    }

    for emotion in emotion_list:
        e = emotion[1]
        for key in range(len(e)):
            if e[0][key] in count_emotion:
                count_emotion[e[0][key]] +=1

    return count_emotion


# 특정 폴더 경로 지정
parent_folder = "/home2/intern4/project/ListenerGeneration/face_emotion_recognition/result"

# 모든 하위 폴더 안의 txt 파일 읽어오기
listener_emotion_list, speaker_emotion_list = read_txt_files_in_subfolders(parent_folder)
# print(listener_emotion_list)
listener_dict = count_each_emotion(listener_emotion_list)
speaker_dict = count_each_emotion(speaker_emotion_list)
# print(listener_dict)
# print(speaker_dict)


labels = list(listener_dict.keys())
sizes = list(listener_dict.values())
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, autopct=lambda p: '{:.1f}%\n({:.0f})'.format(p, p * sum(sizes) / 100), startangle=140)
plt.axis('equal')  # 원형으로 보이도록 설정

# 시각화된 파이 차트를 이미지 파일로 저장
plt.savefig('listener_dict.png')

labels = list(speaker_dict.keys())
sizes = list(speaker_dict.values())
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, autopct=lambda p: '{:.1f}%\n({:.0f})'.format(p, p * sum(sizes) / 100), startangle=140)
plt.axis('equal')  # 원형으로 보이도록 설정

# 시각화된 파이 차트를 이미지 파일로 저장
plt.savefig('speaker_dict.png')
# 읽어온 txt 파일 리스트 출력
# for file_path, content in txt_files:
#     print("File Path:", file_path)
#     print("Content:", content)
#     print("---------------------")
