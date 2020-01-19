# -*- coding: utf-8 -*-

import cv2
import os

def load_img_data(path):
    
    seed_class = os.listdir(path)
    seed_class2 = seed_class[0:2]
    nfiles = 0
    for sc in seed_class2:
        files = [fn for fn in os.listdir(os.path.join(path, sc))
                  if fn.endswith('.png')]
        nfiles += len(files)
    
    img_ls = [None] * nfiles # list of image data
    cl_ls = [None] * nfiles # list of class labels
    
    
    i = 0
    for sc in seed_class2:
        files = [os.path.join(path, sc, fn) for fn in os.listdir(os.path.join(path, sc))
                  if fn.endswith('.png')]
        for f in files:
            img_temp = cv2.imread(f)
            cl_ls[i] = sc
            # Clean image
            img_ls[i] = img_temp
            i = i+1
        
    img_ls = [cv2.GaussianBlur(img, (5, 5), 0) for img in img_ls] 
    
    return (cl_ls, img_ls)