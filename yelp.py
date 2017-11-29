## Import dependencies

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup, SoupStrainer
import requests
import re
from selenium.webdriver.common.by import By
import subprocess


html=None
link_list = []
for i in range(99):
	print("Page", i)
	url = "https://www.yelp.com/search?find_desc=american&find_loc=San+Francisco,+CA&start=" + str((i * 10))
	print(url)
	for i in range(5):
		try:
			response=requests.get(url, headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
			html=response.content
			break
		except Exception as e:
			print ('failed attempt',i)

	#time.sleep(5)
	soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') #decode html
	#print(soup.encode("utf-8"))

	data = soup.findAll('a', attrs = {'data-analytics-label': 'biz-name'})
	for dataa in data:
		if '/biz/' in dataa['href']:
			link_list.append(dataa['href'])
			print(dataa['href'])


fopen = open('links.txt', 'a+')
for link in link_list:
	fopen.write(link + "\n")
fopen.close()

result = open('result.txt', 'a+')


browser = webdriver.Chrome('chromedriver.exe')




for page in link_list:
	try:
		page_url = 'https://www.yelp.com' + page
		browser.get(page_url)
		name = browser.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]/h1')
		print(name.text.encode('utf-8'))
		result.write(name.text + '\n')
		print(10 * '--')
		result.write('---------------' + '\n')	
		lists = browser.find_elements_by_class_name('ywidget')
		for listing in lists:
			if "More business info" in listing.text:
				print(listing.text)
				result.write(listing.text + '\n')
		result.write('\n')
	except Exception as e:
		print(e)

result.close()