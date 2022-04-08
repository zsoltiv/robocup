from picamera import PiCamera
from picamera.array import PiRGBArray
from cv2 import cvtColor, COLOR_BGR2GRAY, imshow, waitKey
from image import contours


class Camera:
    """
    minimalis class a camera kore, mert csak (ettol nem lesz lassabb)
    """

    def __init__(self):
        self.picamera = PiCamera()
        self._resolution = (1024, 768)
        self.picamera.resolution = self._resolution
        self.picamera.color_effects = (128, 128)
        self.images = []

    def picture(self):
        bgr = PiRGBArray(self.picamera, size=self._resolution)
        self.picamera.capture(bgr, 'bgr')
        cnt = contours(cvtColor(bgr.array, COLOR_BGR2GRAY))
        #return cvtColor(bgr.array, COLOR_RGB2GRAY)
        if len(self.images) >= 2:
            self.images = [cnt]
        else:
            self.images.append(cnt)


if __name__ == '__main__':
    from utils import files
    camera = Camera()
    # tesztelesre jo az a preview
    # tenyleges RGB-t ad
    rgb = camera.picture()
    imshow('bulibaro', rgb)
    waitKey(0)
    imshow('bulibaro', contours(rgb))
    waitKey(0)
    #imshow('buzibaro', rgb)
    #waitKey(0)
    imgs = files('signs')
    signs = load_signs(imgs)
    print(imgs[get_sign(rgb, signs)])
