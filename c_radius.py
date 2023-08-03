import cv2
import numpy as np

# Load the cropped image
crop = cv2.imread('crop_2.jpg')

# Calculate the dimensions of the cropped image
height, width = crop.shape[:2]

# Calculate the radius of the circle in the cropped image
radius = np.median([height, width]) / 2

print(f"The radius of the circle is approximately {radius} pixels.")