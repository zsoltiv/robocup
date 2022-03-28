import cv2
from os import listdir
from os.path import join
import numpy as np


def contours(gray):
    _, threshold = cv2.threshold(gray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    return contours


def load_signs(directory):
    signs = []
    for file_ in listdir(directory):
        img = cv2.imread(join(directory, file_))
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        img = contours(img)
        signs.append(img)

    return signs


def get_sign(picture, signs):
    closest = 1.0
    for sign in signs:
        match = cv2.matchShapes(picture, sign, )
        if match < closest:
            closest = match

    return closest


signs = load_signs('signs')
