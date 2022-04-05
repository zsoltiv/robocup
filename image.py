import cv2
import numpy as np


def display(img):
    cv2.imshow('lol', img)
    cv2.waitKey(0)


def match_percent(match):
    return (1.0 - match) * 100


def contours(gray):
    # draga mulatsag, mert csinal egy masolatot az egesz kepbol,
    # ami nagy felbontasnal bajos lehet
    median_value = int(np.median(np.unique(np.copy(gray))))
    _, threshold = cv2.threshold(gray, median_value, 255, 0)
    threshold = cv2.resize(threshold, (1280, 720))
    display(threshold)
    contours_tup, hierarchy = cv2.findContours(
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
    closest = 1.0
    closest_index = None
    for index, sign in enumerate(signs):
        match = cv2.matchShapes(picture, sign, 1, 0)
        print(index, match_percent(match))
        if match < closest:
            closest = match
            closest_index = index

    # indexet adjuk vissza, hogy utana a fajllistabol
    # lekerhessuk melyik kephez all a legkozelebb
    return closest_index


# ideiglenes teszt kod
# csak akkor hivodik meg ha ezt a filet futtatjuk
