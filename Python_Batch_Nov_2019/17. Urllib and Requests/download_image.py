from urllib import request
from random import randint

source = 'https://i.ytimg.com/vi/pY_9y7QKoVg/maxresdefault.jpg'

def download_image(url):
    image_name = input('Enter image name')
    file_name = image_name + '.jpg'
    request.urlretrieve(url, file_name)

download_image(source)





