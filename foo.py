from camera import Camera
from image import color_similarity, display

from skimage.measure import compare_ssim as ssim
from time import sleep

camera = Camera()
while True:
    camera.picture()
    #display(camera.images[-1][1])
    print('megapixel')
    if len(camera.images) == 2:
        match = ssim(camera.images[0][0], camera.images[1][0]) * 100
        print(f'Ennyire hasonlóak a képek: {match}')
        if match >= 90:
            print('egyeznek')
        else:
            print('nem egyeznek')
        #color_match = color_similarity(camera.images[0][1], camera.images[1][1])
        #if color_match >= 90:
        #    print('egyeznek')
        #else:
        #    print('nem egyeznek')
    sleep(1)
