from bs4 import BeautifulSoup
import requests
import mysql.connector
import datetime

# MYSQl Conn Parameters
host = 'localhost'
user = 'root'
password = '****'
database = 'WebScrapeDB'

#
conn = mysql.connector.connect(host=host, user=user, password=password, database=database)

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

        # Insert into MySQL
        cursor = conn.cursor()
        insert_query = "INSERT INTO t_laptopwebscrape (LaptopID, LaptopURL, LaptopImageURL, LaptopPrice, TimestampLoad) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (item.text, link, image_link, price, datetime.datetime.now()))
        conn.commit()

# Close Conn
conn.close()

print('Executed')