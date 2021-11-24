# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 14:09:28 2021

@author: Sanidhya
"""

import cv2
import numpy as np
from skimage import io, img_as_float, img_as_ubyte
from skimage.restoration import denoise_nl_means, estimate_sigma

img = img_as_float(io.imread('D:/Academics/IITD/7th Sem/BTP/Image data/5.jpg'))

sigma_est = np.mean(estimate_sigma(img, multichannel = True))

denoising_img = denoise_nl_means(img, h=1.25*sigma_est, fast_mode=True, 
                                 patch_size=5, 
                                 patch_distance=3, 
                                 multichannel= True)

cv2.imshow('Original', img)
cv2.imshow('Denoised', denoising_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
         
img_8bit = img_as_ubyte(img)
denoised_8bit = img_as_ubyte(denoising_img)
io.imsave('D:/Academics/IITD/7th Sem/BTP/Image data/5_denoised.jpg')
