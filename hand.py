from audioop import tostereo
from pickletools import markobject
import cv2
import mediapipe as md
import hand_tracking_module as htm
import voice

cap =cv2.VideoCapture(0)
detect = htm.handDetector()
tipIds=[4,8,12,16,20]
while True:
    success, img=cap.read()
    img = detect.findHands(img)
    mark_position =detect.findPosition(img,draw=False)
    if len(mark_position) !=0:
            fingers=[]
        # Thumb
            if mark_position[tipIds[0]][1] > mark_position[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            for id in range(1,5):  #y axis
                if mark_position[tipIds[id]][2] < mark_position[tipIds[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            totalFingers=str(fingers.count(1))
            cv2.putText(img,totalFingers, (60,60), cv2.FONT_HERSHEY_SIMPLEX, 1, 255)
            # voice.voice.speak(totalFingers)
    
    cv2.imshow("Image",img)
    cv2.waitKey(1)
   
    

