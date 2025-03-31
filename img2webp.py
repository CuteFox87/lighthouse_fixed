# convert all jpg and png images in the images directory to webp format

import os
import glob
from PIL import Image

def convert_images_to_webp(input_dir, output_dir):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Get all jpg and png files in the input directory
    image_files = glob.glob(os.path.join(input_dir, '*.jpg')) + glob.glob(os.path.join(input_dir, '*.png'))

    for image_file in image_files:
        # Open the image file
        with Image.open(image_file) as img:
            # Convert to webp format
            webp_file = os.path.join(output_dir, os.path.basename(image_file).rsplit('.', 1)[0] + '.webp')
            img.save(webp_file, 'WEBP')
            print(f"Converted {image_file} to {webp_file}")

if __name__ == "__main__":
    input_directory = 'images'  # Directory containing jpg and png images
    output_directory = 'images'  # Directory to save converted webp images

    convert_images_to_webp(input_directory, output_directory)