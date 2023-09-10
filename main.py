from bs4 import BeautifulSoup
import requests

search_filter = input("What product are you searching for?")

url = f"https://intercomp.com.mt/page/1/?post_type=product&s={search_filter}"
webpage = requests.get(url).text
mydoc = BeautifulSoup(webpage, 'html.parser')

item_found ={}

page = mydoc.find('span', class_='page-numbers current')
page_num = int(str(page).split("/")[-2].split("<")[-2][-1])

for webpage in range(1, page_num + 1):
    url = f"https://intercomp.com.mt/page/{webpage}/?post_type=product&s={search_filter}"
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
        price = main_parent.find(class_='woocommerce-Price-amount amount')

        item_found ={'items': item.text, 'price' : price.text, 'link' : link, 'image_link' : image_link}


        print(item_found)