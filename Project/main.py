import cv2
import numpy as np
import utlis
import os

# ---------- SETUP ----------
os.makedirs("Scanned", exist_ok=True)     # Create Scanned folder if not exist
webCamFeed = True                         # True = Webcam, False = Image
pathImage = "1.jpg"                       # Path to sample image
cap = cv2.VideoCapture(0)
cap.set(10, 160)                          # Set brightness
heightImg = 640
widthImg = 480

print("📸 Document Scanner Running...")
print("Press 'S' to SAVE scan | 'Q' to Quit")

utlis.initializeTrackbars()               # Create Trackbars window
count = 0

# ---------- MAIN LOOP ----------
while True:

    # READ FRAME OR IMAGE
    if webCamFeed:
        success, img = cap.read()
        if not success:
            print("❌ Cannot access webcam.")
            break
    else:
        img = cv2.imread(pathImage)

    img = cv2.resize(img, (widthImg, heightImg))
    imgBlank = np.zeros((heightImg, widthImg, 3), np.uint8)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)

    thres = utlis.valTrackbars()
    imgThreshold = cv2.Canny(imgBlur, thres[0], thres[1])
    kernel = np.ones((5, 5))
    imgDial = cv2.dilate(imgThreshold, kernel, iterations=2)
    imgThreshold = cv2.erode(imgDial, kernel, iterations=1)

    # FIND CONTOURS
    imgContours = img.copy()
    imgBigContour = img.copy()
    contours, _ = cv2.findContours(imgThreshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 3)

    biggest, maxArea = utlis.biggestContour(contours)
    imgWarpColored = None  # Initialize variable

    if biggest.size != 0:
        biggest = utlis.reorder(biggest)
        cv2.drawContours(imgBigContour, biggest, -1, (0, 255, 0), 10)
        imgBigContour = utlis.drawRectangle(imgBigContour, biggest, 2)

        pts1 = np.float32(biggest)
        pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg))

        # REMOVE EDGES AND ENHANCE
        imgWarpColored = imgWarpColored[20:imgWarpColored.shape[0]-20,
                                        20:imgWarpColored.shape[1]-20]
        imgWarpColored = cv2.resize(imgWarpColored, (widthImg, heightImg))

        imgWarpGray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
        imgAdaptiveThre = cv2.adaptiveThreshold(imgWarpGray, 255, 1, 1, 7, 2)
        imgAdaptiveThre = cv2.bitwise_not(imgAdaptiveThre)
        imgAdaptiveThre = cv2.medianBlur(imgAdaptiveThre, 3)

        imageArray = ([img, imgGray, imgThreshold, imgContours],
                      [imgBigContour, imgWarpColored, imgWarpGray, imgAdaptiveThre])
    else:
        imageArray = ([img, imgGray, imgThreshold, imgContours],
                      [imgBlank, imgBlank, imgBlank, imgBlank])

    labels = [["Original", "Gray", "Threshold", "Contours"],
              ["Biggest Contour", "Warp Perspective", "Warp Gray", "Adaptive Threshold"]]

    stackedImage = utlis.stackImages(imageArray, 0.75, labels)
    cv2.imshow("Result", stackedImage)

    key = cv2.waitKey(1) & 0xFF

    # --- SAVE WHEN 'S' IS PRESSED ---
    if key == ord('s'):
        if imgWarpColored is not None:
            filename = f"Scanned/myImage{count}.jpg"
            cv2.imwrite(filename, imgWarpColored)
            print(f"✅ Scan saved successfully as {filename}")
            count += 1
        else:
            print("⚠️ No document detected! Try adjusting the paper position.")

    # --- QUIT WHEN 'Q' IS PRESSED ---
    if key == ord('q'):
        print("👋 Exiting scanner...")
        break

cap.release()
cv2.destroyAllWindows()
