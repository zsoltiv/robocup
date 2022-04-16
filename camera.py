from picamera import PiCamera
from picamera.array import PiRGBArray
from cv2 import cvtColor, COLOR_BGR2GRAY, imwrite
from image import contours, avg_color, color_distance_percent, display
from time import sleep


class Camera:
    """
    minimalis class a camera kore, mert csak (ettol nem lesz lassabb)
    """

    def picture(self, display_=False):
        bgr = PiRGBArray(self.picamera, size=self._resolution)
        self.picamera.capture(bgr, 'bgr')
        if display_:
            display(bgr.array)
        #sleep(1)
        avg = avg_color(bgr.array)
        print(f'átlag szín {avg}')
        cnt = contours(cvtColor(bgr.array, COLOR_BGR2GRAY))
        if len(self.images) >= 2:
            self.images = [(cnt, avg)]
        else:
            self.images.append((cnt, avg))
        name = 'img' + str(len(self.images)) + '.png'
        #imwrite(name, cnt)

    def __init__(self):
        self.picamera = PiCamera()
        self._resolution = (1024, 768)
        self.picamera.resolution = self._resolution
        #self.picamera.color_effects = (128, 128)
        self.images = []
        # takolt workaround, mert a legelso kep szar
        self.picture()
        self.images = []


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
