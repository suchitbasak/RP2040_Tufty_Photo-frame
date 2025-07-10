# Display photos on a tufty 2040 board
# save photos in the photos_dir folder
# edit them before hand to make sure they are 320x240 pixels in size so that they fit on the screen

import os
import time
import random
from picographics import PicoGraphics, DISPLAY_TUFTY_2040
from jpegdec import JPEG

# function to change the sequence of images
def shuffle_list(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        # Pick a random index from 0 to i
        j = random.randint(0, i)
        # Swap elements
        my_list[i], my_list[j] = my_list[j], my_list[i]
    return(my_list)

# function display images on screen
def show_image(j, filename, duration):
    j.open_file(filename)
    j.decode()
    display.update()
    time.sleep(duration)


# program begins
display = PicoGraphics(display=DISPLAY_TUFTY_2040)
j = JPEG(display)

# extract filenames from the photos_dir folder
# sample filenames = ["photos_dir/a-solo-1.jpg", "photos_dir/a-solo-2.jpg"]

filenames = os.listdir("/photos_dir")

# loop to display images
for i in range(50000): # let the loop run 50000 times
    shuffled_filenames = shuffle_list(filenames)
    for f in shuffled_filenames:
        if f[0] == 'z': # wanted this specific file to apprear for half a second, as a glitch, for fun
            duration=0.5
        else:
            duration=10
            
        show_image(j, "/smaller/"+f, duration=duration)