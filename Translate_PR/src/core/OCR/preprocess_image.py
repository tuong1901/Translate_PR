import cv2
class preprocess_image:
    def __init__(self):
        pass
    def _preprocess(self, img): 
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        return img

        