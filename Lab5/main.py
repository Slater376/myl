
class Book:
        def __init__(self, title=None, author=None, year=None):
            self.title = title
            self.author = author
            self.year = year
        def get_info(self):
            return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"


class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self,new_radius):
        self.radius = new_radius

title = input()
author = input()
year=int(input())
book1=Book(title, author, year)
print(book1.get_info())

circle1=Circle(5)
new_r = int(input())
circle1.set_radius(new_r)
print(circle1.get_radius())