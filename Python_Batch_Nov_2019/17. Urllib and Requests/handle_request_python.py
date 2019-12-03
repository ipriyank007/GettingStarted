import requests
# payload = {"q":"python modules", "version":3.8}
# r = requests.get('https://httpbin.org/get', payload)


# print(r.json())

#To get http status code
# print(r.url)

#download image using requests and file handling
# with open('new_image.jpg', 'wb') as img:
#     img.write(r.content)

form = {'name':"Robert", 'age':34}
r = requests.post('https://httpbin.org/post', form)

print(r.json()['form'])

