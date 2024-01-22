import cv2 as cv
import mediapipe

class HandProcessor:
    def __init__(self):
        self.mpHands = mediapipe.solutions.hands
        self.hands = self.mpHands.Hands(max_num_hands=2)
        self.mpDraw = mediapipe.solutions.drawing_utils

    def like_func(self, img):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        hlms = self.hands.process(imgRGB)
        height, width, _ = img.shape # _ : channel (we do not use)

        if hlms.multi_hand_landmarks:
            for handlandmarks in hlms.multi_hand_landmarks:
                for fingerNum, landmark in enumerate(handlandmarks.landmark):
                    positionX, positionY = int(landmark.x * width), int(landmark.y * height)

                    if fingerNum > 4 and landmark.y < handlandmarks.landmark[2].y:
                        break

                    if fingerNum == 5 and landmark.x < handlandmarks.landmark[8].x:
                        break

                    if fingerNum == 9 and landmark.x < handlandmarks.landmark[12].x:
                        break

                    if fingerNum == 13 and landmark.x < handlandmarks.landmark[16].x:
                        break

                    if fingerNum == 17 and landmark.x < handlandmarks.landmark[20].x:
                        break

                    if fingerNum == 20 and landmark.y > handlandmarks.landmark[2].y:
                        print("Like!")

                self.mpDraw.draw_landmarks(img, handlandmarks, self.mpHands.HAND_CONNECTIONS)

        return img


    def retweet_func(self, img):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        hlms = self.hands.process(imgRGB)
        height, width, _ = img.shape  # _ : channel (we do not use)

        if hlms.multi_hand_landmarks:
            for handlandmarks in hlms.multi_hand_landmarks:
                for fingerNum, landmark in enumerate(handlandmarks.landmark):
                    positionX, positionY = int(landmark.x * width), int(landmark.y * height)

                    if handlandmarks.landmark[12].y > handlandmarks.landmark[9].y:
                        break

                    if handlandmarks.landmark[16].y > handlandmarks.landmark[13].y:
                        break

                    if handlandmarks.landmark[20].y > handlandmarks.landmark[17].y:
                        break

                    if fingerNum == 4 or fingerNum == 8:

                        thumb_tip = handlandmarks.landmark[4]
                        index_tip = handlandmarks.landmark[8]

                        thumb_x, thumb_y = int(thumb_tip.x * width), int(thumb_tip.y * height)
                        index_x, index_y = int(index_tip.x * width), int(index_tip.y * height)

                        distance = ((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2) ** 0.5
                        #print(distance)

                        if distance < 20:
                            print("Retweet!")

                #self.mpDraw.draw_landmarks(img, handlandmarks, self.mpHands.HAND_CONNECTIONS)

        return img

