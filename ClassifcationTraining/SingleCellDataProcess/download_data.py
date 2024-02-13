# -*- coding: utf-8 -*-
"""
Created on Sun May 14 13:41:21 2023

@author: Yuta
"""

import sys, os


#option = int(sys.argv[1])
#random_state = int(sys.argv[2])

data_process_path = './SingleCellDataProcess/'   #change this line if you have a different path for the data processing
data_path = './data/'  #location of where the processed raw data will be saved


data_vec = [ 'GSE75748cell', 'GSE75748time', 'GSE84133human3']
for data in data_vec:
    os.system('python main.py --data ' + data)

