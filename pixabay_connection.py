import requests

from config import api_key

# example:
# https://pixabay.com/api/?key=XXX&q=yellow+flowers&image_type=photo&pretty=true


def get_images_urls(number_images=20, query=None, images_per_page=20):  # , page=1, per_page=20):
    request_string = "https://pixabay.com/api/?key="+api_key+"&q=yellow+flowers&image_type=photo&pretty=true"
    request_string += "&per_page="+str(images_per_page)
    print(request_string)
    r = requests.get(request_string)
    print(r)
    # print(r.json())
    json_response = r.json()
    print("r.status_code", r.status_code)
    print("r.status_code type", type(r.status_code))
    
    images_urls = []
    if r.status_code == 200:  # 200: OK
        print("OK")
        
        for i in range(images_per_page):# range(json_response["totalHits"]):
            print("i: ", i)
            print(json_response["hits"][i]["tags"])
            
            images_urls.append(json_response["hits"][i]["largeImageURL"])
            
        # print(r.text)
        # print(r.json())
        #print(r.json()["total"])
        #print(r.json()["totalHits"])
        #print(r.json()["hits"])
        #print(r.json()["hits"][0])  # dizionario!
        #print(r.json()["hits"][0]["pageURL"])
        ## largeImageURL or webformatURL
        #print(r.json()["hits"][0]["largeImageURL"])
        
    return images_urls

# "total": 4692,
#	"totalHits": 500,
#	"hits": [

def main():

    print("Result: ", get_images_urls(images_per_page=30))
    
    
    
if __name__ == "__main__":
    main()