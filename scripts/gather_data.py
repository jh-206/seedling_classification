# -*- coding: utf-8 -*-
"""
Gather V2 seedling data

@author: jhirschi
"""

# =============================================================================
# Setup
# =============================================================================

import requests
import io
import zipfile
import os

out_dir = "C:/Users/jhirschi/Documents/Code/Python/seedling_classification/data"

resp = requests.get('https://www.kaggle.com/vbookshelf/v2-plant-seedlings-dataset/downloads/v2-plant-seedlings-dataset.zip/1')



