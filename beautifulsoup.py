from bs4 import BeautifulSoup
import requests
import urllib.request
import time

sause = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
print('Successful!')

soup = BeautifulSoup(sause, 'lxml')
## print(soup.title.text)

## print(soup.find_all('p'))

for para in soup.find_all('p'):
    ##print(para.text)
    ##print(50 * "*")
    ## time.sleep(2)
    pass

## Finding usls is also easy!!

for i in soup.find_all('a'):
    print(i.get('href'))
