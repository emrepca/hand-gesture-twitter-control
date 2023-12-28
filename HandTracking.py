import cv2 as cv
from hand_processing import HandProcessor


camera = cv.VideoCapture(0)
hand_processor = HandProcessor()

while True:
    success, img = camera.read()
    processed_img = hand_processor.like_func(img)
    cv.imshow("Camera", processed_img)

    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()
camera.release()
