from os import path
from glob import glob


def find_ext(dr, ext):
    return glob(path.join(dr, "*.{}".format(ext)))
