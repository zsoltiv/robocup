import cv2
import numpy as np
from skimage.measure import compare_ssim as ssim
#from skimage.metrics import structural_similarity as ssim


def display(img):
    cv2.imshow('lol', img)
    cv2.waitKey(0)


def resize_to_same_size(img1, img2):
    w1, h1 = img1.shape[:2]
    w2, h2 = img2.shape[:2]

    w = max([w1, w2])
    h = max([h1, h2])

    img1 = cv2.resize(img1, (w, h))
    img2 = cv2.resize(img2, (w, h))

    return (img1, img2)


def match_percent(match):
    return (1.0 - match) * 100


def histogram(img):
    hist = cv2.calcHist([img], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    return cv2.normalize(hist, None).flatten()


def color_similarity(img1, img2):
    # histogram magia
    hist1 = cv2.calcHist([img1], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist2 = cv2.calcHist([img2], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    #hist1 = cv2.normalize(hist1, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F).flatten()
    #hist2 = cv2.normalize(hist2, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F).flatten()
    hist1 = cv2.normalize(hist1, None).flatten()
    hist2 = cv2.normalize(hist2, None).flatten()
    return match_percent(cv2.compareHist(hist1, hist2, cv2.HISTCMP_BHATTACHARYYA))


def contours(gray):
    # draga mulatsag, mert csinal egy masolatot az egesz kepbol,
    # ami nagy felbontasnal bajos lehet
    median_value = int(np.median(np.unique(np.copy(gray))))
    _, threshold = cv2.threshold(gray, median_value, 255, 0)
    #display(threshold)
    contours_tup = cv2.findContours(
            threshold,
            cv2.RETR_TREE,
            cv2.CHAIN_APPROX_SIMPLE)

    return threshold


def load_sign(file_):
    img = cv2.imread(file_)
    return contours(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY))


def load_signs(file_list):
    """
    ugyanakkora a signs halmaz mint a file_list
    """
    signs = []
    for file_ in file_list:
        signs.append(load_sign(file_))

    return signs


def get_sign(picture, signs):
    closest = 0.0
    closest_index = None
    for index, sign in enumerate(signs):
        try:
            r_picture, r_sign = resize_to_same_size(picture, sign)
            display(r_picture)
            display(r_sign)
            match = ssim(r_picture, r_sign)
            print(index, match)
            if match > closest:
                closest = match
                closest_index = index
        except Exception:
            pass

    # indexet adjuk vissza, hogy utana a fajllistabol
    # lekerhessuk melyik kephez all a legkozelebb
    return closest_index


# ideiglenes teszt kod
# csak akkor hivodik meg ha ezt a filet futtatjuk
if __name__ == '__main__':
    imgs = cv2.imread('fire1.jpg')
    test = cv2.imread('fire2.jpg')
    r_test, r_imgs = resize_to_same_size(test, imgs)
    print(match_percent(color_similarity(r_test, r_imgs)))
    #print(ssim(r_test, r_imgs))
