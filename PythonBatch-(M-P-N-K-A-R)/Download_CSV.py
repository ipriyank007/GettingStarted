'''
Created on Jan 28, 2019

@author: Priyank007
'''
from os import getcwd
from urllib import request

sample_url = 'https://www.sample-videos.com/csv/Sample-Spreadsheet-5000-rows.csv'

def download_historic_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str= str(csv)
    lines = csv_str.split("\\n")
    dest_url = getcwd()
    print(getcwd())
    dest_url += r'\RobotSample.csv'
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_historic_data(sample_url)
    
    