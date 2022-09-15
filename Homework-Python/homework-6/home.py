# # Задача 1:
# «Спарсить» данные с любого валютного сайта. Использовать библиотеку bs4.

import requests
from bs4 import BeautifulSoup


# url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

# for n, i in enumerate(items, start=1):
#     itemName = i.find('h4', class_='card-title').text.strip()
#     itemPrice = i.find('h5').text
#     print(f'{n}:  {itemPrice} за {itemName}')

# pages = soup.find('ul', class_='pagination')
# urls = []
# links = pages.find_all('a', class_='page-link')

# for link in links:
#     pageNum = int(link.text) if link.text.isdigit() else None
#     if pageNum != None:
#         hrefval = link.get('href')
#         urls.append(hrefval)

# for slug in urls:
#     newUrl = url.replace('?page=1', slug)
#     response = requests.get(newUrl)
#     soup = BeautifulSoup(response.text, 'lxml')
#     items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
#     for n, i in enumerate(items, start=n):
#         itemName = i.find('h4', class_='card-title').text.strip()
#         itemPrice = i.find('h5').text
#         print(f'{n}:  {itemPrice} за {itemName}')

# # Задача 2:
# Написать программу, которая будет циклом загружать картинки с любого сайта.



# p = requests.get(img)
# out = open("...\img.jpg", "wb")
# out.write(p.content)
# out.close()

# # Задача 3:
# Найти бесплатный api погоды и получить данные с него в консоль.
