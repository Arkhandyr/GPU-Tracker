from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

sources, items, prices, discounts = [], [], [], []

df = pd.DataFrame({'Produto':items,'Preço':prices, 'Desconto':discounts, 'Loja':source}) 
df.sort_values(by='Preço', key=lambda s: s.str[3:].astype(float))
df.to_csv('products.csv', index=False, encoding='utf-8')

def getKabum():
    driver.get("https://www.kabum.com.br/busca/rtx-3060")
    productsKabum = driver.find_elements(By.CLASS_NAME, 'sc-ff8a9791-7')
    for product in productsKabum:
        source = 'Kabum'
        item = product.find_element(By.CLASS_NAME, 'sc-d99ca57-0')
        price = product.find_element(By.CLASS_NAME,  'sc-3b515ca1-2')
        try:
            discount = product.find_element(By.CSS_SELECTOR, 'div.sc-ff8a9791-5 p')
            discounts.append(discount.text)
        except:
            discounts.append(None)
        sources.append(source)
        items.append(item.text)
        prices.append((price.text).replace('.','').replace(',','.'))

def getPichau():
    driver.get("https://www.pichau.com.br/search?q=rtx%203060&product_category=6459")
    productsPichau = driver.find_elements(By.CLASS_NAME, 'MuiCardContent-root')
    for product in productsPichau:
        source = 'Pichau'
        item = product.find_element(By.CLASS_NAME, 'MuiTypography-root')
        price = product.find_element(By.CLASS_NAME,  'jss204')
        sources.append(source)
        items.append(item.text)
        prices.append((price.text).replace('.','').replace(',','.'))

getKabum()
getPichau()