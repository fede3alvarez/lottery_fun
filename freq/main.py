import os
import datetime

import IPython
import IPython.display
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf

mpl.rcParams['figure.figsize'] = (8, 6)
mpl.rcParams['axes.grid'] = False


def get_data(filename, directory = None):
    base_folder = os.path.dirname(__file__)

    if directory is None:
        filename = os.path.join(base_folder, filename)
    else:    
        filename = os.path.join(base_folder, directory, filename)
    