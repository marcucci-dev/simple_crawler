import os
import threads_download
from threads_download import thread_get_images

def main():
    # Choose the number of images to download
    number_images = int(input("How many images you want to download? "))

    # Choose the content of the images
    query = input("What's the subject of your images? ")

    # Name the folder where saving the images
    folder = input("Insert the name of the folder where you want to save images: ")

    # Choose the max number of threads at work
    workers = int(input("How many threads are working? "))
    if workers > 200:
        workers = 200
        print("Impossible to select a value higher than 200")

    # Call thread_get_images and start downloading
    local_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), folder)
    thread_get_images(number_images, query, local_path, workers)

# Call the main function
if __name__ == "__main__":
    main()
