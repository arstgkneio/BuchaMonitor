#this function should read data from column(s) of csv and populate a list

# populate rolling window with last 24 hours worth of data

import time as tm
import datetime
import os
import glob
import inspect
import pandas

# Builds working directory using canonical path
module_dir = os.path.realpath(os.path.dirname(module_path))

# Folder containing .csv files
path = module_dir + "/bucha_logs"
file_prefix = 'bucha_log'

# Padding character
padding_char = '_'

# function
def get_last_24hr_lines():
    file_list = glob.glob(path + '/' + file_prefix + '*.csv')
    file_list.sort()
    datafile1 = file_list[-1] #most recent data file
    datafile2 = file_list[-2] #2nd most recent data file
    concat_datafile =

    with open(datafile, 'rb') as f:
        f.seek(-2, os.SEEK_END)
        while f.read(1) != b'\n':
            f.seek(-2, os.SEEK_CUR)
        last_line = (f.readline().decode())
        return(last_line)
