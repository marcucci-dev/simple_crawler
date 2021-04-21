import requests

from config import api_key

# example:
# https://pixabay.com/api/?key=XXX&q=yellow+flowers&image_type=photo&pretty=true


def get_images_urls(number_images=20, query='yellow+flowers'):

    if number_images >= 200:
        images_per_page = 200
    elif number_images >= 3:  # min is 3
        images_per_page = number_images
    else:
        return []
    page = 1  # at the moment

    request_string = "https://pixabay.com/api/?key={}".format(api_key)
    request_string += "&q={}".format(query)
    request_string += "&image_type=photo"
    request_string += "&pretty=true"
    request_string += "&page={}".format(page)
    request_string += "&per_page={}".format(images_per_page)

    r = requests.get(request_string)
    json_response = r.json()
    print("r.status_code", r.status_code)

    images_urls = []
    if r.status_code == 200:  # 200: OK

        for index, item in enumerate(json_response["hits"]):
            # print("index:", index)
            # print("item:",  item)
            images_urls.append(json_response["hits"][index]["largeImageURL"])

        # print(r.json()["total"])
        # print(r.json()["totalHits"])
        # print("TOT :", print(r.json()["totalHits"]))
    return images_urls


def main():

    print("Result: ", get_images_urls(number_images=10))
    

if __name__ == "__main__":
    main()
