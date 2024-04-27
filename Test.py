import cv2
import numpy as np

# Aturan warna
lower_white = np.array([0, 0, 200], dtype=np.uint8)
upper_white = np.array([180, 30, 255], dtype=np.uint8)

lower_gray = np.array([0, 0, 0])
upper_gray = np.array([220, 220, 220])


lower_blue = np.array([0, 0, 112])
upper_blue = np.array([224,255,255])

# Membaca gambar
# image = cv2.imread('./Dataset/Cloud/cloud108.jpg')
image = cv2.imread('./Dataset/RainCloud/RainCloud (104).jpg')

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Konversi gambar ke ruang warna HSV
# mask_white = cv2.inRange(hsv_image, lower_white, upper_white)
mask_gray = cv2.inRange(hsv_image, lower_gray, upper_gray)
mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)

# Gabungkan semua mask menjadi satu
# final_mask = cv2.bitwise_or(mask_white, cv2.bitwise_or(mask_gray, mask_blue))
mask_white = cv2.bitwise_not(mask_blue)

# Aplikasikan mask ke gambar asli
result = cv2.bitwise_and(image, image, mask=mask_white)
# Menampilkan hasil
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()


  # if gray_pixels > white_pixels and gray_pixels > blue_pixels:
  #   # print("test")
  #   print(gray_pixels)
  #   print(blue_pixels)
  #   rgb_values[4:8] = [False, True, False, "Mendung"]
  # if white_pixels > gray_pixels and white_pixels > blue_pixels:
  #   rgb_values[4:8] = [True, False, True, "Cerah"]
  # elif white_pixels > blue_pixels and white_pixels < gray_pixels:
  #   rgb_values[4:8] = [True, False, False, "Cerah"]