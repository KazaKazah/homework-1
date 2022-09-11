import requests
# # Задача 1:
# С помощью библиотеки ‘requests’ написать логику для - загрузки изображения с сайта


# s = requests.Session() 
# s.headers.update({
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9;'
#     })

# def load_user_data(user_id, page, session):
#     url = '...' % (user_id, page)
#     request = session.get(url)
#     return request.text

# def contain_movies_data(text):
#     soup = BeautifulSoup(text)
#     film_list = soup.find('div', {'class': 'profileFilmsList'})
#     return film_list is not None

# page = 1
# while True:
#     data = load_user_data(user_id, page, s)
#     if contain_movies_data(data):
#         with open('./page_%d.html' % (page), 'w') as output_file:
#             output_file.write(data.encode('cp1251'))
#             page += 1
#     else:
#             break


# # Задача 2:
# С помощью библиотеки ‘requests’ написать логику для – формирования текстового файла с ссылки https://jsonplaceholder.typicode.com/photos

# payload = {'key1': 'value1', 'key2': 'value2'}  
# r = requests.get('https://jsonplaceholder.typicode.com/photos', params=payload)
# print(r.url) 


# # Задача 3:
# Из второго задания – циклом пройти по полученным данным и загрузить все фото в одном папку.
