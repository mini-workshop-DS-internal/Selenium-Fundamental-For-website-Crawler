from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import re

driver = webdriver.Chrome("PATH/chromedriver") # your absolute path chromedriver don't forget adjust with your chrome display version
driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("corona" + Keys.RETURN)
time.sleep(5)
#print(driver.page_source)
soup = BeautifulSoup(driver.page_source, 'lxml')
raw = soup.findAll('h3')

headline = []
link_ = []
for line in raw:
	link = str(line.find_parent('a'))
	url = re.findall(r'(https?://\S+)',link)
	print(url)
	try:
		driver.get(url[0].replace('"',''))
	except:
		continue

driver.close()
