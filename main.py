import os
import threads_download
from threads_download import thread_get_images

def main():
    # Choose the number of images to download
    number_images = int(input("How many images you want to download? "))

    # Choose the content of the images with an appropriate keyword
    key_words = []
    key_word = input("What's the subject of your images? ")
    # Store all keywords in a list
    while key_word != "":
        key_words.append(key_word)
        key_word = input("Other? ")
    
    # Form the query string with all the key words
    query = ""
    for i in range(len(key_words)):
        query += key_words[i]
        # Each keyword is joined with "+"
        if i <= len(key_words) - 2:
            query += "+"

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
