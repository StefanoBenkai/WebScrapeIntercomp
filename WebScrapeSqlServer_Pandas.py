from bs4 import BeautifulSoup
import requests
import pandas as pd
from sqlalchemy import create_engine
import datetime


# DB Parameters
server = 'YARA\MSSQLSERVER01'
database = 'WebScrape'
username = ''
password = ''


connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=SQL+Server'
engine = create_engine(connection_string)
engine = create_engine(connection_string)

search_filter = '16GB'

url = f"https://intercomp.com.mt/page/1/?post_type=product&s={search_filter}"
webpage = requests.get(url).text
mydoc = BeautifulSoup(webpage, 'html.parser')

item_found = []

page = mydoc.find('span', class_='page-numbers current')
page_num = int(str(page).split("/")[-2].split("<")[-2][-1])

for webpage_num in range(1, page_num + 1):
    url = f"https://intercomp.com.mt/page/{webpage_num}/?post_type=product&s={search_filter}"
    webpage = requests.get(url).text
    mydoc = BeautifulSoup(webpage, "html.parser")
    desc = mydoc.find_all(class_='woocommerce-loop-product__title')

    for item in desc:
        parent = item.parent
        if parent.name != 'a':
            continue
        link = parent['href']

        main_parent = parent.parent
        image_link = parent.find(class_='product-thumbnail').find('img')['src']
        price = main_parent.find(class_='woocommerce-Price-amount amount').get_text(strip=True)
        price = float(price[1:].replace(',', ''))

        item_data = {'LaptopID': item.text, 'LaptopURL': link, 'LaptopImageURL': image_link, 'LaptopPrice': price, 'TimestampLoad': datetime.datetime.now()}
        item_found.append(item_data)


df = pd.DataFrame(item_found)

# Insert into SQL Server
df.to_sql('T_LaptopWebScrape', engine, if_exists='append', index=False)
