# paddl_ocr.py
import cv2
from paddleocr import PaddleOCR  # newer API name
from PIL import Image
import os
from paddleocr import TextRecognition

class paddl_ocrs:
    def __init__(self, img_path, lang): 
        self.ocr = PaddleOCR(
            lang=lang, 
            use_angle_cls=True 
         )
        self.img_path = img_path

    def _preprocess(self, img): 
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        return img

    def recognize(self): 
        img = cv2.imread(self.img_path)
        if img is None:
            raise FileNotFoundError(f"Cannot read image: {self.img_path}")
        
        proc_img = self._preprocess(img)
        result = self.ocr.ocr(self.img_path )

        text_lines = []
        for line in result:
            for res in line:
                text_lines.append(res[1][0])

        return "\n".join(text_lines)

