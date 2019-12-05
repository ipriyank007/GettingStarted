import requests
import time
import concurrent.futures

img_urls = [
    'https://images.unsplash.com/photo-1574735102003-9d7f2f6daa4b',
    'https://images.unsplash.com/photo-1573905891290-b8e0b2d56224',
    'https://images.unsplash.com/photo-1574950225749-647a2e190c09',
    'https://images.unsplash.com/photo-1574873231362-5523c575101e',
    'https://images.unsplash.com/photo-1574950578143-858c6fc58922',
    'https://images.unsplash.com/photo-1574738887531-2fd79e647fdf',
    'https://images.unsplash.com/photo-1574090062401-8e15b1775220',
    'https://images.unsplash.com/photo-1573554394544-930a4cf6fc66',
    'https://images.unsplash.com/photo-1573380499247-58e22435fcfb',
    'https://images.unsplash.com/photo-1571847490051-491c12ff6540',
]

t1 = time.perf_counter()

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3][0:15] + '.jpg'
    with open(img_name, 'wb') as f:
        f.write(img_bytes)
        return f'{img_name} downloaded!'

with concurrent.futures.ThreadPoolExecutor() as executor:
    # executor.map(download_image, img_urls)
    results = [executor.submit(download_image, img_url) for img_url in img_urls]
    
    for f in concurrent.futures.as_completed(results):
        print(f.result())

t2 = time.perf_counter()

print(f'Process took {t2-t1} sec(s)')