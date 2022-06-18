from cv2 import cv2
import numpy as np

# This piece of code is to access the camera module
# cap = cv2.VideoCapture(0)
# while True:
#     # Capture the video frame
#     # by frame
#     success, frame = cap.read()
#     gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     # Display the resulting frame
#     cv2.imshow("frame", gray_frame)
#     # the 'q' button is set as the
#     # quitting button you may use any
#     # desired button of your choice
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
# ------------------------------------------------------------------------------------------------------------

# Threshold is a technique where it is used to separate the foreground and background areas in the image.

# img = cv2.imread("E:/OpenCV/OpenCV/pexels-pixabay-60597.jpg")
# # Resizing image to make it smaller
# img = cv2.resize(img, (320, 240))
# # Converting color image to grayscale
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # Applying threshold to the gray image
# ret, thresh1 = cv2.threshold(gray_img, 125, 255, cv2.THRESH_BINARY)
# ret, thresh2 = cv2.threshold(gray_img, 125, 255, cv2.THRESH_BINARY_INV)
# ret, thresh3 = cv2.threshold(gray_img, 125, 255, cv2.THRESH_TRUNC)
# ret, thresh4 = cv2.threshold(gray_img, 125, 255, cv2.THRESH_TOZERO)
# ret, thresh5 = cv2.threshold(gray_img, 125, 255, cv2.THRESH_TOZERO_INV)
# # Displaying resultant images
# cv2.imshow("Original Image", img)
# cv2.imshow("Binary Threshold", thresh1)
# cv2.imshow("Binary Threshold Inverted", thresh2)
# cv2.imshow("Truncated Threshold", thresh3)
# cv2.imshow("Set to 0", thresh4)
# cv2.imshow("Set to 0 Inverted", thresh5)
# # Wait for user to press key for exit
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# -------------------------------------------------------------------------------------------------------------
# Noise is the variation in the pixels of the image. We overcome this by changing this pixel value with
# the average of nearby pixel by applying filters on the image. We need find the best kernel size based on
# our use case. different kinds of blurring techniques are:
# mean blur
# median blur
# guassian blur
# bilateral blur

# img = cv2.imread("noise_image.jpg")
# # Resizing image to make it smaller
# img = cv2.resize(img, (300, 280))
# # Applying different blur functions with 7*7 filter
# img_0 = cv2.blur(img, ksize=(7, 7))
# img_1 = cv2.GaussianBlur(img, (7, 7), 0)
# img_2 = cv2.medianBlur(img, 7)
# img_3 = cv2.bilateralFilter(img, 7, 75, 75)
# # Displaying resultant images
# cv2.imshow("Original", img)
# cv2.imshow("Blur", img_0)
# cv2.imshow("Gaussian Blur", img_1)
# cv2.imshow("Median Blur", img_2)
# cv2.imshow("Bilateral Filter", img_3)
# # Waits for a user to press key for exit
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ----------------------------------------------------------------------------------------------------------
# Canny Edge Detection Algorithm on webcam
# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)
# cap.set(10, 100)
# kernel = np.ones((3, 3), dtype=np.uint8)
# while True:
#     success, img = cap.read()
#     gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     canny_img = cv2.Canny(gray_img, 100, 100)
#     dialate_img = cv2.dilate(canny_img, kernel)
#     imgerode = cv2.erode(dialate_img, kernel)
#     cv2.imshow("edge detection", imgerode)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
# ------------------------------------------------------------------------------------------------------------

# Resize and crop function
# img = cv2.imread("E:/OpenCV/OpenCV/pexels-pixabay-60597.jpg")
# img_resize = cv2.resize(img, (1000, 1500))
# print(img.shape)
# print(img_resize.shape)
# # for cropping we use matrix slicing
# cv2.imshow("cropped_img", img[0:200, 200:600])
# cv2.imshow("image", img)
# cv2.imshow("resize", img_resize)
# cv2.waitKey(0)

# ---------------------------------------------------------------------------------------------------------

# drawing shapes and text on images
# we draw a rectangle, line, circle on the image. we can even write text using cv2.puttext on the image.
# img = np.zeros((512, 512, 3), dtype=np.uint8)
# # img[:] = 0, 0, 255
# # drawing line on the image
# img_line = cv2.line(img, (300, 0), (300, 300), (0, 0, 255))
# cv2.imshow("image", img_line)
# cv2.waitKey(0)

# -------------------------------------------------------------------------------------------------------
# warp perspective
img = cv2.imread("playing_cards.jpg")
width, height = 250, 350
pts1 = np.float32([[516, 140], [936, 299], [311, 694], [694, 855]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
result_img = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("warp perspective image", result_img)
cv2.waitKey(0)
