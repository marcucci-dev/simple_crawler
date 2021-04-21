from crawler.threads_download import thread_get_images
from crawler.pixabay_connection import check_api_key


def main():
    # Warning the user if the api key has not been set
    check_api_key()

    # Choose the number of images to download
    try:
        number_images = int(input("How many images do you want to download? 3 is the minimum. "))
        if number_images < 3:
            print("Value not valid! Quitting ...")
            quit()
    except ValueError:
        print("Value not valid! Quitting ...")
        quit()

    # Choose the content of the images with an appropriate keyword
    key_words = []
    key_word = input("What's the subject of your images? ")
    # Store all keywords in a list
    while key_word != "":
        key_words.append(key_word)
        key_word = input("Other subject? Just press enter to skip. ")

    # Form the query string with all the key words
    query = "+".join(key_words)

    # Choose the max number of threads at work
    try:
        workers = int(input("How many threads are working? 200 is the maximum allowed. "))
        if workers > 200:
            workers = 200
            print("Impossible to select a value higher than 200! The value has been set to 200!")
    except ValueError:
        print("Value not valid! Quitting ...")
        quit()
    # Save the images in downloads folder
    folder = "download"

    # Call thread_get_images and start downloading
    thread_get_images(number_images, query, folder, workers)


# Call the main function
if __name__ == "__main__":
    main()
