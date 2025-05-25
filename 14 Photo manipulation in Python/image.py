
import numpy as np
from PIL import Image as PILImage
import os

class Image:
    def __init__(self, x_pixels=0, y_pixels=0, num_channels=0, filename=''):
        self.input_path = 'input/'
        self.output_path = 'output/'

        os.makedirs(self.input_path, exist_ok=True)
        os.makedirs(self.output_path, exist_ok=True)

        if filename:
            self.array = self.read_image(filename)
            self.y_pixels, self.x_pixels, self.num_channels = self.array.shape
        elif x_pixels and y_pixels and num_channels:
            self.x_pixels = x_pixels
            self.y_pixels = y_pixels
            self.num_channels = num_channels
            self.array = np.zeros((y_pixels, x_pixels, num_channels), dtype=np.float32)
        else:
            raise ValueError("You must provide either dimensions or a filename")

    def read_image(self, filename, gamma=2.2):
        image = PILImage.open(self.input_path + filename).convert('RGB')
        image_np = np.asarray(image).astype(np.float32) / 255.0
        image_np = np.power(image_np, gamma)
        return image_np

    def write_image(self, output_file_name, gamma=2.2):
        im = np.clip(self.array, 0, 1)
        im_gamma = np.power(im, 1 / gamma)
        im_uint8 = (im_gamma * 255).astype(np.uint8)
        output_image = PILImage.fromarray(im_uint8)
        output_image.save(self.output_path + output_file_name)
        print(f"Image saved: {self.output_path + output_file_name}")

if __name__ == '__main__':
    im = Image(filename='lake.png')  # Put lake.png inside the input/ folder
    im.write_image('test.png')       # It will save to output/test.png
