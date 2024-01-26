from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
property_page = response.text
soup = BeautifulSoup(property_page, "html.parser")

# prettified_html = soup.prettify()
# print(prettified_html)

property_prices_element = soup.find_all('span', class_='PropertyCardWrapper__StyledPriceLine')
property_prices = []

for price in property_prices_element:
    price = int(price.get_text().split("+")[0].split("/")[0].split("$")[1].replace(",",""))
    property_prices.append(price)

property_addr_element = soup.find_all('address', {'data-test': 'property-card-addr'})
property_addrs = []
for addr in property_addr_element:
    property_addrs.append(addr.get_text().strip())

property_anchor_element = soup.find_all('a', {'data-test': 'property-card-link'})
property_links = []
for anchor in property_anchor_element:
    property_links.append(anchor.get("href"))






















# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option(name="detach", value=True)
# driver=webdriver.Chrome(options=chrome_options)
#
# driver.get("url")


