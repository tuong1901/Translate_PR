from OCR import paddl_ocrs
from capture import capture_region

class translate_pipeline:
    def __init__(self):
        self.capture_region = capture_region()
        self.paddl_ocrs = paddl_ocrs()
    def pipeline(self):
        img = self.capture_region.capture_region()
        text = self.paddl_ocrs.recognize(img)
        return text
    