import urllib.request
import random

def download_an_image(url):
    name = random.randrange(0,1000)
    full_name = str(name) + '.png'
    urllib.request.urlretrieve(url, full_name)


download_an_image('https://duckduckgo.com/i/33572f85.png')
