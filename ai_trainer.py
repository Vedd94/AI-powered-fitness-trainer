import cv2
import numpy as np
import time
import pose_estimator_module as pm

def pushUps(para1):

    # Handle webcam vs file
    if para1 is None:
        cap = cv2.VideoCapture(0)   # webcam
    else:
        cap = cv2.VideoCapture(para1) 

    detector = pm.poseDetector()
    count = 0
    dir1 = 0
    dir2 = 0
    while True:
        success, img = cap.read()
        # img = cv2.imread('AiTrainer/test.png')
        img = detector.findPose(img, False)
        lmList = detector.getPosition(img, draw = False)
        # print(img.shape)
        if len(lmList) != 0:

            angle1 = detector.findAngle(img, 12, 14, 16) # Right arm
            angle2 = detector.findAngle(img, 11, 13, 15) # Left arm

            per1 = np.interp(angle1, (60,180), (0, 100))
            per2 = np.interp(angle2, (60,180), (0, 100))

            # check for the squat
            if per1 == 100 or per2 == 100:
                if dir1 == 0 or dir2 == 0:
                    count += 0.5
                    dir1, dir2 = 1, 1

            if per1 == 0 or per2 == 0:
                if dir1 == 1 or dir2 == 1:
                    count += 0.5
                    dir1, dir2 = 0, 0

            # print(count) 

            cv2.rectangle(img, (0,250), (150,580), (0,255,0),cv2.FILLED)
            cv2.putText(img, str(int(count)), (50, 360), cv2.FONT_HERSHEY_PLAIN,5, (255,0,0),7)   

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                

        cv2.imshow("Image", img)
        cv2.waitKey(1)


def squats(para1):

    if para1 is None:
        cap = cv2.VideoCapture(0)   # webcam
    else:
        cap = cv2.VideoCapture(para1) 

    detector = pm.poseDetector()
    count = 0
    dir1 = 0
    dir2 = 0
    while True:
        success, img = cap.read()
        # img = cv2.imread('AiTrainer/test.png')
        img = detector.findPose(img, False)
        lmList = detector.getPosition(img, draw = False)
        print(img.shape)
        if len(lmList) != 0:

            angle1 = detector.findAngle(img, 24, 26, 28) # Right leg
            angle2 = detector.findAngle(img, 23, 25, 27) # Left leg

            per1 = np.interp(angle1, (76,180), (0, 100))
            per2 = np.interp(angle2, (76,180), (0, 100))

            # check for the squat
            if per1 == 100 or per2 == 100:
                if dir1 == 0 or dir2 == 0:
                    count += 0.5
                    dir1, dir2 = 1, 1

            if per1 == 0 or per2 == 0:
                if dir1 == 1 or dir2 == 1:
                    count += 0.5
                    dir1, dir2 = 0, 0

            # print(count) 

            cv2.rectangle(img, (0,350), (150,720), (0,255,0),cv2.FILLED)
            cv2.putText(img, str(int(count)), (50, 460), cv2.FONT_HERSHEY_PLAIN,5, (255,0,0),7)   
                

        cv2.imshow("Image", img)
        cv2.waitKey(1)


def bicepCurls(para1):

    if para1 is None:
        cap = cv2.VideoCapture(0)   # webcam
    else:
        cap = cv2.VideoCapture(para1) 

    detector = pm.poseDetector()
    count = 0
    dir1 = 0
    dir2 = 0
    while True:
        success, img = cap.read()
        # img = cv2.imread('AiTrainer/test.png')
        img = detector.findPose(img, False)
        lmList = detector.getPosition(img, draw = False)
        print(img.shape)
        if len(lmList) != 0:

            angle1 = detector.findAngle(img, 12, 14, 16) # Right Arm
            angle2 = detector.findAngle(img, 11, 13, 15) # Left Arm

            per1 = np.interp(angle1, (5,97), (0, 100))
            per2 = np.interp(angle2, (5,97), (0, 100))

            # check for the dumbell curls
            if per1 == 100 or per2 == 100:
                if dir1 == 0 or dir2 == 0:
                    count += 0.5
                    dir1, dir2 = 1, 1

            if per1 == 0 or per2 == 0:
                if dir1 == 1 or dir2 == 1:
                    count += 0.5
                    dir1, dir2 = 0, 0

            # print(count) 

            cv2.rectangle(img, (0,350), (150,720), (0,255,0),cv2.FILLED)
            cv2.putText(img, str(int(count)), (50, 460), cv2.FONT_HERSHEY_PLAIN,5, (255,0,0),7)   
                

        cv2.imshow("Image", img)
        cv2.waitKey(1)