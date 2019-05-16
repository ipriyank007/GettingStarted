import random
import urllib.request

def download_Web_Image(url):
    name = random.randrange(1,1000)
    full_Name = str(name) + '.jpg'
    urllib.request.urlretrieve(url,full_Name)
    
download_Web_Image("https://pps.whatsapp.net/v/t61.11540-24/42074900_243172199690049_8266225956327260160_n.jpg?oe=5BC74E0C&oh=d24956e2e8cba354ea08a33b4e54313f")
    
    

123 345 743