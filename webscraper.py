from selenium import webdriver
from bs4 import BeautifulSoup

chrome_options = webdriver.ChromeOptions()
chrome_options.headless = True
chrome = webdriver.Chrome(options=chrome_options)
chrome.get('https://www.zillow.com/homes/standford-ca/sold/')
page = chrome.page_source

page = BeautifulSoup(page, 'html.parser')

links = [a['href'] for a in page.find_all('a', 'list-card-link')]

ids = [l.split('/')[-2].split('_')[0] for l in links]
    

