import os
import threads_download
from threads_download import thread_get_images

# Choose the number of images to download
number_images = int(input("How many images you want to download? "))

# Choose the content of the images
query = input("What's the subject of your images? ")

# Name the folder where saving the images
folder = input("Insert the name of the folder where you want to save images: ")

# Choose the max number of threads at work
max_workers = int(input("How many threads are working? "))

# Call thread_get_images and start downloading
local_path = os.path.abspath("/" + folder)
thread_get_images(number_images, query, local_path, max_workers)

