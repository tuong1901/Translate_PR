import mss
import mss.tools
from mss import mss as mss_instance
from PIL import Image
from typing import Tuple
#Có cách chụp kiểu khác để nó ấy được overlay
class ScreenCapture:
    #Khởi tạo biến self và lớp thuộc tính của nó
    def __init__(self):
        self.sct = mss_instance()
    #khai báo phương thức capture_screen với đầu vào là monitor và trả về một đối tượng Image.Image
    def capture_screen(self, monitor: int = 1) -> Image.Image:
         
        screenshot = self.sct.grab(self.sct.monitors[monitor])
        img = Image.frombytes('RGB', screenshot.size, screenshot.rgb)
        return img
    
    def capture_region(self, top: int, left: int, width: int, height: int) -> Image.Image:
    
        region = {
            "top": top,
            "left": left,
            "width": width,
            "height": height
        } 
        output = "sct-{top}x{left}_{width}x{height}.png".format(**region)
        screenshot = self.sct.grab(region)
        img = Image.frombytes('RGB', screenshot.size, screenshot.rgb)
        mss.tools.to_png(screenshot.rgb, screenshot.size ) 
        return img
    
    def save_screenshot(self, img: Image.Image, file_path: str) -> None:
 
        img.save(file_path)
   