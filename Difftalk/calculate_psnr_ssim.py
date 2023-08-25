# import cv2
# from skimage.metrics import peak_signal_noise_ratio, structural_similarity

# def calculate_psnr_ssim(image_path1, image_path2):
#     # 이미지 파일 읽기
#     image1 = cv2.imread(image_path1)
#     image2 = cv2.imread(image_path2)
#     image1 = cv2.resize(image1,(256,256))
#     # print(image1.shape)
#     # print(image2.shape)

#     # PSNR 계산
#     psnr = peak_signal_noise_ratio(image1, image2)

#     # SSIM 계산
#     ssim = structural_similarity(image1, image2, win_size = 3, multichannel=True)

#     return psnr, ssim

# avg_psnr = 0
# avg_ssim = 0
# for i in range(0,2251):
#     # 이미지 파일 경로
#     image_path1 = '/home2/intern4/project/Difftalk/resize_32/resized_image_{}.jpg'.format(i) # original
#     if i <=9:
#         image_path2 = '/home2/intern4/project/Difftalk/result/9_with_high_epoch_20/0000_000{}.jpg'.format(i) # reconstruct
#     else:
#         image_path2 = '/home2/intern4/project/Difftalk/result/9_with_high_epoch_20/0000_00{}.jpg'.format(i) # reconstruct

#     # PSNR과 SSIM 추출
#     psnr, ssim = calculate_psnr_ssim(image_path1, image_path2)
#     avg_psnr += psnr
#     avg_ssim += ssim

#     # 결과 출력
#     print(f"PSNR: {psnr:.2f}")
#     print(f"SSIM: {ssim:.4f}")
# print("[AVG_PSNR]:{}".format(avg_psnr/20))
# print("[AVG_SSIM]:{}".format(avg_ssim/20))


import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

def calculate_psnr(image1, image2):
    mse = np.mean((image1 - image2) ** 2)
    max_pixel_value = 255.0
    psnr = 20 * np.log10(max_pixel_value / np.sqrt(mse))
    return psnr

def calculate_ssim(image1, image2):
    return ssim(image1, image2, win_size = 3, multichannel=True)

def calculate_average_psnr_ssim(folder1, folder2):
    total_psnr = 0
    total_ssim = 0
    num_images = 0

    filenames1 = sorted(os.listdir(folder1))
    filenames2 = sorted(os.listdir(folder2))

    for filename1, filename2 in zip(filenames1, filenames2):
        if filename1.endswith(".jpg") or filename1.endswith(".png"):
            image1 = cv2.imread(os.path.join(folder1, filename1))
            image2 = cv2.imread(os.path.join(folder2, filename2))
            
            if image1 is not None and image2 is not None:
                psnr = calculate_psnr(image1, image2)
                ssim_value = calculate_ssim(image1, image2)
                total_psnr += psnr
                total_ssim += ssim_value
                num_images += 1
    
    if num_images > 0:
        average_psnr = total_psnr / num_images
        average_ssim = total_ssim / num_images
        return average_psnr, average_ssim
    else:
        return None, None

# 폴더 경로 설정
folder1 = '/home2/intern4/project/Difftalk/resize_32'
folder2 = '/home2/intern4/project/Difftalk/result/11_without_high_epoch_20'

# PSNR과 SSIM의 평균 계산
average_psnr, average_ssim = calculate_average_psnr_ssim(folder1, folder2)

if average_psnr is not None and average_ssim is not None:
    print(f"Average PSNR: {average_psnr:.2f}")
    print(f"Average SSIM: {average_ssim:.4f}")
else:
    print("No images found or error occurred.")



