import cv2
import numpy as np


def display(img):
    cv2.imshow('lol', img)
    cv2.waitKey(0)

def contours(gray):
    median_value = int(np.median(np.unique(np.copy(gray))))
    print(median_value)
    _, threshold = cv2.threshold(gray, median_value, 255, 0)
    display(threshold)
    contours_tup, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 4.5.4 ota valamiert tuple-t ad vissza alapbol, szoval csinalunk belole listat
    return contours_tup[0]

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
        match = cv2.matchShapes(picture, sign, 1, 0)
        if match > closest:
            closest = match
            closest_index = index

    # indexet adjuk vissza, hogy utana a fajllistabol
    # lekerhessuk melyik kephez all a legkozelebb
    return closest_index

import utils
signs = utils.files('signs')
print(signs)
imgs = load_signs(signs)
test = load_sign('test.jpg')
print(signs[get_sign(test, imgs)], signs)
