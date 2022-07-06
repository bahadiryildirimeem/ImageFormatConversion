# Image format conversion
- convert images to any opencv support format (bmp, jpg, png...)<br>
- Put the image to be converted in the input folder (you can put images in any format at the same time)<br>
- The converted image is saved in the output folder

# What's new?
Now this script takes 3 parameters. Image output format, image output name, and output image starting number.

Output image name parameter helps you to don't attempt to rename all of images. All output images name's start with this name.
Output image starting number is the starting index of first output image.

So you can easily reformat and rename your images for the creating datasets.

# Environment
- python 2.7
- opencv

# Run

## convert images format to png
 ` python img2.py png newName 3`

 ## convert images format to bmp
 ` python img2.py bmp newName 3`

 ## convert images format to jpg
 ` python img2.py jpg newName 3`

 ## ...


