import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.goodreads.com/book/show/325779.Next_of_Kin').text
soup = BeautifulSoup(r, 'lxml')

# summary = soup.find('span', id="freeText9906280155399248377")
# print(summary)

title = soup.find('h1', itemprop="name")
print(title.text.strip())