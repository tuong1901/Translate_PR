from capture import ScreenCapture

class Framefix:
    def __init__(self):
        pass

    def capFullmon(self):
        cap = ScreenCapture()
        img = cap.capture_region(top=0, left=0, width=300, height=200) 
        print("✓ Đã chụp và lưu ảnh thành công!")

        img = cap.capture_screen(monitor=1)
        cap.save_screenshot(img, "captured_region1.png")
        print("✓ Đã chụp và lưu ảnh thành công!")
      