import cv2

import utils
import image


def load_img(file_):
    return cv2.imread(file_, 0)


if __name__ == '__main__':
    template_files = utils.files('signs')
    test_files = utils.files('tests')
    templates = [load_img(file_) for file_ in template_files]
    tests = [load_img(file_) for file_ in test_files]
    template_widths = [template.shape[::-1] for template in templates]

    for test in tests:
        test = test.copy()
        for i, template in enumerate(templates):
            try:
                res = cv2.matchTemplate(test, template, cv2.TM_SQDIFF)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                cv2.rectangle(
                        test,
                        min_loc,
                        (min_loc[0] + template_widths[i][0], min_loc[1] + template_widths[i][1]),
                        255,
                        2)
            except:
                pass
