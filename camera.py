from picamera import PiCamera
from picamera.array import PiRGBArray
from cv2 import cvtColor, COLOR_BGR2GRAY


class Camera:
    """
    minimalis class a camera kore, mert csak (ettol nem lesz lassabb)
    """

    def __init__(self):
        self.picamera = PiCamera()
        self.picamera.resolution = (1024, 768)
        self.picamera.color_effects = (128, 128)

    def picture(self):
        # cvtColor() es COLOR_BGR2GRAY a cv2-ben van
        #
        # COLOR_RGB2GRAY helyett COLOR_BGR2GRAY, mert a PiRGBArray() fuggveny
        # forditott RGB-t ad (Blue, Green, Red)
        #
        # ennek az eredmenyet ha parameterkent odaadjuk a contours()-nak
        # akkor megkapjuk a konturokat amiket osszehasonlithatunk
        return cvtColor(PiRGBArray(self.picamera), COLOR_BGR2GRAY)


camera = Camera()
# tesztelesre jo az a preview
camera.picamera.start_preview()
# tenyleges RGB-t ad
rgb = camera.picture()
