from .capture import ScreenCapture

if __name__ == "__main__": 
    screen_capture = ScreenCapture()
     
    image = screen_capture.capture_region(100, 100, 300, 200)
     
    image.save("captured_region.png")
