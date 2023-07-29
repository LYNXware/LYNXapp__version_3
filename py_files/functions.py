import os
import sys


def resource_path(relative_path):
    # get absolute path to resource
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)