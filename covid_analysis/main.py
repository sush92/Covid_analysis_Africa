
import pandas as pd
import numpy as np
import os
import argparse
from best_3_cntry import get_best_3_country

def initialize():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='file_path',type=str,default=False,help='covid csv file path')
    try:
        args = parser.parse_args()
        if args.file_path:
            if os.path.exists(args.file_path):
                return args.file_path
            else:
                raise Exception('\nFile not exists! \nPlease enter a valid path..')
    except:
        raise Exception('\nEnter the input file path..!')

if __name__ == "__main__":
    
    file_path = initialize()
    get_best_3_country(file_path)

