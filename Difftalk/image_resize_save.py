from PIL import Image

def resize_and_save_image(input_path, output_path, new_size):
    try:
        # 이미지 열기
        image = Image.open(input_path)

        # 이미지 리사이즈
        resized_image = image.resize(new_size)

        # 리사이즈한 이미지 저장
        resized_image.save(output_path)
        print(f"Image has been resized and saved to {output_path}")

    except Exception as e:
        print(f"Error: {e}")

# 사용 예시
for i in range(0,2251):
    input_image_path = "/home2/intern4/project/Difftalk/data/preprocessing/images/32/32_{}.jpg".format(i)  # 입력 이미지 파일 경로
    output_image_path = "./resize_32/resized_image_{}.jpg".format(i)  # 저장할 리사이즈된 이미지 파일 경로
    new_size = (256, 256)  # 새로운 이미지 크기 (가로 256, 세로 256)

    resize_and_save_image(input_image_path, output_image_path, new_size)
