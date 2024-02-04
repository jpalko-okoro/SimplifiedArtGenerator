from PIL import ImageFilter

SHOW_TRACE_LOGS = true

# Pass the grayscale image in for this first pass of filtering
def image_filtering_pass_1(image):
    # Make sure image is grayscale without alpha values
    if image.mode in ('L', 'LA', 'P', 'I'):
        filtered_image = image
    else:
        filtered_image = image.convert('LA')

    width, height = filtered_image.size

    grayscale_values = []

    for y in range(height):
        for x in range(width):
            pixel_value = filtered_image.getpixel((x, y))

            # If the filtered_image is in LA format, the pixel value is a tuple otherwise it is a single integer
            if isinstance(pixel_value, int):
                grayscale_values.append(pixel_value)
            else:
                # If the filtered_image is in 'LA' mode, extract the luminance value (luminance, alpha)
                grayscale_values.append(pixel_value[0])

        
    if (SHOW_TRACE_LOGS):
        print("Width of image:", filtered_image.width)
        print("Height of image:", filtered_image.   height)
        pixel_num = width * height
        print("All pixel grayscale values:", grayscale_values[:pixel_num])

    # Adaptive thresholding over the pixels
    difference_threshold = 10

    # Averaging out the image to make more consistent values (0 has no affect)
    local_average = filtered_image.filter(ImageFilter.BoxBlur(0))

    # TODO: Fix this filtering to actually use the querieid grayscale values and a windowed based average for them or something
    filtered_image = filtered_image.point(
        lambda x, local_avg=local_average: 0
        if x > local_avg.getpixel((x % width, y % height))[0] else 255)

    # Read out the value of each pixel from 0 to 255 for grayscale
    return filtered_image
