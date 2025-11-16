import mss
import mss.tools
from mss import mss as mss_instance
from PIL import Image
from typing import Tuple
class ScreenCapture:
    def __init__(self):
        self.sct = mss_instance()

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
        screenshot = self.sct.grab(region)
        img = Image.frombytes('RGB', screenshot.size, screenshot.rgb)
        return img
    def save_screenshot(self, img: Image.Image, file_path: str) -> None:
 
        img.save(file_path)

    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Capture the primary monitor
        screenshot = sct.grab(monitor)

 