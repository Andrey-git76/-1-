class Book: 
    def __init__(self, title, author, year): 
        self.title = title 
        self.author = author 
        self.year = year
    def get_info(self):
        return f"{self.title};{self.author}; {self.year}"
book = Book("Тарас Бульба", "Николай Гоголь", 1835)
print(book.get_info())


class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self, new_radius):
        self.radius = new_radius
circle = Circle(7)
print("Радиус = ", circle.get_radius())
circle.set_radius(15) 
print("Изменённый радиус = ", circle.get_radius())
