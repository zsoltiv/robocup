import cv2


def contours(gray):
    _, threshold = cv2.threshold(gray, 50, 255, 0)
    contours, hierarchy, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    return contours


def load_signs(file_list):
    """
    ugyanakkora a signs halmaz mint a file_list
    """
    signs = []
    for file_ in file_list:
        img = cv2.imread(file_)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        img = contours(img)
        signs.append(img)

    return signs


def get_sign(picture, signs):
    closest = 1.0
    closest_index = None
    for index, sign in enumerate(signs):
        match = cv2.matchShapes(picture, sign, 1, 0)
        if match < closest:
            closest = match
            closest_index = index

    # indexet adjuk vissza, hogy utana a fajllistabol
    # lekerhessuk melyik kephez all a legkozelebb
    return closest_index

import utils
signs = utils.files('signs')
imgs = load_signs(signs)
print(signs[get_sign(imgs[0], imgs)], signs)
