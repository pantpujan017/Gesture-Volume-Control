import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange=volume.GetVolumeRange()

minVol=volRange[0]
maxVol=volRange[1]
vol=0
volBar=400
volPer=0
area=0
colorVol=(255,0,0)
##
wCam, hCam=640,480
##
cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime=0

detector=htm.handDetector(detectionCon=0.7,maxHands=1)


while True:
    success, img = cap.read()

    # Find Hand

    img=detector.findHands(img)
    lmList,bbox=detector.findPosition(img,draw=True)
    if len(lmList) !=0:

        # Filter based on size
        area=(bbox[2]-bbox[0])*(bbox[3]-bbox[1])//100
        # print(area)
        if 250<area<1000:
            # print("yes")
            # Find Distance between index and Thumb
            length,img,lineInfo=detector.findDistance(4,8,img)
            # print(length)

        # Convert Volume

            volBar = np.interp(length, [50, 200], [400, 150])
            volPer = np.interp(length, [50, 200], [0, 100])

            smoothness=10
            volPer=smoothness*round(volPer/smoothness)



        # Reduce Resolution to make it smoother

        # Check fingers up
            fingers=detector.fingersUp()
            print(fingers)


        # If pinky is down set volume
            if not fingers[4]:
                volume.SetMasterVolumeLevelScalar(volPer/100, None)
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0,255,0), cv2.FILLED)
                colorVol=(0,255,0)
            else:
                colorVol=(255,0,0)




        # Drawings

        # Frame rate


        # print(lmList[4],lmList[8])

        x1,y1=lmList[4][1],lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)

        cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)
        cv2.circle(img, (cx, cy), 15, (255, 0, 255),cv2.FILLED)

        length=math.hypot(x2-x1,y2-y1)
        #print(length)


        # Hand range was 50-300
        # Volume Range -65 - 0

    cv2.rectangle(img,(50,150),(85,400),(255,0,0),3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255,0,0), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 3)
    cVol = int(volume.GetMasterVolumeLevelScalar() * 100)
    cv2.putText(img, f'Vol Set: {int(cVol)}', (400, 50), cv2.FONT_HERSHEY_COMPLEX,
                1, colorVol, 3)

    cTime = time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,f'FPS:{int(fps)}',(40,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)

    cv2.imshow("Img", img)
    cv2.waitKey(1)

