# #Задание 2
# Реализуйте класс «Книга». Необходимо хранить в полях класса: название книги, год выпуска, издателя, жанр, автора, цену.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

class Book:
    def __init__(self, name, year, isda, genre, auth, price):
        self.name = name
        self.year = year
        self.isda = isda
        self.genre = genre
        self.auth = auth
        self.price = price
    
    def to_dict(self):
        dictionary = {
            "name":self.name,
            "year":self.year,
            "isda":self.isda,
            "genre":self.genre,
            "auth":self.auth,
            "price":self.price
        }
        return dictionary


