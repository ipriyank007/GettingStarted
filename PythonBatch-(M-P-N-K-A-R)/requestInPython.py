import requests

para = {'username': 'priyank', 'password': 'password123'}
r = requests.post('https:/httpbin.org/basic-auth/', data=para)

# with open('Python_Comics.png', 'wb') as f:
#     f.write(r.content)
# print(r.ok)
# print(r.status_code)
# r_dict = r.json()
# print(r_dict)
print(r.json())
