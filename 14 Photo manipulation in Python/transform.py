from image import Image
import numpy as np

def brighten(image, factor):
    # when we brighten, we just want to make each channel higher by some amount 
    # factor is a value > 0, how much you want to brighten the image by (< 1 = darken, > 1 = brighten)
    image.array = np.clip(image.array * factor, 0, 1)
    return image

def adjust_contrast(image, factor, mid):
    # adjust the contrast by increasing the difference from the user-defined midpoint by factor amount
    image.array = np.clip((image.array - mid) * factor + mid, 0, 1)
    return image

def blur(image, kernel_size):
    # kernel size is the number of pixels to take into account when applying the blur
    # (ie kernel_size = 3 would be neighbors to the left/right, top/bottom, and diagonals)
    # kernel size should always be an *odd* number
    pad = kernel_size // 2
    padded = np.pad(image.array, ((pad, pad), (pad, pad), (0, 0)), mode='edge')
    blurred = np.zeros_like(image.array)
    for y in range(image.y_pixels):
        for x in range(image.x_pixels):
            region = padded[y:y+kernel_size, x:x+kernel_size]
            blurred[y, x] = np.mean(region, axis=(0, 1))
    image.array = blurred
    return image

def apply_kernel(image, kernel):
    # the kernel should be a 2D array that represents the kernel we'll use!
    # for the sake of simiplicity of this implementation, let's assume that the kernel is SQUARE
    # for example the sobel x kernel (detecting horizontal edges) is as follows:
    # [1 0 -1]
    # [2 0 -2]
    # [1 0 -1]
    k_size = kernel.shape[0]
    pad = k_size // 2
    padded = np.pad(image.array, ((pad, pad), (pad, pad), (0, 0)), mode='edge')
    filtered = np.zeros_like(image.array)
    for y in range(image.y_pixels):
        for x in range(image.x_pixels):
            for c in range(image.num_channels):
                region = padded[y:y+k_size, x:x+k_size, c]
                filtered[y, x, c] = np.sum(region * kernel)
    image.array = np.clip(filtered, 0, 1)
    return image

def combine_images(image1, image2):
    # let's combine two images using the squared sum of squares: value = sqrt(value_1**2 + value_2**2)
    # size of image1 and image2 MUST be the same
    if image1.array.shape != image2.array.shape:
        raise ValueError("Images must be the same size to combine")
    combined_array = np.sqrt(np.square(image1.array) + np.square(image2.array))
    combined_array = np.clip(combined_array, 0, 1)
    combined_image = Image(image1.x_pixels, image1.y_pixels, image1.num_channels)
    combined_image.array = combined_array
    return combined_image
    
if __name__ == '__main__':
    lake = Image(filename='lake.png')
    city = Image(filename='city.png')

    # Example usage and testing of the functions
    brightened_lake = brighten(lake, 1.2)
    brightened_lake.write_image('brightened_lake.png')

    contrasted_city = adjust_contrast(city, 1.5, 0.5)
    contrasted_city.write_image('contrasted_city.png')

    blurred_lake = blur(lake, 3)
    blurred_lake.write_image('blurred_lake.png')

    # Sobel X kernel for edge detection
    sobel_x = np.array([[1, 0, -1],
                        [2, 0, -2],
                        [1, 0, -1]])
    edge_city = apply_kernel(city, sobel_x)
    edge_city.write_image('edge_city.png')

    combined_image = combine_images(lake, city)
    combined_image.write_image('combined.png')
