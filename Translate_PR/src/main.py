from core.capture import ScreenCapture
#from core.OCR import paddl_ocrs
# src/main.py
from core.OCR.paddl_ocr import paddl_ocrs
import paddle
if __name__ == "__main__":
   print("ScreenCapture module is ready to use.")
   cap = ScreenCapture()
   img = cap.capture_region(top=0, left=0, width=300, height=200) 
   print("✓ Đã chụp và lưu ảnh thành công!")

   img = cap.capture_screen(monitor=1)
   cap.save_screenshot(img, "captured_region1.png")
   print("✓ Đã chụp và lưu ảnh thành công!")  
   IMG_PATH = "hih.png"  
   text = paddl_ocrs(IMG_PATH, lang="en")   # gọi hàm nhận dạng
   print(text.recognize())  
   
   