# ez-img-download-script
Simple python script to download images from a gallery with filenames that end in incremental numbers.

## A Little Context
I figured I would post this script on GH in the off-chance somebody comes across it and finds it of use. 
I had the need to download each .png file of an NFT collection from Pinata and found it quite tedious to keep editing the link. If this helps anyone save some time, cool. If not, oh well, at least its stored for my own future use.



## Instructions
This script, unless modified to fit different needs, will only work for image urls ending in "1, 2, 3, etc..."

 - In the for i in range(0, "insert number here"),  replace "insert total number" with the number of images to iterate through.
 - Enter the image url following the syntax of "base_url" + str(number) + "file extension"
 - Set the number in time.sleep() to the number in seconds to delay between each iteration
