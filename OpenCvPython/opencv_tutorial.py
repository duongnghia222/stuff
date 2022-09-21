import cv2
import numpy as np
print("hi")
# # show img
# img = cv2.imread("resources/hoa_hau_khanh_van3.png")
# cv2.imshow("Output", img)
# cv2.waitKey(0)


# # show video
# cap = cv2.VideoCapture("resources/bai du thi.mp4")
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# # webcam
# cap = cv2.VideoCapture(0)
# cap.set(3, 720) # width
# cap.set(4, 1080) # height
# cap.set(10, 100) # brightness
# while True:
#     success, img = cap.read()
#     cv2.imshow("WebCam", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'): # press q to quit
#         break

# # change color image
# img = cv2.imread("resources/hoa_hau_khanh_van3.png")
# kernel = np.ones((5,5), np.uint8)
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(img, (7,7), 0)
# imgCanny = cv2.Canny(img, 100, 100)
# imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
# imgEroded = cv2.erode(imgDilation, kernel, iterations=1)
# cv2.imshow("Gray Image", imgGray)
# cv2.imshow("Blur Image", imgBlur)
# cv2.imshow("Canny image", imgCanny)
# cv2.imshow("Dilation Image", imgDilation)
# cv2.imshow("Eroded Image", imgEroded)
#
# cv2.waitKey(0)


# # crop image
# img = cv2.imread("resources/messi-neymar-mbappe-3956.png")
# print("Size: ", img.shape) # (height, width, nums of bgr)
# imgResized = cv2.resize(img, (800, 500)) # (width, height)
#
# imgCropped = imgResized[100:300,100:200] # [height, width]
# cv2.imshow("Output", img)
# cv2.imshow("Resized img", imgResized)
# cv2.imshow("Cropped img", imgCropped)
#
# cv2.waitKey(0)

# # Draw
# img = np.zeros((512,512,3), np.uint8)
# print(img.shape)
# img[100:200] =  0,255,0
# img[0:100] =  155,0,0
# cv2.line(img, (0,0), (img.shape[0],img.shape[1]), (0,0,255), 3)
# cv2.rectangle(img, (5,5), (150, 130), (0,11, 123), cv2.FILLED)
# cv2.circle(img, (256, 256), 40, (0,1, 235), cv2.FILLED)
# cv2.putText(img, "Hello World !", (300,300), cv2.FONT_HERSHEY_PLAIN, 2, (1,3,134), 1)
# cv2.imshow("Output", img)
# cv2.waitKey(0)


# # get warpPerspective
# img = cv2.imread("resources/playing_card.png")
# height, width = 350,250
# pts1 = np.float32([[206,361],[345,261],[357,583],[504,488]])
# pts2 = np.float32([[0,0],[width, 0],[0, height],[width, height]])
# matrix = cv2.getPerspectiveTransform(pts1, pts2)
# imgOut = cv2.warpPerspective(img, matrix, (width,height))
# cv2.imshow("Cards", img)
# cv2.imshow("Out", imgOut)
# cv2.waitKey(0)


# # img arrange
# img = cv2.imread("resources/hoa_hau_khanh_van3.png")
# imgHori = np.hstack((img,img))
# imgVert = np.vstack((img,img))
# cv2.imshow("Horizontal ", imgHori)
# cv2.imshow("Vertical ", imgVert)
# cv2.waitKey(0)


# # img detection
#
# def empty(x):
#     pass
#
# path = 'resources/messi-neymar-mbappe-3956.png'
# cv2.namedWindow("trackBars")
# cv2.resizeWindow("trackBars", 640, 240)
# cv2.createTrackbar("Hue Min", "trackBars", 0, 179, empty)
# cv2.createTrackbar("Hue Max", "trackBars", 26, 179, empty)
# cv2.createTrackbar("Sat Min", "trackBars", 57, 255, empty)
# cv2.createTrackbar("Sat Max", "trackBars", 285, 255, empty)
# cv2.createTrackbar("Val Min", "trackBars", 67, 255, empty)
# cv2.createTrackbar("Val Max", "trackBars", 255, 255, empty)
# while True:
#     img = cv2.imread(path)
#     imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     h_min = cv2.getTrackbarPos("Hue Min", "trackBars")
#     h_max = cv2.getTrackbarPos("Hue Max", "trackBars")
#     s_min = cv2.getTrackbarPos("Sat Min", "trackBars")
#     s_max = cv2.getTrackbarPos("Sat Max", "trackBars")
#     v_min = cv2.getTrackbarPos("Val Min", "trackBars")
#     v_max = cv2.getTrackbarPos("Val Max", "trackBars")
#     print(h_min,h_max,s_min,s_max,v_min,v_max)
#     lower = np.array([h_min,s_min,v_min])
#     upper = np.array([h_max,s_max,v_max])
#     mask = cv2.inRange(imgHSV,lower,upper)
#     imgRes = cv2.bitwise_and(img, img, mask=mask)
#     cv2.imshow("Original", img)
#     #cv2.imshow("HSV", imgHSV)
#     cv2.imshow("Mask", mask)
#     cv2.imshow("Result", imgRes)
#     cv2.waitKey(1)



# shape detection
def getContours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for c in contours:
        area = cv2.contourArea(c)
        print(area)

path = "resources/shape.png"
img = cv2.imread(path)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)
cv2.imshow("Img", img)
cv2.imshow("Blur Img", imgBlur)
cv2.imshow("Gray Img", imgGray)
cv2.imshow("Canny Img", imgCanny)

cv2.waitKey(0)