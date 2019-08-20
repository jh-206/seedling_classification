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
from sklearn.model_selection import train_test_split


# If not using spyder project, set directory manually
if False: 
    os.chdir('...')


datadir = os.getcwd() + "/data/raw/v2-plant-seedlings-dataset"
#os.path.isfile(datadir + "/Black-grass/1.png")

seed_class = os.listdir(datadir)
seed_class2 = seed_class[0:2]
nfiles = 0
for sc in seed_class2:
    files = [fn for fn in os.listdir(os.path.join(datadir, sc))
              if fn.endswith('.png')]
    nfiles += len(files)

img_ls = [None] * nfiles # list of image data
cl_ls = [None] * nfiles # list of class labels


i = 0
for sc in seed_class2:
    files = [os.path.join(datadir, sc, fn) for fn in os.listdir(os.path.join(datadir, sc))
              if fn.endswith('.png')]
    for f in files:
        img_temp = cv2.imread(f)
        cl_ls[i] = sc
        # Clean image
        img_ls[i] = img_temp
        i = i+1
    
# =============================================================================
# Clean images
# =============================================================================

img_ls = [cv2.GaussianBlur(img, (5, 5), 0) for img in img_ls] 



#cv2.imshow("image", tr_img_ls[20])
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# =============================================================================
# Partition Train, Test, Validation
# =============================================================================

seed = 5
split = (.8, .1, .1)

len(cl_ls)
cl = np.asarray(cl_ls)

img_tr,img_te,cl_tr,cl_te = train_test_split(
        img_ls,cl_ls,test_size=0.1,random_state=seed,stratify=cl_ls)

img_tr, img_val, cl_tr, cl_val= train_test_split(
    img_tr, cl_tr, test_size=0.1, random_state=seed,stratify=cl_tr)






