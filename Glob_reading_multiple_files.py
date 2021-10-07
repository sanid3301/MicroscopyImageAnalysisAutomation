# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 15:20:04 2021

@author: Sanidhya
"""

import cv2
import glob

file_list = glob.glob('D:/Academics/IITD/7th Sem/BTP/Image data/*.*')
print (file_list)

my_list = []

path = 'D:/Academics/IITD/BTP/Image data/*.*'
for file in glob.glob(path):
    a = cv2.imread(file)
    my_list.append(a)
    