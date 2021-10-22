import cv2
import time
import os
import HandTrackingModule as htm
import random
import simpleaudio as sa
import cvzone

filename = 'pop.wav'
wave_obj = sa.WaveObject.from_wave_file(filename)

def HPVocales2():
    wCam, hCam = 640, 480

    cap = cv2.VideoCapture(1)
    cap.set(3, wCam)
    cap.set(4, hCam)

    folderPath = "FingerImages"
    myList = os.listdir(folderPath)
    print(myList)
    overlayList = []
    for imPath in myList:
        image = cv2.imread(f'{folderPath}/{imPath}')
        # print(f'{folderPath}/{imPath}')
        overlayList.append(image)

    print(len(overlayList))
    pTime = 0

    detector = htm.handDetector(detectionCon=0.75, maxHands=1)

    tipIds = [4, 8, 12, 16, 20]

    totalFingers = 0

    aux = -1
    permite = True

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            if (lmList[8][1] > 0 and lmList[8][1] < 500):
                aux = 1

            if (totalFingers != 2):
                permite = True

            if (totalFingers == 2):
                if (permite == True):
                    if (aux == 1):
                        wave_obj.play()
                        HPVocales()
                    permite = False

            totalFingers = fingers.count(1)

        imagen = cv2.imread('vocales2.png', cv2.IMREAD_UNCHANGED)

        cv2.rectangle(img, (43, 30), (285, 70), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Atras', (98, 65), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        imgResult = cvzone.overlayPNG(img, imagen, [60, 110])

        cv2.imshow("Image", imgResult)
        cv2.waitKey(1)

def HPVocales():
    wCam, hCam = 640, 480

    cap = cv2.VideoCapture(1)
    cap.set(3, wCam)
    cap.set(4, hCam)

    folderPath = "FingerImages"
    myList = os.listdir(folderPath)
    print(myList)
    overlayList = []
    for imPath in myList:
        image = cv2.imread(f'{folderPath}/{imPath}')
        # print(f'{folderPath}/{imPath}')
        overlayList.append(image)

    print(len(overlayList))
    pTime = 0

    detector = htm.handDetector(detectionCon=0.75, maxHands=1)

    tipIds = [4, 8, 12, 16, 20]

    totalFingers = 0

    aux = -1
    permite = True

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            if (lmList[8][1] > 0 and lmList[8][1] < 500):
                aux = 1
            if (lmList[8][1] > 500 and lmList[8][1] < 999):
                aux = 2

            if (totalFingers != 2):
                permite = True

            if (totalFingers == 2):
                if (permite == True):
                    if (aux == 1):
                        wave_obj.play()
                        VocalesDesorden()
                    if (aux == 2):
                        wave_obj.play()
                        HPVocales2()
                    permite = False

            totalFingers = fingers.count(1)

        imagen = cv2.imread('vocales1.png', cv2.IMREAD_UNCHANGED)

        cv2.rectangle(img, (43, 30), (285, 70), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Atras', (98, 65), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (673, 30), (915, 70), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Siguiente', (680, 65), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        imgResult = cvzone.overlayPNG(img, imagen, [60, 110])

        cv2.imshow("Image", imgResult)
        cv2.waitKey(1)

def HPDedos2():
    wCam, hCam = 640, 480

    cap = cv2.VideoCapture(1)
    cap.set(3, wCam)
    cap.set(4, hCam)

    folderPath = "FingerImages"
    myList = os.listdir(folderPath)
    print(myList)
    overlayList = []
    for imPath in myList:
        image = cv2.imread(f'{folderPath}/{imPath}')
        # print(f'{folderPath}/{imPath}')
        overlayList.append(image)

    print(len(overlayList))
    pTime = 0

    detector = htm.handDetector(detectionCon=0.75, maxHands=1)

    tipIds = [4, 8, 12, 16, 20]

    totalFingers = 0

    aux = -1
    permite = True

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            if (lmList[8][1] > 0 and lmList[8][1] < 500):
                aux = 1

            if (totalFingers != 2):
                permite = True

            if (totalFingers == 2):
                if (permite == True):
                    if (aux == 1):
                        wave_obj.play()
                        HPDedos()
                    permite = False

            totalFingers = fingers.count(1)

        imagen = cv2.imread('dedos2.png', cv2.IMREAD_UNCHANGED)

        cv2.rectangle(img, (43, 30), (285, 70), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Atras', (98, 65), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        imgResult = cvzone.overlayPNG(img, imagen, [70, 100])

        cv2.imshow("Image", imgResult)
        cv2.waitKey(1)

def HPDedos():
    wCam, hCam = 640, 480

    cap = cv2.VideoCapture(1)
    cap.set(3, wCam)
    cap.set(4, hCam)

    folderPath = "FingerImages"
    myList = os.listdir(folderPath)
    print(myList)
    overlayList = []
    for imPath in myList:
        image = cv2.imread(f'{folderPath}/{imPath}')
        # print(f'{folderPath}/{imPath}')
        overlayList.append(image)

    print(len(overlayList))
    pTime = 0

    detector = htm.handDetector(detectionCon=0.75, maxHands=1)

    tipIds = [4, 8, 12, 16, 20]

    totalFingers = 0

    aux = -1
    permite = True

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            if (lmList[8][1] > 0 and lmList[8][1] < 500):
                aux = 1
            if (lmList[8][1] > 500 and lmList[8][1] < 999):
                aux = 2

            if (totalFingers != 2):
                permite = True

            if (totalFingers == 2):
                if (permite == True):
                    if (aux == 1):
                        wave_obj.play()
                        SumaDedos()
                    if (aux == 2):
                        wave_obj.play()
                        HPDedos2()
                    permite = False

            totalFingers = fingers.count(1)

        imagen = cv2.imread('dedos1.png', cv2.IMREAD_UNCHANGED)

        cv2.rectangle(img, (43, 30), (285, 70), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Atras', (98, 65), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (673, 30), (915, 70), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Siguiente', (680, 65), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        imgResult = cvzone.overlayPNG(img, imagen, [70, 100])

        cv2.imshow("Image", imgResult)
        cv2.waitKey(1)

def SumaDedos():
    wCam, hCam = 640, 480

    cap = cv2.VideoCapture(1)
    cap.set(3, wCam)
    cap.set(4, hCam)

    folderPath = "FingerImages"
    myList = os.listdir(folderPath)
    print(myList)
    overlayList = []
    for imPath in myList:
        image = cv2.imread(f'{folderPath}/{imPath}')
        # print(f'{folderPath}/{imPath}')
        overlayList.append(image)

    print(len(overlayList))
    pTime = 0

    detector = htm.handDetector(detectionCon=0.75, maxHands=1)

    tipIds = [4, 8, 12, 16, 20]

    totalFingers = 0

    aux = -1
    permite = True

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            if (lmList[8][2] > 300 and lmList[8][2] < 340):
                aux = 1

            if (lmList[8][2] > 400 and lmList[8][2] < 440):
                aux = 2

            if (lmList[8][2] > 500 and lmList[8][2] < 540):
                aux = 3

            if (totalFingers != 2):
                permite = True

            if (totalFingers == 2):
                if (permite == True):
                    if (aux == 1):
                        wave_obj.play()
                        juegoDEDOS()
                    if (aux == 2):
                        wave_obj.play()
                        HPDedos()
                    if (aux == 3):
                        wave_obj.play()
                        menu()
                    permite = False

            totalFingers = fingers.count(1)

        cv2.putText(img, f'SUMA DE DEDOS', (235, 150), cv2.FONT_HERSHEY_PLAIN, 4, (219, 152, 52), 6)

        cv2.rectangle(img, (350, 300), (650, 340), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Jugar', (440, 335), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (330, 400), (670, 440), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Como Jugar', (350, 435), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (350, 500), (650, 540), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Menu', (445, 535), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

def VocalesDesorden():
    wCam, hCam = 640, 480

    cap = cv2.VideoCapture(1)
    cap.set(3, wCam)
    cap.set(4, hCam)

    folderPath = "FingerImages"
    myList = os.listdir(folderPath)
    print(myList)
    overlayList = []
    for imPath in myList:
        image = cv2.imread(f'{folderPath}/{imPath}')
        # print(f'{folderPath}/{imPath}')
        overlayList.append(image)

    print(len(overlayList))
    pTime = 0

    detector = htm.handDetector(detectionCon=0.75, maxHands=1)

    tipIds = [4, 8, 12, 16, 20]

    totalFingers = 0

    aux = -1
    permite = True

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            if (lmList[8][2] > 300 and lmList[8][2] < 340):
                aux = 1

            if (lmList[8][2] > 400 and lmList[8][2] < 440):
                aux = 2

            if (lmList[8][2] > 500 and lmList[8][2] < 540):
                aux = 3

            if (totalFingers != 2):
                permite = True

            if (totalFingers == 2):
                if (permite == True):
                    if (aux == 1):
                        wave_obj.play()
                        juegoVOCALES()
                    if (aux == 2):
                        wave_obj.play()
                        HPVocales()
                    if (aux == 3):
                        wave_obj.play()
                        menu()
                    permite = False

            totalFingers = fingers.count(1)

        cv2.putText(img, f'VOCALES EN DESORDEN', (100, 150), cv2.FONT_HERSHEY_PLAIN, 4, (219, 152, 52), 6)

        cv2.rectangle(img, (350, 300), (650, 340), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Jugar', (440, 335), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (330, 400), (670, 440), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Como Jugar', (350, 435), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (350, 500), (650, 540), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Menu', (445, 535), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

def iniciar():
    wCam, hCam = 640, 480

    cap = cv2.VideoCapture(1)
    cap.set(3, wCam)
    cap.set(4, hCam)

    folderPath = "FingerImages"
    myList = os.listdir(folderPath)
    print(myList)
    overlayList = []
    for imPath in myList:
        image = cv2.imread(f'{folderPath}/{imPath}')
        # print(f'{folderPath}/{imPath}')
        overlayList.append(image)

    print(len(overlayList))
    pTime = 0

    detector = htm.handDetector(detectionCon=0.75, maxHands=1)

    tipIds = [4, 8, 12, 16, 20]

    totalFingers = 0

    aux = -1
    permite = True

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            if (lmList[8][2] > 300 and lmList[8][2] < 340):
                aux = 1

            if (lmList[8][2] > 400 and lmList[8][2] < 440):
                aux = 2

            if (lmList[8][2] > 500 and lmList[8][2] < 540):
                aux = 3

            if (totalFingers != 2):
                permite = True

            if (totalFingers == 2):
                if (permite == True):
                    if (aux == 1):
                        wave_obj.play()
                        SumaDedos()
                    if (aux == 2):
                        wave_obj.play()
                        VocalesDesorden()
                    if (aux == 3):
                        wave_obj.play()
                        menu()
                    permite = False

            totalFingers = fingers.count(1)

        cv2.putText(img, f'REMI', (285, 180), cv2.FONT_HERSHEY_PLAIN, 12, (219, 152, 52), 25)

        cv2.rectangle(img, (280, 300), (720, 340), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Suma de Dedos', (305, 335), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (230, 400), (770, 440), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Silabas en Desorden', (250, 435), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (350, 500), (650, 540), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Atras', (440, 535), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

def creditos():
    wCam, hCam = 640, 480

    cap = cv2.VideoCapture(1)
    cap.set(3, wCam)
    cap.set(4, hCam)

    folderPath = "FingerImages"
    myList = os.listdir(folderPath)
    print(myList)
    overlayList = []
    for imPath in myList:
        image = cv2.imread(f'{folderPath}/{imPath}')
        # print(f'{folderPath}/{imPath}')
        overlayList.append(image)

    print(len(overlayList))
    pTime = 0

    detector = htm.handDetector(detectionCon=0.75, maxHands=1)

    tipIds = [4, 8, 12, 16, 20]

    totalFingers = 0

    aux = -1
    permite = True

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            if (lmList[8][2] > 500 and lmList[8][2] < 540):
                aux = 1

            if (totalFingers != 2):
                permite = True

            if (totalFingers == 2):
                if (permite == True):
                    if (aux == 1):
                        wave_obj.play()
                        menu()
                    permite = False

            totalFingers = fingers.count(1)

        cv2.putText(img, f'REMI', (285, 180), cv2.FONT_HERSHEY_PLAIN, 12, (219, 152, 52), 25)

        cv2.putText(img, f'Oscar Mendoza', (300, 280), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)
        cv2.putText(img, f'Patrick Marquez', (285, 330), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)
        cv2.putText(img, f'Inigo Diez Canseco', (245, 380), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (350, 500), (650, 540), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Atras', (440, 535), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

def menu():
    wCam, hCam = 640, 480

    cap = cv2.VideoCapture(1)
    cap.set(3, wCam)
    cap.set(4, hCam)

    folderPath = "FingerImages"
    myList = os.listdir(folderPath)
    print(myList)
    overlayList = []
    for imPath in myList:
        image = cv2.imread(f'{folderPath}/{imPath}')
        # print(f'{folderPath}/{imPath}')
        overlayList.append(image)

    print(len(overlayList))
    pTime = 0

    detector = htm.handDetector(detectionCon=0.75, maxHands=1)

    tipIds = [4, 8, 12, 16, 20]

    totalFingers = 0

    aux = -1
    permite = True

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            if (lmList[8][2] > 300 and lmList[8][2] < 340):
                aux = 1

            if (lmList[8][2] > 400 and lmList[8][2] < 440):
                aux = 2

            if (lmList[8][2] > 500 and lmList[8][2] < 540):
                aux = 3

            if (totalFingers != 2):
                permite = True

            if (totalFingers == 2):
                if (permite == True):
                    if(aux == 1):
                        wave_obj.play()
                        iniciar()
                    if(aux == 2):
                        wave_obj.play()
                        creditos()
                    if(aux == 3):
                        wave_obj.play()
                        exit(1)
                    permite = False

            totalFingers = fingers.count(1)

        cv2.putText(img, f'REMI', (285, 180), cv2.FONT_HERSHEY_PLAIN, 12, (219, 152, 52), 25)

        cv2.rectangle(img, (350, 300), (650, 340), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Iniciar', (435, 335), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (350, 400), (650, 440), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Creditos', (400, 435), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.rectangle(img, (350, 500), (650, 540), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Salir', (440, 535), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

def juegoVOCALES():
    wCam, hCam = 640, 480

    cap = cv2.VideoCapture(1)
    cap.set(3, wCam)
    cap.set(4, hCam)

    folderPath = "FingerImages"
    myList = os.listdir(folderPath)
    print(myList)
    overlayList = []
    for imPath in myList:
        image = cv2.imread(f'{folderPath}/{imPath}')
        # print(f'{folderPath}/{imPath}')
        overlayList.append(image)

    print(len(overlayList))
    pTime = 0

    detector = htm.handDetector(detectionCon=0.75, maxHands=1)

    tipIds = [4, 8, 12, 16, 20]

    arrPalabras = ['CASA', 'SAPO', 'CAMA', 'PATO', 'PECERA', 'GORILA']
    arrSilabas = ['CA', 'SA', 'PO', 'MA', 'PA', 'TO', 'PE', 'CE', 'RA', 'GO', 'RI', 'LA', 'SI', 'RO', 'CO']
    arrIndex = [[1, 13, 7, 0], [2, 8, 1, 10], [14, 3, 0, 11], [5, 4, 9, 6], [7, 12, 8, 6], [11, 10, 6, 9]]

    aleatorio = random.randint(0, 5)
    palabraObjetivo = arrPalabras[aleatorio]

    palabra = ''

    aux = ''
    permite = True

    bool = 0

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            totalFingers = fingers.count(1)

            if (lmList[8][2] == 180 or lmList[8][2] == 175 or lmList[8][2] == 170 or lmList[8][2] == 185 or lmList[8][
                2] == 190):
                aux = arrSilabas[arrIndex[aleatorio][0]]

            if (lmList[8][2] == 280 or lmList[8][2] == 275 or lmList[8][2] == 270 or lmList[8][2] == 285 or lmList[8][
                2] == 290):
                aux = arrSilabas[arrIndex[aleatorio][1]]

            if (lmList[8][2] == 380 or lmList[8][2] == 375 or lmList[8][2] == 370 or lmList[8][2] == 385 or lmList[8][
                2] == 390):
                aux = arrSilabas[arrIndex[aleatorio][2]]

            if (lmList[8][2] == 480 or lmList[8][2] == 475 or lmList[8][2] == 470 or lmList[8][2] == 485 or lmList[8][
                2] == 490):
                aux = arrSilabas[arrIndex[aleatorio][3]]

            if (lmList[8][2] > 10 and lmList[8][2] < 60 and totalFingers == 2):
                wave_obj.play()
                VocalesDesorden()

            # print(lmList[8])

            # print(fingers)

            if (totalFingers != 0 and totalFingers != 2):
                permite = True

            if (totalFingers == 2):
                if (permite == True):
                    palabra += aux
                    permite = False

            if (palabraObjetivo == palabra):
                cv2.putText(img, f'BIEN HECHO!', (300, 350), cv2.FONT_HERSHEY_PLAIN, 5, (45, 200, 235), 5)

            if (totalFingers == 0):
                if (permite == True):
                    palabra = palabra[:-2]
                    permite = False

            if (totalFingers == 5):
                palabra = ''
                aleatorio = random.randint(0, 5)
                palabraObjetivo = arrPalabras[aleatorio]

        # h, w, c = overlayList[totalFingers - 1].shape
        # img[0:h, 0:w] = overlayList[totalFingers - 1]

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        # cv2.putText(img, f'FPS: {int(fps)}', (750, 675), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.putText(img, f'OBJETIVO: {str(palabraObjetivo)}', (200, 100), cv2.FONT_HERSHEY_PLAIN, 4, (84, 153, 34), 6)
        cv2.putText(img, f'{str(arrSilabas[arrIndex[aleatorio][0]])}', (70, 200), cv2.FONT_HERSHEY_PLAIN, 4,
                    (18, 156, 243), 4)
        cv2.putText(img, f'{str(arrSilabas[arrIndex[aleatorio][1]])}', (70, 300), cv2.FONT_HERSHEY_PLAIN, 4,
                    (18, 156, 243), 4)
        cv2.putText(img, f'{str(arrSilabas[arrIndex[aleatorio][2]])}', (70, 400), cv2.FONT_HERSHEY_PLAIN, 4,
                    (18, 156, 243), 4)
        cv2.putText(img, f'{str(arrSilabas[arrIndex[aleatorio][3]])}', (70, 500), cv2.FONT_HERSHEY_PLAIN, 4,
                    (18, 156, 243), 4)
        cv2.putText(img, f'{str(palabra)}', (340, 600), cv2.FONT_HERSHEY_PLAIN, 5, (15, 196, 241), 5)

        cv2.rectangle(img, (800, 10), (950, 60), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Salir', (823, 50), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

def juegoDEDOS():
    wCam, hCam = 640, 480

    cap = cv2.VideoCapture(1)
    cap.set(3, wCam)
    cap.set(4, hCam)

    folderPath = "FingerImages"
    myList = os.listdir(folderPath)
    print(myList)
    overlayList = []
    for imPath in myList:
        image = cv2.imread(f'{folderPath}/{imPath}')
        # print(f'{folderPath}/{imPath}')
        overlayList.append(image)

    print(len(overlayList))
    pTime = 0

    detector = htm.handDetector(detectionCon=0.75, maxHands=1)

    tipIds = [4, 8, 12, 16, 20]

    last_value = 0
    temp_last = 0

    suma_obj = random.randint(1, 5)

    totalFingers = 0
    bool = 0
    permite = False

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # print(fingers)
            totalFingers = fingers.count(1)

            if totalFingers == 0:
                last_value += temp_last
            temp_last = totalFingers

            if (lmList[8][2] > 10 and lmList[8][2] < 60 and totalFingers == 2):
                wave_obj.play()
                SumaDedos()

        if suma_obj == last_value:
            cv2.putText(img, f'BIEN HECHO!', (300, 400), cv2.FONT_HERSHEY_PLAIN, 5, (45, 200, 235), 5)

        if suma_obj < last_value:
            cv2.putText(img, f'UPS! TE ESTAS PASANDO', (240, 400), cv2.FONT_HERSHEY_PLAIN, 3, (6, 111, 229), 3)

        print('Valor Acumulado: ', last_value)
        print('Valor Actual: ', totalFingers)

        h, w, c = overlayList[totalFingers - 1].shape
        img[0:h, 0:w] = overlayList[totalFingers - 1]

        cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        # cv2.putText(img, f'FPS: {int(fps)}', (750, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.putText(img, f'SUMA: {int(last_value)}', (400, 675), cv2.FONT_HERSHEY_PLAIN, 3, (43, 201, 72), 3)
        cv2.putText(img, f'OBJETIVO: {int(suma_obj)}', (355, 70), cv2.FONT_HERSHEY_PLAIN, 3, (24, 24, 156), 3)

        cv2.rectangle(img, (800, 10), (950, 60), (60, 76, 231), cv2.FILLED)
        cv2.putText(img, f'Salir', (823, 50), cv2.FONT_HERSHEY_PLAIN, 3, (15, 196, 241), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

def main():
    menu()

if __name__ == "__main__":
    main()