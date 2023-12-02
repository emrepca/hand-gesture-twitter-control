import cv2 as cv
import mediapipe

camera = cv.VideoCapture(0)

mpHands = mediapipe.solutions.hands

hands = mpHands.Hands(max_num_hands=2)

mpDraw = mediapipe.solutions.drawing_utils

while True:

    success, img = camera.read()

    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB) #converting image to RGB format

    hlms = hands.process(imgRGB)
    print(hlms.multi_hand_landmarks)

    if hlms.multi_hand_landmarks:
        for handlanmarks in hlms.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handlanmarks, mpHands.HAND_CONNECTIONS)


    cv.imshow("Camera", img)
    if cv.waitKey(1) & 0xFF == 27: #27, the value of the esc key in the ASCII table.
        break

