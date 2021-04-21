from threads_download import thread_get_images
from pixabay_connection import check_api_key


def main():
    # Warning the user if the api key has not been set
    check_api_key()

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

    # Choose the max number of threads at work
    workers = int(input("How many threads are working? "))
    if workers > 200:
        workers = 200
        print("Impossible to select a value higher than 200")

    # Save the images in downloads folder
    folder = "download"
    
    # Call thread_get_images and start downloading
    thread_get_images(number_images, query, folder, workers)


# Call the main function
if __name__ == "__main__":
    main()
