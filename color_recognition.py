from skimage.metrics import structural_similarity as ssim
from image import color_similarity, match_percent
from camera import Camera

from time import sleep

camera = Camera()

while True:
    sleep(1)
    camera.picture(display_=False)
    if len(camera.images) == 2:
        #match = ssim(camera.images[0], camera.images[1]) * 100
        #print(f'Ennyire hasonlóak a képek: {match}')
        #if match >= 90:
        #    print('egyeznek')
        #else:
        #    print('nem egyeznek')
        color_match = match_percent(color_similarity(camera.images[0], camera.images[1]))
        print(f'ennyire egyeznek: {color_match}')
        if color_match >= 90:
            print('egyeznek')
        else:
            print('nem egyeznek')
