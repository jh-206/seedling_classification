# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 16:07:46 2019

@author: jhirschi
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
from sklearn.model_selection import train_test_split
import tensorflow as tf
from keras.layers import MaxPooling2D
from functions import loadData

# =============================================================================
# Load Data
# =============================================================================

# If not using spyder project, set directory manually
if False: 
    os.chdir('...')

datadir = os.getcwd() + "/data/raw/v2-plant-seedlings-dataset"

cl_ls, img_ls = loadData.load_img_data(datadir)

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


# =============================================================================
# Model
# =============================================================================

model = tf.keras.models.Sequential()

