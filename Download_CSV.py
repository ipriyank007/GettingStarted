'''
Created on Jan 28, 2019

@author: Priyank007
'''
from urllib import request

goog_url = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1546021818&period2=1548700218&interval=1d&events=history&crumb=BvvIIo/X9iP/goog.csv'

def download_historic_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str= str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'C:\myProjects\goog.csv'
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_historic_data(goog_url)
    
    