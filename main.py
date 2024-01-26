from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
property_page = response.text
soup = BeautifulSoup(property_page, "html.parser")

# prettified_html = soup.prettify()
# print(prettified_html)

property_prices = soup.find_all('span', class_='PropertyCardWrapper__StyledPriceLine')

for price in property_prices:
    price = int(price.get_text().split("+")[0].split("/")[0].split("$")[1].replace(",",""))
    print(price)


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option(name="detach", value=True)
# driver=webdriver.Chrome(options=chrome_options)
#
# driver.get("url")


