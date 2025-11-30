from OCR import paddl_ocrs
from capture import capture_region
from trans import translation_ggapi
class translate_pipeline:
    def __init__(self):
        self.capture_region = capture_region()
        self.paddl_ocrs = paddl_ocrs()
        self.translate = translation_ggapi()
    def pipeling_regioncapture(self):
        print("ScreenCapture module is ready to use.")
        cap = ScreenCapture()
        img = cap.capture_region(top=0, left=0, width=300, height=200) 
        print("✓ Đã chụp và lưu ảnh thành công!")
        cap.save_screenshot(img, "captured_region1.png")
        print("✓ Đã chụp và lưu ảnh thành công!")  
        IMG_PATH = "hih.png"  
        text = paddl_ocrs(IMG_PATH, lang="en")   # gọi hàm nhận dạng
        print(text.recognize())  
        text = self.paddl_ocrs.recognize(img)
        return text
    
   

   