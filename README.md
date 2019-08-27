# People counting raspberry pi
people counting using deep learning on raspberry pi

This is two main parts combine together. one is a model to decide a picture of 64x64 is a head or not, another is to sliding windows along all parts of the image, with the stripe of 50. and select those with the score of larger than the threshold to be head.

libraries needs keras, tensorflow, opencv-python==3.4.5.20, numpy
