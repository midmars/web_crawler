#coding=utf-8
from selenium import selenium
from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import requests
import re
import time
from bs4 import BeautifulSoup

browser = webdriver.Firefox()
browser.get('https://statementdog.com/analysis/tpe/2330#2330')
soup = BeautifulSoup(browser.page_source)
#soup.select('li .news.new-no-cmmt p a b')
for ele in soup.select('.news-title b'):
	print ele.text
browser.close()