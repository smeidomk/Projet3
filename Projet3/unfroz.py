import os

import sys

def find_data_file(filename):
	# find_data_file is used in order to display the game's images
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(__file__)
    return os.path.join(datadir, filename)