from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
property_page = response.text
soup = BeautifulSoup(property_page, "html.parser")

# prettified_html = soup.prettify()
# print(prettified_html)

property_prices_element = soup.find_all('span', class_='PropertyCardWrapper__StyledPriceLine')
property_prices = []

for price in property_prices_element:
    price = price.get_text().split("+")[0].split("/")[0].replace(",","")
    property_prices.append(price)

property_addr_element = soup.find_all('address', {'data-test': 'property-card-addr'})
property_addrs = []
for addr in property_addr_element:
    property_addrs.append(addr.get_text().strip())

property_anchor_element = soup.find_all('a', {'data-test': 'property-card-link'})
property_links = []
for anchor in property_anchor_element:
    property_links.append(anchor.get("href"))


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)
driver=webdriver.Chrome(options=chrome_options)

property_details = zip(property_addrs, property_prices, property_links)

for property in property_details:
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeWxsE4Hjn0vMY1e3tkRLoN3IrczUCVCXZxVcJrs-q_W4GKFw/viewform?usp=sf_link")
    time.sleep(0.15)
    addr_field = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    submit_btn = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    # print(property[1])
    addr_field.clear()
    addr_field.send_keys(property[0])
    time.sleep(0.1)
    price_field.clear()
    price_field.send_keys(property[1])
    time.sleep(0.1)
    link_field.clear()
    link_field.send_keys(property[2])
    time.sleep(0.1)
    submit_btn.click()

driver.quit()






