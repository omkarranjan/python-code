# -*- coding: utf-8 -*-
"""
Created on Thu May 17 14:37:08 2018

@author: Omkar Ranjan

Code to rename the text files as Foldername_oldfilename_series and store saperately in output file .(renaming files from sub folders of a folder.)

"""


import glob, os
from shutil import copyfile


directory_list = list()
for root, dirs, files in os.walk("C:/Users/IBM_ADMIN/Desktop/dummy_main", topdown=False):
    for name in dirs:
        directory_list.append(os.path.join(root, name))

print( directory_list)

for dire in directory_list:
    i = 1
    for pathAndFilename in glob.iglob(os.path.join(dire, r'*.txt')):
        titlePattern =  dire.split('\\')[-1]+'_%s_' + str(i)
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        copyfile(pathAndFilename, os.path.join("C:/Users/IBM_ADMIN/Desktop"+ "/output/" , titlePattern % title + ext))
        i = i + 1
        