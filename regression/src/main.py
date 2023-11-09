#! /user/bin/env python3








__version__ = "0.1.0.0"
__author__ = "Vidyadhar Bendre<vidyadhar.bendre@gmail.com>"
__maintainers__ = [
    "Vidyadhar Bendre<vidyadhar.bendre@gmail.com>"
]

import sys
import os
import numpy as np

sys.path.insert(0, os.getcwd())
# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from data_manager import DataManager

def main():
    data_file_path = os.path.join('../data/houseprice.csv')
    data_manager = DataManager(data_file_path)
    