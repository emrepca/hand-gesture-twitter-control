import cv2 as cv
import mediapipe
import keyboard
import time


class HandProcessor:
    def __init__(self):
        self.mpHands = mediapipe.solutions.hands
        self.hands = self.mpHands.Hands(max_num_hands=1)
        self.mpDraw = mediapipe.solutions.drawing_utils

    def bgr2RGB(self, img):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        return imgRGB

    def handLandMarkModel(self, imgRGB):
        hlms = self.hands.process(imgRGB)
        return hlms

    def like_func(self, hlms, imgRGB):
        height, width, _ = imgRGB.shape  # _ : channel (we do not use)

        if hlms.multi_hand_landmarks:
            for handlandmarks in hlms.multi_hand_landmarks:
                for fingerNum, landmark in enumerate(handlandmarks.landmark):
                    positionX, positionY = int(landmark.x * width), int(landmark.y * height)

                    if (fingerNum < 4 and landmark.y > handlandmarks.landmark[2].y and
                        handlandmarks.landmark[5].x > handlandmarks.landmark[8].x and
                        handlandmarks.landmark[9].x > handlandmarks.landmark[12].x and
                        handlandmarks.landmark [13].x > handlandmarks.landmark[16].x and
                        handlandmarks.landmark[17].x > handlandmarks.landmark[20].x and
                        handlandmarks.landmark[20].y > handlandmarks.landmark[2].y):
                        print("Like")

                self.mpDraw.draw_landmarks(imgRGB, handlandmarks, self.mpHands.HAND_CONNECTIONS)

        return imgRGB

    def retweet_func(self, hlms, imgRGB):
        height, width, _ = imgRGB.shape  # _ : channel (we do not use)

        if hlms.multi_hand_landmarks:
            for handlandmarks in hlms.multi_hand_landmarks:
                for fingerNum, landmark in enumerate(handlandmarks.landmark):
                    positionX, positionY = int(landmark.x * width), int(landmark.y * height)

                    if (handlandmarks.landmark[12].y < handlandmarks.landmark[11].y and
                        handlandmarks.landmark[16].y < handlandmarks.landmark[15].y and
                        handlandmarks.landmark[20].y < handlandmarks.landmark[19].y and
                        fingerNum == 4 or fingerNum == 8):

                        thumb_tip = handlandmarks.landmark[4]
                        index_tip = handlandmarks.landmark[8]

                        thumb_x, thumb_y = int(thumb_tip.x * width), int(thumb_tip.y * height)
                        index_x, index_y = int(index_tip.x * width), int(index_tip.y * height)

                        distance = ((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2) ** 0.5
                        #print(distance)

                        if distance < 30:
                            print("Retweet!")

                # self.mpDraw.draw_landmarks(img, handlandmarks, self.mpHands.HAND_CONNECTIONS)

        #return imgRGB


    def scroll_down_func(self, hlms, imgRGB):
        height, width, _ = imgRGB.shape

        if hlms.multi_hand_landmarks:
            for handlandmarks in hlms.multi_hand_landmarks:
                for fingerNum, landmark in enumerate(handlandmarks.landmark):
                    positionX, positionY = int(landmark.x * width), int(landmark.y * height)

                    if (handlandmarks.landmark[12].y > handlandmarks.landmark[9].y and
                        handlandmarks.landmark[16].y > handlandmarks.landmark[13].y and
                        handlandmarks.landmark[20].y > handlandmarks.landmark[17].y and
                        handlandmarks.landmark[4].x < handlandmarks.landmark[5].x and
                        handlandmarks.landmark[8].y < handlandmarks.landmark[5].y):
                        print("Scroll Down")

            #return imgRGB


    def scroll_up_func(self, hlms, imgRGB): #sorunlu
        height, width, _ = imgRGB.shape

        if hlms.multi_hand_landmarks:
            for handlandmarks in hlms.multi_hand_landmarks:
                for fingerNum, landmark in enumerate(handlandmarks.landmark):
                    positionX, positionY = int(landmark.x * width), int(landmark.y * height)

                    if (handlandmarks.landmark[8].y > handlandmarks.landmark[5].y and
                        handlandmarks.landmark[12].y < handlandmarks.landmark[9].y and
                        handlandmarks.landmark[16].y < handlandmarks.landmark[13].y and
                        handlandmarks.landmark[20].y < handlandmarks.landmark[17].y and
                        handlandmarks.landmark[4].x < handlandmarks.landmark[5].x and
                        handlandmarks.landmark[4].y > handlandmarks.landmark[0].y):
                        print("Scroll Up")

            #return imgRGB



    def bookmark_func(self, hlms, imgRGB):
        height, width, _ = imgRGB.shape

        if hlms.multi_hand_landmarks:
            for handlandmarks in hlms.multi_hand_landmarks:
                for fingerNum, landmark in enumerate(handlandmarks.landmark):
                    positionX, positionY = int(landmark.x * width), int(landmark.y * height)

                    if (handlandmarks.landmark[8].y > handlandmarks.landmark[7].y and
                        handlandmarks.landmark[12].y > handlandmarks.landmark[11].y and
                        handlandmarks.landmark[16].y > handlandmarks.landmark[15].y and
                        handlandmarks.landmark[20].y > handlandmarks.landmark[19].y and
                        handlandmarks.landmark[4].x > handlandmarks.landmark[1].x):
                        print("Bookmark!")



    def empty_func(self, hlms, imgRGB):

        height, width, _ = imgRGB.shape

        if hlms.multi_hand_landmarks:
            for handlandmarks in hlms.multi_hand_landmarks:
                for fingerNum, landmark in enumerate(handlandmarks.landmark):
                    positionX, positionY = int(landmark.x * width), int(landmark.y * height)

                    thumb_tip = handlandmarks.landmark[4]
                    index_tip = handlandmarks.landmark[8]

                    thumb_x, thumb_y = int(thumb_tip.x * width), int(thumb_tip.y * height)
                    index_x, index_y = int(index_tip.x * width), int(index_tip.y * height)

                    distance = ((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2) ** 0.5

                    if (handlandmarks.landmark[4].y < handlandmarks.landmark[3].y and
                        handlandmarks.landmark[8].y < handlandmarks.landmark[7].y and
                        handlandmarks.landmark[12].y < handlandmarks.landmark[11].y and
                        handlandmarks.landmark[16].y < handlandmarks.landmark[15].y and
                        handlandmarks.landmark[20].y < handlandmarks.landmark[19].y and
                        handlandmarks.landmark[8].y < handlandmarks.landmark[4].y and
                        distance > 120):
                        print("Empty hand!")