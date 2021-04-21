from threading import Thread
import os
from time import time
from threading import BoundedSemaphore

from crawler.pixabay_connection import get_images_urls
from crawler.download_images import persist_image
from crawler import semaphore


def thread_get_images(number_images: int, query: str, local_path: str, workers: int) -> list:

    begin = time()

    # initializes the semaphore with the max number of concurrent threads
    semaphore.pool_sema = BoundedSemaphore(value=workers)

    threads = []
    urls = get_images_urls(number_images, query)

    for i in range(len(urls)):
        t = Thread(target=persist_image, args=(local_path, urls[i]))
        threads.append(t)
        t.start()

    # Another alternative implementation to the semaphore:
    # with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
    #    {executor.submit(persist_image, local_path, url_): url_ for url_ in urls}

    for t in threads:
        t.join()

    print("Downloaded images: {}/{} ".format(len(urls), number_images))

    end = time()
    print("Elapsed time: ", end - begin)


def main():
    local_path = os.path.normpath(os.path.join(os.getcwd(), "../download"))
    thread_get_images(10, "flower", local_path, 10)


if __name__ == "__main__":
    main()
