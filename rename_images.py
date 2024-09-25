import os

def rename_images_in_folder(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Filter the list to only include image files
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
    images = [f for f in files if os.path.splitext(f)[1].lower() in image_extensions]

    # Rename each image file
    for index, image in enumerate(images, start=1):
        # Get the file extension
        extension = os.path.splitext(image)[1]
        # Create new filename
        new_name = f"image{index}{extension}"
        # Get the full path for both the old and new names
        old_path = os.path.join(folder_path, image)
        new_path = os.path.join(folder_path, new_name)
        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {old_path} -> {new_path}")

# Specify the path to the folder where the images are stored
folder_path = '/Users/luciarebolino/Desktop/DecodingChristmas/DecodingChristmasWeb/images/wreath'

rename_images_in_folder(folder_path)
