from pixabay_connection import get_images_urls
from download_images import persist_image
from threading import Thread, Lock
import os
import concurrent.futures


def thread_get_images(number_images: int, query: str, local_path: str, workers: int) -> list:

    threads = []
    url = get_images_urls(number_images, query)
    for i in range(number_images):
        t = Thread(target=persist_image, args=(local_path, url[i]))
        threads.append(t)
        t.start()

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        executor.submit(threads)

    # for t in threads:
    #     t.join()


def main():
    local_path = os.path.normpath(join(os.getcwd(), "download"))
    thread_get_images(10, "flower", local_path, 10)


if __name__ == "__main__":
    main()
