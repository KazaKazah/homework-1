# #Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса: название модели, год выпуска, производителя,
# объем двигателя, цвет машины, цену. Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

class Car:

    wheels = 4
    doors = 4
    motor = 1

    def __init__(self, model, year, proiz, obem, color, price):
        self._model = model
        self._year = year
        self._proiz = proiz
        self._obem = obem
        self._color = color
        self._price = price

    def showDescription(self):
        print("This car is a", self.get_model(), self.year,
              self.proiz, self.obem, self.color, self.price)

    def get_model(self):
        return self._model

    def set_model(self, value):
        self._model = value


c = Car('sedan', '2021', 'Toytoa', '2.4', 'black', '4000000')
# print(c.model)
print(c.year)
print(c.proiz)
print(c.obem)
print(c.color)
print(c.price)
c.set_model("BMW")


