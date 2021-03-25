import numpy as np
import glob
import pandas as pd

class Review:
    """
    import the file of reviews
    """
    def __init__(self, path):
        self.row = pd.read_csv(path)