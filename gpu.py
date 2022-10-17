from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

products=[]
prices=[]
driver.get("https://www.kabum.com.br/busca/rtx-3060")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('div',href=True, attrs={'class':'sc-ff8a9791-7 dZlrn productCard'}):
    name=a.find('span', attrs={'class':'sc-d99ca57-0 iRparH sc-ff8a9791-16 kRYNji nameCard'})
    price=a.find('span', attrs={'class':'sc-3b515ca1-2 jTvomc priceCard'})
    products.append(name.text)
    prices.append(price.text)
    
print('completed')
df = pd.DataFrame({'Produto':products,'Preço':prices}) 
df.to_csv('produtos.csv', index=False, encoding='utf-8')