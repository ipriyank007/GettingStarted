from bs4 import BeautifulSoup

with open('index.html', 'r') as html:
    soup = BeautifulSoup(html, 'lxml')

# print(soup)
# print(soup.prettify)

# match = soup.find('div', class_='article')
# print(match.p.text)

matches = soup.find_all('div', class_='article')
for match in matches:
    print(match.h2.a['href'])