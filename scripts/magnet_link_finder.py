from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests
import re
from requests.exceptions import ProxyError
from bs4 import BeautifulSoup as bs
import pyperclip as pc
import time
import main

# Configure Firefox options
options = webdriver.FirefoxOptions()
options.binary_location = r'C:/Program Files/Mozilla Firefox/firefox.exe'  
options.add_argument('--headless')  # Run in headless mode (no GUI)

# Initialize Firefox webdriver without specifying executable_path
driver = webdriver.Firefox(options=options)

# searching for torrent 
def search_torrent(query):
	url = 'https://pirate-proxy.dad/search.php?q='+query+'&all=on&search=Pirate+Search&page=0&orderby='
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64)'}
	try:
		time.sleep(3)
		driver.get(url)
		driver.implicitly_wait(10)
		html_source = driver.page_source
		soup = bs(html_source, 'html.parser')
		
		if(soup.find_all('span', class_="list-item item-name item-title")):
			results = soup.find_all('span', class_="list-item item-name item-title")
			size = soup.find_all('span', class_='list-item item-size')
			magnet_link = search_result(soup, results, size)
			return magnet_link
		else:	
			print("No results were returned. Please refine your search.")
			main.menu()

	except Exception as e:
		print(f"An unexpected error occurred: {e}")

# showing search results
def search_result(soup, results, size):
	links = []
	i = 1
	counter = 0
	# showing the results
	for r,s in zip(results,size):
		if counter < 20:
			print(i,re.sub(r'[\W_]+', ' ', r.text[:49]),s.text.replace("B","B, seedrs-"))
			i += 1
			counter += 1
	# getting the links for the results
	for link in soup.find_all('a'):
		b = link.get('href')
		if re.match("^/description", b):
			full_link = "https://pirate-proxy.dad" + b
			links.append(full_link)
	
	print("Select a torrent: ")
	choice = int(input())
	
	choice_url = links[choice-1]
	magnet_link = getTorrent(choice_url)
	return magnet_link

# getting magnet link
def getTorrent(choice_url):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.2840.71 Safari/539.36'}
	time.sleep(3)
	driver.get(choice_url)
	driver.implicitly_wait(10)
	html_source = driver.page_source
	soup = bs(html_source, 'html.parser')
	desired_label = soup.find('label', id = 'd')
	
	if desired_label:
		magnet=desired_label.find_all('a')
		# finding the magnet link in the webpage
		for link in magnet:
			b=link.get('href')
			if re.match("^magnet:" ,b):
				magnet_link=b
				return magnet_link
				driver.quit()
	else:
		print("No magnet link found")
		driver.quit()
	


