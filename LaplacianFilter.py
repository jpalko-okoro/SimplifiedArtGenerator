import cv2
import matplotlib.pyplot as plt

# Reference: https://medium.com/@nikatsanka/comparing-edge-detection-methods-638a2919476e

# Open the image
img = cv2.imread('TestPictures/Father-Portrait-Small.png')

# Apply gray scale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply gaussian blur
blur_img = cv2.GaussianBlur(gray_img, (3, 3), 0)

# Positive Laplacian Operator
laplacian = cv2.Laplacian(blur_img, cv2.CV_64F)

# Invert image colors for white background and black lines
inverted_edges = cv2.bitwise_not(laplacian)

plt.figure()
plt.title('father-portrait')
plt.imsave('father-portrait.png', inverted_edges, cmap='gray', format='png')
plt.imshow(inverted_edges, cmap='gray')
plt.show()