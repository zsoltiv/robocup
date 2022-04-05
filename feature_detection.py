from skimage.metrics import structural_similarity as ssim

import image


if __name__ == '__main__':
    fire1 = image.load_sign('fire1.jpg')
    fire2 = image.load_sign('fire2.jpg')
    print(ssim(fire1, fire2))
