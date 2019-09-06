from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.goodreads.com/book/show/24658.The_Prose_Edda')


soup = BeautifulSoup(r.text, 'lxml')
# reviews = soup.find_all('span', class_="readable")
reviews = soup.find_all('div', class_="reviewText stacked")

for i, review in enumerate(reviews):
    for rvs in review.span.find_all('span', style="display:none"):
        print(i+1, rvs.text)
        print()
