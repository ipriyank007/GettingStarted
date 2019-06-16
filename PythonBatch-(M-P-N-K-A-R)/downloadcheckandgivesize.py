import urllib.request
import os


def download_image(url):
    global file_Name
    file_Name = 'myimage.png'

    urllib.request.urlretrieve(url, file_Name)

download_image('https://duckduckgo.com/i/33572f85.png')

def check_existance(fname):
    if os.path.exists(fname):
        print(os.stat(fname).st_size)

check_existance(file_Name)

