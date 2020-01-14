import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw   
from PIL import Image, ImageDraw
         

def watermark_one_image(original_image):
    print("what watermaerk do you want?")
    imput = input(" ")
    """ 
    takes an image and pastes a wateramrk and custom text
    left some random bits of code dont know what they do but it dosent
    work if comented out or erased
    """
    
    if original_image == '0crest.png':
        original_image = original_image.resize((50,50))
    else:
        original_image = original_image.resize((300,300))
        draw = ImageDraw.Draw(original_image)
        draw.text((0, 250),imput, fill=255)
        del draw
        original_image = original_image.paste(img)  
    
    width, height = original_image.size
    
    
    
    
    #start with transparent mask 
    #not sure what this does dont remove it doe
    rounded_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,255))
    
    
    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask
    
    
    # Uncomment the following line to show the mask
    #plt.imshow(rounded_mask)
    
    
    
    # Make the new image, starting with all transparent
    #another instance of nessesary but wierd code
    result = PIL.Image.new('RGBA', original_image.size, (0,0,0,0))
    result.paste(original_image, (0,0), mask=rounded_mask)
    return result
    
def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    taken from original file
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list

def watermark_all(directory=None):
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have the watermarks added 
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    # Load all the images
    image_list, file_list = get_images(directory)  

    # Go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        print (n)
        filename, filetype = os.path.splitext(file_list[n])
        
        # adds watermarks
        curr_image = image_list[n]
        new_image = watermark_one_image(curr_image) 
        
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)   
