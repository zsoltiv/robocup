import cv2
import numpy as np

def contours(gray):
    _, threshold = cv2.threshold(gray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    return contours


def canny(gray):
    #_, threshold         = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    #_, threshold_inverse = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
    return cv2.Canny(gray, 100, 200)


sign = cv2.imread('sign.png')
sign = cv2.cvtColor(sign, cv2.COLOR_RGB2GRAY)

cv2.imshow("test", canny(sign))
cv2.waitKey(0)

sign_h, sign_w = sign.shape[::-1]

img = cv2.imread('colored_test.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img_h, img_w = img.shape[:-1]

cv2.imshow("test", canny(img_gray))
cv2.waitKey(0)

sign_contours = contours(sign)
img_contours = contours(img_gray)
matched = cv2.matchShapes(sign_contours, img_contours, cv2.CONTOURS_MATCH_I1, 0.0)
print(matched)

#sign = cv2.resize(sign, (img_w // 2, img_h // 2), interpolation=cv2.INTER_LINEAR)

#res = cv2.matchTemplate(img_gray, sign, cv2.TM_CCOEFF_NORMED)
#threshold = 0.5
#coords = np.where(res >= threshold)

#_, threshold = cv2.threshold(img_gray, 127, 255, 0)
#contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(img, contours, -1, (0, 255, 0), 4)

#cv2.imshow("test", img)
#cv2.waitKey(0)
