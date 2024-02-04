import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2

# Reference: https://medium.com/@nikatsanka/comparing-edge-detection-methods-638a2919476e

def rgbSobelFilter(img):
    # Sobel Operator
    h, w, d = img.shape

    # define filters
    horizontal = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])  # s2
    vertical = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])  # s1

    # define images with 0s
    newgradientImage = np.zeros((h, w, d))

    # offset by 1
    for channel in range(d):
        for i in range(1, h - 1):
            for j in range(1, w - 1):
                print(f"Working in channel {channel} in {d} for pixel {i} & {j} out of {h} & {w}")
                # Gx = [1 0 -1; 2 0 -2; 1 0 -1]
                # Gy = [1 2 1; 0 0 0; -1 -2 -1]
                horizontalGrad = (horizontal[0, 0] * img[i - 1, j - 1, channel]) + \
                                (horizontal[0, 1] * img[i - 1, j, channel]) + \
                                (horizontal[0, 2] * img[i - 1, j + 1, channel]) + \
                                (horizontal[1, 0] * img[i, j - 1, channel]) + \
                                (horizontal[1, 1] * img[i, j, channel]) + \
                                (horizontal[1, 2] * img[i, j + 1, channel]) + \
                                (horizontal[2, 0] * img[i + 1, j - 1, channel]) + \
                                (horizontal[2, 1] * img[i + 1, j, channel]) + \
                                (horizontal[2, 2] * img[i + 1, j + 1, channel])

                verticalGrad = (vertical[0, 0] * img[i - 1, j - 1, channel]) + \
                            (vertical[0, 1] * img[i - 1, j, channel]) + \
                            (vertical[0, 2] * img[i - 1, j + 1, channel]) + \
                            (vertical[1, 0] * img[i, j - 1, channel]) + \
                            (vertical[1, 1] * img[i, j, channel]) + \
                            (vertical[1, 2] * img[i, j + 1, channel]) + \
                            (vertical[2, 0] * img[i + 1, j - 1, channel]) + \
                            (vertical[2, 1] * img[i + 1, j, channel]) + \
                            (vertical[2, 2] * img[i + 1, j + 1, channel])

                # Edge Magnitude
                mag = np.sqrt(pow(horizontalGrad, 2.0) + pow(verticalGrad, 2.0))
                # Avoid underflow: clip result
                newgradientImage[i - 1, j - 1, channel] = mag

    # now add the images r g and b
    rgb_edge = newgradientImage[:,:,0] + newgradientImage[:,:,1] + newgradientImage[:,:,2]

    # Invert image colors for white background and black lines
    # inverted_edges = cv2.bitwise_not(rgb_edge)
    # return inverted_edges
    return rgb_edge

def graySobelFilter(img):
    # Apply gray scale
    gray_img = np.round(0.299 * img[:, :, 0] +
                        0.587 * img[:, :, 1] +
                        0.114 * img[:, :, 2]).astype(np.uint8)

    # Sobel Operator
    h, w = gray_img.shape
    # define filters
    horizontal = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])  # s2
    vertical = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])  # s1

    # define images with 0s
    newhorizontalImage = np.zeros((h, w))
    newverticalImage = np.zeros((h, w))
    newgradientImage = np.zeros((h, w))

    # offset by 1
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            print(f"Working for pixel {i} & {j} out of {h} & {w}")
            horizontalGrad = (horizontal[0, 0] * gray_img[i - 1, j - 1]) + \
                            (horizontal[0, 1] * gray_img[i - 1, j]) + \
                            (horizontal[0, 2] * gray_img[i - 1, j + 1]) + \
                            (horizontal[1, 0] * gray_img[i, j - 1]) + \
                            (horizontal[1, 1] * gray_img[i, j]) + \
                            (horizontal[1, 2] * gray_img[i, j + 1]) + \
                            (horizontal[2, 0] * gray_img[i + 1, j - 1]) + \
                            (horizontal[2, 1] * gray_img[i + 1, j]) + \
                            (horizontal[2, 2] * gray_img[i + 1, j + 1])

            newhorizontalImage[i - 1, j - 1] = abs(horizontalGrad)

            verticalGrad = (vertical[0, 0] * gray_img[i - 1, j - 1]) + \
                        (vertical[0, 1] * gray_img[i - 1, j]) + \
                        (vertical[0, 2] * gray_img[i - 1, j + 1]) + \
                        (vertical[1, 0] * gray_img[i, j - 1]) + \
                        (vertical[1, 1] * gray_img[i, j]) + \
                        (vertical[1, 2] * gray_img[i, j + 1]) + \
                        (vertical[2, 0] * gray_img[i + 1, j - 1]) + \
                        (vertical[2, 1] * gray_img[i + 1, j]) + \
                        (vertical[2, 2] * gray_img[i + 1, j + 1])

            newverticalImage[i - 1, j - 1] = abs(verticalGrad)

            # Edge Magnitude
            mag = np.sqrt(pow(horizontalGrad, 2.0) + pow(verticalGrad, 2.0))
            newgradientImage[i - 1, j - 1] = mag

    # Invert image colors for white background and black lines
    inverted_edges = cv2.bitwise_not(newgradientImage)
    return inverted_edges

if __name__ == "__main__":
    # Open the image
    img = np.array(Image.open('TestPictures/Father-Portrait-Small.png')).astype(np.uint8)
    rgbSobel_inverted_edges = rgbSobelFilter(img)
    # graySobel_inverted_edges = graySobelFilter(img)

    # plt.figure()
    # plt.title('father-portrait-sobel-gray.png')
    # plt.imsave('father-portrait-sobel-gray.png', graySobel_inverted_edges, cmap='gray', format='png')
    # plt.imshow(graySobel_inverted_edges, cmap='gray')
    # plt.show()

    plt.figure()
    plt.title('father-portrait-sobel-rgb.png')
    plt.imsave('father-portrait-sobel-rgb.png', rgbSobel_inverted_edges, cmap='gray', format='png')
    plt.imshow(rgbSobel_inverted_edges, cmap='gray')
    plt.show()