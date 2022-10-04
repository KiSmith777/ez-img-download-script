# Save this .py file to the same directory you'd like to download the images to
# Once saved, open a command prompt and type: python3 EzImg.py

import requests # to get image from the web
import shutil # to save it locally
import time # to set a time delay if there is a rate limit for retrieving content

## Set up the image URL and filename
number = 0
while (number < "insert total number"): 
  # set the image url with the following syntax: "base url" + str(number) + "file extension"
    image_url = "https://example.com/gallery/picture-" + str(number) + ".png" 
    filename = image_url.split("/")[-1]

    # Open the image url, set stream = true to return the image.
    r = requests.get(image_url, stream = True)

    # Check to verify image successfully received
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
    
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
        
        print('Image sucessfully Downloaded: ',filename)
      
    else:
        print('Image Couldn\'t be retreived')

    # increment number each iteration
    number = number + 1
    # sets the number in time.sleep() in seconds to set the delay between each iteration
    time.sleep(5)
