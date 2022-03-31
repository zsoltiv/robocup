from picamera import PiCamera
from picamera.array import PiRGBArray
from cv2 import cvtColor, COLOR_RGB2GRAY, imshow, waitKey
from image import load_signs, get_sign, contours
from utils import files


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
        bgr = PiRGBArray(self.picamera, size=(1024, 768))
        self.picamera.capture(bgr, 'bgr')
        return cvtColor(bgr.array, COLOR_RGB2GRAY)


camera = Camera()
# tesztelesre jo az a preview
camera.picamera.start_preview()
# tenyleges RGB-t ad
rgb = contours(camera.picture())
#camera.picamera.stop_preview()
#imshow('buzibaro', rgb)
#waitKey(0)
imgs = files('signs')
signs = load_signs(imgs)
print(imgs[get_sign(rgb, signs)])
