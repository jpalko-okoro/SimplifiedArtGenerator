import cv2
import matplotlib.pyplot as plt

# Reference: https://medium.com/@nikatsanka/comparing-edge-detection-methods-638a2919476e

# Open the image
img = cv2.imread('TestPictures/Father-Portrait-Small.png')

# Apply Canny
edges = cv2.Canny(img, 100, 200, 3, L2gradient=True)

# Invert image colors for white background and black lines
inverted_edges = cv2.bitwise_not(edges)

plt.figure()
plt.title('father-portrait')
plt.imsave('father-portrait-canny.png', inverted_edges, cmap='gray', format='png')
plt.imshow(inverted_edges, cmap='gray')
plt.show()