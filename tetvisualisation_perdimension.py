
#TET visualisation as per dimension: navigating ot emotion_good, emotion_bad and painint


import glob
import json
from PIL import Image 
import io
import base64

def extract_png(data,png_number):
    photo_list = []
    count=0
    for i in data:
        if 'png' in i:
            if count in range(png_number,27,7):
                photo_list.append(i['png'].split(',')[-1])
            count+=1
    return photo_list



if __name__ == "__main__":
    
    data_txt_paths = []

    # Iterate over the directories
    for directory in glob.glob('CRPS_preprocesising_experimental/Input_and_output_folders/jatos_results_data_20240405112333/*'):
        # Search for data.txt files within each directory
        data_txt_files = glob.glob(f"{directory}/comp-result_*/data.txt")
        # Add the paths to data.txt files to the list
        data_txt_paths.extend(data_txt_files)
    
    emotion_bad_photo_all_sessions = []
    for pth in data_txt_paths:
        data = json.load(open(pth))
        emotion_bad_photo_conditions_list = extract_png(data,3)
        emotion_bad_photo_all_sessions.extend(emotion_bad_photo_conditions_list)
    
    import base64
from PIL import Image
from io import BytesIO

# List of 80 base64 strings
base64_strings = emotion_bad_photo_all_sessions  # Your list of base64 strings goes here

# Split the list into groups of four
groups_of_four = [base64_strings[i:i+4] for i in range(0, len(base64_strings), 4)]

# Iterate over each group
for i, group in enumerate(groups_of_four):
    # List to store images in the group
    images = []
    
    # Iterate over each image in the group
    for base64_string in group:
        try:
            # Decode the base64 string to get the image data
            image_data = base64.b64decode(base64_string)
            # Open the image using PIL
            image = Image.open(BytesIO(image_data))
            # Append the image to the list
            images.append(image)
        except Exception as e:
            print(f"Error processing base64 string: {e}")
    
    # Calculate the total width and height of all images in the group
    total_width = sum(image.width for image in images)
    max_height = max(image.height for image in images)
    
    # Create a new blank image to hold the group of images
    new_image = Image.new('RGB', (total_width, max_height))
    
    # Paste each image onto the new image
    x_offset = 0
    for image in images:
        new_image.paste(image, (x_offset, 0))
        x_offset += image.width
    
    import os

    '''# Save the new image
    new_image.save(os.path.join(f"group_{i+1}.png"))'''

  # Save the new image
    new_image.save(os.path.join("/Users/rk354/Desktop/CRPS_preprocesising_experimental/Input_and_output_folders/P13_TET_visualisation", f"group_{i+1}.png"))
    

