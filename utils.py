from os import listdir
from os.path import join


def files(dir_):
    """
    visszaadja egy mappa tartalmat
    """
    return [join(dir_, file) for file in listdir(dir_)]
