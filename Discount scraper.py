from bs4 import BeautifulSoup
import requests
import re
#This function takes the url and gets the html content and then passes it to beautifulsoup
def get_soup(url):
    page = requests.get(url)
    return BeautifulSoup(page.text, 'html.parser') #will return the soup object

#gets the price from the between the tag strong, within the function get_soup
def get_price(url):
    price_tag = get_soup(url).find_all('strong')
    prices = []
    for text in price_tag:
        price = text.text
        numbers = re.findall(r'^£\d+', price)  #This finds the text beginning with £ and containing integers

        if len(numbers) == 1: # checks the length of numbers, the text we want is a value == 1
            prices.append(numbers[0])

    for price in prices:
        return prices

url = f'https://www.cotswoldoutdoor.com/p/patagonia-womens-down-sweater-hooded-jacket-B11ABB0139.html?colour=161'
get_price(url)

def get_discount():
    original_price, discount_price = get_price(url)
    original_price_without_pound = int(original_price.replace('£',''))
    discount_price_without_pound = int(discount_price.replace('£',''))
    total_discount = original_price_without_pound - discount_price_without_pound
    return print(f'The original price was, {original_price}, with the discount it is now, {discount_price}, you have saved, £{total_discount}.')
get_discount()


