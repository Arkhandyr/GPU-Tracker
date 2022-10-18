from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

source, items, prices, discounts = [], [], [], []

driver.get("https://www.kabum.com.br/busca/rtx-3060")

products = driver.find_elements(By.CLASS_NAME, 'sc-ff8a9791-7')
print(f'{len(products)} itens encontrados.')

for product in products:
    source = 'Kabum'
    item = product.find_element(By.CLASS_NAME, 'sc-d99ca57-0')
    price = product.find_element(By.CLASS_NAME,  'sc-3b515ca1-2')
    try:
        discount = product.find_element(By.CSS_SELECTOR, 'div.sc-ff8a9791-5 p')
        discounts.append(discount.text)
    except:
        discounts.append(None)
    items.append(item.text)
    prices.append((price.text).replace('.','').replace(',','.'))
    
df = pd.DataFrame({'Produto':items,'Preço':prices, 'Desconto':discounts, 'Loja':source}) 
df.sort_values(by='Preço', key=lambda s: s.str[3:].astype(float))
df.to_csv('products.csv', index=False, encoding='utf-8')