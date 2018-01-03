## Author: Mohammed Yusuf Khan
## Import the required dependencies

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup, SoupStrainer
import requests
import re
from selenium.webdriver.common.by import By
import subprocess
import pandas as pd


browser = webdriver.Chrome('chromedriver.exe')

## 3 Links that we selected to scrape as mentioned in the word doc, all can be done as well
links = ['https://academic.oup.com/neuro-oncology/article-abstract/19/suppl_6/vi273/4590533?redirectedFrom=fulltext',
'https://academic.oup.com/neuro-oncology/article-abstract/19/suppl_6/vi272/4590524?redirectedFrom=fulltext',
'https://academic.oup.com/neuro-oncology/article-abstract/19/suppl_6/vi272/4590529?redirectedFrom=fulltext'
]

## Scraping begins from here
content = []
for i in links:
	browser.get(i)
	head_article = browser.find_element_by_css_selector('#ContentColumn > div.content-inner-wrap > div.widget.widget-ArticleTopInfo.widget-instance-OUP_Abstract_ArticleTop_Info_Widget > div > div > h1')
	print(head_article.text)

	# Exrtacting the abstract number from the corpus of text

	regex = head_article.text.split('.')
	print("test result", regex)
	abstract_number = regex[0]
	head_article = regex[1]

	print("abstract number", abstract_number)
	print("head article", head_article)	

	authors = browser.find_element_by_css_selector('#ContentColumn > div.content-inner-wrap > div.widget.widget-ArticleTopInfo.widget-instance-OUP_Abstract_ArticleTop_Info_Widget > div > div > div.wi-authors > div')
	print(authors.text)

	current_url = browser.current_url
	print(browser.current_url)

	abstract = browser.find_element_by_css_selector('#ContentTab > div.widget.widget-ArticleFulltext.widget-instance-OUP_Abstract_Article_FullText_Widget > div > div > section')
	print(abstract.text.encode('utf-8')) # encoding required or else it will throw an error
	
	topics = browser.find_element_by_css_selector('#ContentTab > div.widget.widget-ArticleFulltext.widget-instance-OUP_Abstract_Article_FullText_Widget > div > div > div.article-metadata-panel.clearfix > div.related-topic-tags')
	print(topics.text)

	issue_section = browser.find_element_by_css_selector('#ContentTab > div.widget.widget-ArticleFulltext.widget-instance-OUP_Abstract_Article_FullText_Widget > div > div > div.article-metadata-panel.clearfix > div.article-metadata-tocSections > a')
	print(issue_section.text)
	print("Done")
	
	content.append([abstract_number, head_article, browser.current_url, authors.text, abstract.text.encode('utf-8'), topics.text, issue_section.text])

print(content)
print(len(content))

output = pd.DataFrame(data = content , columns = ['Abstract No.','Title','URL','Authors','Abstract Text','Topic','Issue Section'])

print(output)

## outputing it into an excel file.
output.to_excel('outputfile.xlsx', index = False)