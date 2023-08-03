import cv2
import numpy as np

# Load the image
image = cv2.imread(r'C:\Users\BLACK\Desktop\BLACK\Python\Circle\1.jpg')

# ------- Image filtering starts from here -------

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply low-pass filter (Gaussian blur)
low_pass = cv2.GaussianBlur(gray, (9,9), 2)

# Subtract low-pass filtered image from the original image to get the high-pass filtered image
# high_pass = cv2.subtract(gray, low_pass)

# #  normalized filter
# high_pass_normalized = cv2.normalize(high_pass, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# blurred = cv2.medianBlur(high_pass_normalized, 3)

# ------- Canny edge here -------
edges = cv2.Canny(low_pass, 50, 150)

# cv2.imshow("output", edges)
# cv2.waitKey(0)

# ------- Houghs starts from here -------
detected_circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 28, param1=20, param2=40, minRadius=22, maxRadius=90)

# Check if any circles were found
if detected_circles is not None:
  detected_circles = np.uint16(np.around(detected_circles)) 
  
  for pt in detected_circles[0, :]: 
    a, b, r = pt[0], pt[1], pt[2] 
  
    cv2.circle(image, (a, b), r, (0, 255, 0), 2) 
    cv2.circle(image, (a, b), 1, (0, 0, 255), 3)

# Display the image with the detected circles
cv2.imshow("output", image)
cv2.waitKey(0)

num_pipes = len(detected_circles[0])
print('Number of pipes detected:', num_pipes)