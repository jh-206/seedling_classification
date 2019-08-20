# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 17:13:48 2019

@author: jhirschi
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import glob

# If not using spyder project, set directory manually
if False: 
    os.chdir('...')


datadir = os.getcwd() + "/data/raw/v2-plant-seedlings-dataset"
os.path.isfile(datadir + "/Black-grass/1.png")

seed_class = os.listdir(datadir)
seed_class2 = seed_class[0:2]
nfiles = 0
for sc in seed_class2:
    files = [fn for fn in os.listdir(os.path.join(datadir, sc))
              if fn.endswith('.png')]
    nfiles += len(files)

tr_img_ls = [None] * nfiles # list of image data
tr_cl_ls = [None] * nfiles # list of class labels

i = 0
for sc in seed_class2:
    files = [os.path.join(datadir, sc, fn) for fn in os.listdir(os.path.join(datadir, sc))
              if fn.endswith('.png')]
    for f in files:
        img_temp = cv2.imread(f)
        tr_cl_ls[i] = sc
        # Clean image
        tr_img_ls[i] = img_temp
        i = i+1


    
    



#img = cv2.imread(datadir + "/Black-grass/1.png")
#imgb = cv2.imread(datadir + "/Black-grass/1.png", cv2.IMREAD_GRAYSCALE)
#
img = tr_img_ls[100]
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#
#plt.imshow(img, cmap = "gray")




# =============================================================================
# Gaussian Blur
# =============================================================================

img_blur = cv2.GaussianBlur(img, (5, 5), 0)

cv2.imshow("image", img_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()


