import requests

r = requests.get('https://www.xkcd.com/353')

#para = {'username': 'priyank', 'password': 'password123'}
#r = requests.post('https:/httpbin.org/basic-auth/', data=para)

#print(r.get) #will take in string format)
#print(r.content) #will take in bytes


with open('Python_Comics.png', 'wb') as f:
    f.write(r.content)
# print(r.ok)
# print(r.status_code)
# r_dict = r.json()
# print(r_dict)
#print(r.json())
