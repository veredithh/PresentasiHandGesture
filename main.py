# Import Library
import os
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

import sys

# Variabel Ukuran Camera
width, height = 1280, 720

# Variabel Folder Presentasi
folderPath = 'Presentation'

cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)


pathImages = sorted(os.listdir(folderPath), key=len)
imgNumber = 0

# Variabel Ukuran Webcam pada Slide
hs, ws = int(150 * 1.5), int(213 * 1.5)

# Variabel Pembatas Gesture
gestureThreshold = 300

# Variabel Delay Gesture
buttonPressed = False
buttonCounter = 0
buttonDelay = 30

# Variabel untuk Menggambar pada Slide
annotations = [[]]
annotationNumber = -1
annotationStart = False

# Variabel Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:

    success, img = cap.read()
    img = cv2.flip(img, 1)
    pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)
    hands, img = detector.findHands(img)

    # Garis Pembatas Gesture
    cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (102, 255, 102), 10)

    if hands and buttonPressed is False:
        hand = hands[0]
        fingers = detector.fingersUp(hand)

        # Garis Tengah Tangan
        cx, cy = hand['center']

        # Tracking Jari Telunjuk
        lmList = hand['lmList']

        xVal = int(np.interp(lmList[8][0], [width // 2, w], [0, width]))
        yVal = int(np.interp(lmList[8][1], [100, height - 100], [0, height]))
        indexFinger = xVal, yVal

        if cy <= gestureThreshold:

            # Gesture 1 - Ke Slide Sebelumnya
            if fingers == [1, 0, 0, 0, 0]:
                print('Kembali')

                if imgNumber > 0:
                    buttonPressed = True
                    annotations = [[]]
                    annotationNumber = -1
                    annotationStart = False
                    imgNumber -= 1

            # Gesture 2 - Ke Slide Selanjutnya
            if fingers == [0, 1, 1, 0, 0]:
                print('Lanjut')

                if imgNumber < len(pathImages) - 1:
                    buttonPressed = True
                    annotations = [[]]
                    annotationNumber = -1
                    annotationStart = False
                    imgNumber += 1

            # Gesture 6 - Exit
            if fingers == [0, 1, 0, 0, 1]:
                sys.exit('User keluar dari aplikasi')

        # Gesture 3 - Pointer
        if fingers == [0, 1, 0, 0, 0]:
            print('Pointer')

            cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)

        # Gesture 4 - Menggambar
        if fingers == [0, 1, 1, 1, 0]:
            print('Menggambar')

            if annotationStart is False:
                annotationStart = True
                annotationNumber += 1
                annotations.append([])
            cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)
            annotations[annotationNumber].append(indexFinger)

        else:
            annotationStart = False

        # Gesture 5 - Menghapus Gambar
        if fingers == [0, 1, 1, 1, 1]:
            print('Hapus Gambar')

            if annotations:
                annotations.pop(-1)
                annotationNumber -= 1
                buttonPressed = True

    # Delay Gesture
    if buttonPressed:
        buttonCounter += 1
        if buttonCounter > buttonDelay:
            buttonCounter = 0
            buttonPressed = False

    # Pembeda Garis
    for i in range(len(annotations)):
        for j in range(len(annotations[i])):
            if j != 0:
                cv2.line(imgCurrent, annotations[i][j - 1], annotations[i][j], (0, 0, 200),12)

    # Webcam di Dalam Slide
    imgSmall = cv2.resize(img, (ws, hs))
    h, w, _ = imgCurrent.shape
    imgCurrent[0:hs, w - ws:w] = imgSmall

    cv2.imshow("Image", img)
    cv2.imshow("Slides", imgCurrent)

    # Break Program
    key = cv2.waitKey(1)
    if key == ord('q'):
        break