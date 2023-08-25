import pandas as pd
import matplotlib.pyplot as plt
import os 

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
        e = emotion
        for key in range(len(e)):
            if e[key] in count_emotion:
                count_emotion[e[key]] +=1

    return count_emotion

information = pd.read_csv('/home2/intern4/project/ListenerGeneration/dataset/RLD_data.csv')

listener = information.loc[information['attitude']=='negative','listener']
speaker = information.loc[information['attitude']=='negative','speaker']
# print(listener[0], speaker[0])
# listener = information.loc[information['attitude']=='positive',2]
# speaker = information.loc[information['attitude']=='positive',3]
# print(listener, speaker)
info = information.loc[information['attitude']=='negative',['listener','speaker']]

folder_path = '/home2/intern4/project/ListenerGeneration/face_emotion_recognition/original_result'
all_contents = os.listdir(folder_path)
folder_dict = {}
# 모든 내용물에 대해 반복
for content in all_contents:
    content_path = os.path.join(folder_path, content)
    
    # 폴더인지 확인
    if os.path.isdir(content_path):
        # 폴더 이름을 키로, 경로를 값으로 딕셔너리에 저장
        folder_name = content
        if folder_name in folder_dict:
            folder_dict[folder_name].append(content_path)
        else:
            folder_dict[folder_name] = [content_path]

total_listener_emotion = []
total_speaker_emotion = []

for i in info.index:
    listener_folder_name = info.loc[i].listener+'.mp4'
    speaker_folder_name = info.loc[i].speaker+'.mp4'

    listener_folder_path = folder_dict[listener_folder_name]
    speaker_folder_path = folder_dict[speaker_folder_name]
    listener_txt_files = [f for f in os.listdir(*listener_folder_path) if f.endswith('.txt')]
    speaker_txt_files = [f for f in os.listdir(*speaker_folder_path) if f.endswith('.txt')]

    for txtfile in listener_txt_files:
        txt_file_path = os.path.join(*listener_folder_path,txtfile)
        with open(txt_file_path, 'r') as txt_file:
                    listener_emotion = [txt_file.read().strip().split('\n')]
                    total_listener_emotion.extend(listener_emotion)
    for txtfile in speaker_txt_files:
        txt_file_path = os.path.join(*speaker_folder_path,txtfile)
        with open(txt_file_path, 'r') as txt_file:
                    speaker_emotion = [txt_file.read().strip().split('\n')]
                    total_speaker_emotion.extend(speaker_emotion)

listener_dict = count_each_emotion(total_listener_emotion)
speaker_dict = count_each_emotion(total_speaker_emotion)

labels = list(listener_dict.keys())
sizes = list(listener_dict.values())
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, autopct=lambda p: '{:.1f}%\n({:.0f})'.format(p, p * sum(sizes) / 100), startangle=140)
plt.axis('equal')  # 원형으로 보이도록 설정

# 시각화된 파이 차트를 이미지 파일로 저장
plt.savefig('negative_listener_dict.png')

labels = list(speaker_dict.keys())
sizes = list(speaker_dict.values())
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, autopct=lambda p: '{:.1f}%\n({:.0f})'.format(p, p * sum(sizes) / 100), startangle=140)
plt.axis('equal')  # 원형으로 보이도록 설정

# 시각화된 파이 차트를 이미지 파일로 저장
plt.savefig('negative_speaker_dict.png')