## Working Version to download high Resolution Images
## Author: Mohammed Yusuf Khan

# Import the Dependencies
from selenium import webdriver
import time
import sys

# Main function
def main():
	count = input("Give an approx number of images needed on a scale: (0 - 5) ")
	if int(count) > 5:
		exit()

	all_photos_in_a_list = []
	browser = webdriver.Chrome('chromedriver.exe')
	browser.get('https://unsplash.com/new')
	
	browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(int(count))
	
	all_links = browser.find_elements_by_class_name('_23lr1')
	print(len(all_links))
	print(type(all_links))
	
	for i in all_links:
		print(i.text)
		print(i.get_attribute('href'))
		all_photos_in_a_list.append(i.get_attribute('href'))

	for i in all_photos_in_a_list[:3]:
		browser.get(i)
		browser.find_elements_by_css_selector('#app > div > div:nth-child(5) > div > div:nth-child(1) > div:nth-child(1) > header > div._3-6v7 > div._13Q-._27vvN._2iWc- > a')[0].click()
		print(i)
		print("Downloading")
		time.sleep(2)

	input()


if __name__ == '__main__':
	main()