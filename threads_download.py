from pixabay_connection import get_images_urls
from download_images import persist_image
from threading import Thread, Lock
import concurrent.futures


def thread_get_images(nums: int, local_path: str) -> list:

    threads = []
    url = get_images_urls(number_images=nums)
    for i in range(nums):
        t = Thread(target=persist_image, args=(local_path, url[i]))
        threads.append(t)
        t.start()

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.submit(threads)

    # for t in threads:
    #     t.join()


def main():
    path = r".\saved"
    thread_get_images(10, path)


if __name__ == "__main__":
    main()
