import cv2 as cv
from hand_processing import HandProcessor


camera = cv.VideoCapture(0)
hand_processor = HandProcessor()

while True:
    success, img = camera.read()

    processed_img_like = hand_processor.like_func(img)
    cv.imshow("Like processing", processed_img_like)

    processed_img_retweet = hand_processor.retweet_func(img)
    #cv.imshow("Retweet processing", processed_img_retweet)


    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()
camera.release()
