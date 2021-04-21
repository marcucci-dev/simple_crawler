import hashlib
import io
import os
import requests
from PIL import Image

from crawler import semaphore


def persist_image(folder_path: str, url: str):

    """
    If the counter is larger than zero, decrement it by one and return True immediately.
    If the counter is zero, block until awoken by a call to release().
    """
    semaphore.pool_sema.acquire()

    try:
        image_content = requests.get(url).content

    except Exception as e:
        print("ERROR - Could not download {} - {}".format(url, e))

    try:
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        file_path = os.path.join(folder_path, hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=85)
        print("SUCCESS - saved {} - as {}".format(url, file_path))
    except Exception as e:
        print("ERROR - Could not download {} - {}".format(url, e))

    semaphore.pool_sema.release()
