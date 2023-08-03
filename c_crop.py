import cv2
import numpy as np

# Load the image
image = cv2.imread('your_image.png')

# Define a bounding box around the circle you're interested in
# The format is: start y, stop y, start x, stop x
# Replace with appropriate values
bounding_box = np.array([start_y, stop_y, start_x, stop_x]) 

# Crop the image using the bounding box
crop = image[bounding_box[0]:bounding_box[1], bounding_box[2]:bounding_box[3]]

# Save the cropped image
cv2.imwrite('cropped_circle.png', crop)