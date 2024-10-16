# Python3 program to process 
# images using scikit-image

# pip install -U scikit-image
import os

# importing io from skimage
import skimage
from skimage import io

# way to load car image from file
#file = os.path.join(skimage.data_dir, 'ganesh.jpg')


cars = io.imread("ganesh.jpg")

# way to show the input image
io.imshow(cars)
io.show()
