import cv2
import numpy as np
#from skimage.measure import compare_ssim as ssim
from skimage.metrics import structural_similarity as ssim
from skimage.exposure import match_histograms


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


def match_percent2(match):
    return match * 100


def histogram(img):
    #channels = cv2.split(img)
    #hists = []
    #for i in range(3):
    #    hist = cv2.calcHist(channels, [i], None, [256], [0, 256])
    #    hist = cv2.normalize(hist, None),flatten()
    #    hists.append(hist)
    #return hists
    img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    return cv2.normalize(cv2.calcHist([img], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256]), None).flatten()


def color_similarity(img1, img2):
    # histogram magia
    
    #matches = []
    #for i in range(3):
    #    matches.append(cv2.compareHist(img1[i], img2[i], cv2.HISTCMP_BHATTACHARYYA))
    #matches = np.sort(np.array(matches))
    #print(matches)
    #median = np.median(matches)
    #print(median)
    #return median
    #sum_ = 0
    #for match in matches:
    #    print(match)
    #    sum_ += match

    #return sum_ / len(matches)
    #return match_histograms(img1, img2, multichannel=True)
    #return cv2.compareHist(img1, img2, cv2.HISTCMP_BHATTACHARYYA)
    return cv2.compareHist(img1, img2, cv2.HISTCMP_BHATTACHARYYA)


def gray_median(gray):
    return int(np.median(np.unique(np.copy(gray))))

def contours(gray):
    # draga mulatsag, mert csinal egy masolatot az egesz kepbol,
    # ami nagy felbontasnal bajos lehet
    median_value = gray_median(gray)
    _, threshold = cv2.threshold(gray, median_value, 255, 0)
    #display(threshold)
    contours_tup = cv2.findContours(
            threshold,
            cv2.RETR_TREE,
            cv2.CHAIN_APPROX_SIMPLE)

    return threshold


def avg_color(img):
    return np.average(np.average(img, axis=0), axis=0)


def color_distance_percent(avg1, avg2):
    diff = np.absolute(np.subtract(avg1, avg2))
    hundreds = np.asarray([100, 100, 100])
    distance = np.absolute(np.subtract(avg1, diff))
    return np.multiply(np.divide(distance, avg1), hundreds)


#def load_sign(file_):
#    img = cv2.imread(file_)
#    return contours(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY))
#
#
#def load_signs(file_list):
#    """
#    ugyanakkora a signs halmaz mint a file_list
#    """
#    signs = []
#    for file_ in file_list:
#        signs.append(load_sign(file_))
#
#    return signs
#
#
#def get_sign(picture, signs):
#    closest = 0.0
#    closest_index = None
#    for index, sign in enumerate(signs):
#        try:
#            r_picture, r_sign = resize_to_same_size(picture, sign)
#            display(r_picture)
#            display(r_sign)
#            match = ssim(r_picture, r_sign)
#            print(index, match)
#            if match > closest:
#                closest = match
#                closest_index = index
#        except Exception:
#            pass
#
#    # indexet adjuk vissza, hogy utana a fajllistabol
#    # lekerhessuk melyik kephez all a legkozelebb
#    return closest_index


# ideiglenes teszt kod
# csak akkor hivodik meg ha ezt a filet futtatjuk
if __name__ == '__main__':
    test1 = avg_color(cv2.imread('tests/test1.jpg'))
    test2 = avg_color(cv2.imread('tests/test3.jpg'))
    print(color_distance_percent(test1, test2))
