import urllib.request

# mypage = urllib.request.urlopen('https://www.google.com')
# print(mypage.read())


url = 'https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.mnn.com%2Fassets%2Fimages%2F2016%2F02%2Fangry-cat.jpg.838x0_q80.jpg&f=1'
filename = 'D:/cat.jpg'
urllib.request.urlretrieve(url, filename)
urllib.request.urlopen()