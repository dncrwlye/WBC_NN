#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 19:28:34 2021

@author: dancrowley
"""

#crop images using the crop_images.py file
#then resize them all to 250 x 250 sized image...for some reason!
  
from PIL import Image
from resizeimage import resizeimage
import os
import re
import argparse
import glob

parser = argparse.ArgumentParser()
parser.add_argument("--image_cropped", help="location of cropped images")
parser.add_argument("--imdir", help="where to save the images")
args = parser.parse_args()

#filenames = os.listdir('/Users/dancrowley/Desktop/bioinformatics/final_project/crop_dir/')
#filenames = os.listdir(args.image_cropped) + "*.jpg"

#filenames = '/Users/dancrowley/Desktop/bioinformatics/final_project/crop_dir/' + "*.jpg"

filenames = str(args.image_cropped) + "/*.jpg"

filenames = glob.glob(filenames)

for i in list(range(0,len(filenames),1)):

#fn = os.path.join('/Users/dancrowley/Desktop/bioinformatics/final_project/crop_dir/', filenames[0])
    fn = os.path.join(args.image_cropped, filenames[i])
    fd_img = open(fn, 'r+b')
    img = Image.open(fd_img)
    img = resizeimage.resize_contain(img, [1000, 1000])
    filenames[i]= re.sub(".jpg", ".png", filenames[i]) #change to .png
    filenames[i]= re.sub(str(args.image_cropped), str(args.imdir), filenames[i]) #change to .png
    filenames[i]= re.sub(" ", "_", filenames[i]) #change to .png
    #final_file = os.path.join(args.imdir, filenames[i])
    final_file = filenames[i]
    print(final_file)
    #final_file = os.path.join('/Users/dancrowley/Desktop/bioinformatics/final_project', filenames[i])
    img.save(final_file, img.format)
    fd_img.close()
    
    
    