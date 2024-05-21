import cv2 as cv
from hand_processing import HandProcessor


camera = cv.VideoCapture(0)
hand_processor = HandProcessor()

while camera.isOpened():
    success, img = camera.read()

    rgbImage = hand_processor.bgr2RGB(img)
    hlms = hand_processor.handLandMarkModel(rgbImage)

    processed_like_func = hand_processor.like_func(hlms, rgbImage)
    processed_retweet_func = hand_processor.retweet_func(hlms, rgbImage)
    processed_scroll_down_func = hand_processor.scroll_down_func(hlms, rgbImage)
    processed_scroll_up_func = hand_processor.scroll_up_func(hlms, rgbImage)
    processed_bookmark_func = hand_processor.bookmark_func(hlms, rgbImage)
    processed_empty_func = hand_processor.empty_func(hlms, rgbImage)

    cv.imshow("WebCam", processed_like_func)

    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()
camera.release()
