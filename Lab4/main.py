import math
import datetime



inp_number = int(input("Введите число, из которого необходимо извлечь квадратный корень: "))
sqr = math.sqrt(inp_number)
print("Квадратный корень:", sqr)

now = datetime.datetime.now()
dat = now.date()
time = now.time()

choice = input("Что Вы хотите узнать: \n"
               "Введите: \n"
               "1 — чтобы узнать время \n"
               "2 — чтобы узнать дату \n"
               "3 — чтобы узнать всё вместе \n")

if choice == "1":
    print("Текущее время:", time)
elif choice == "2":
    print("Текущая дата:", dat)
elif choice == "3":
    print("Дата и время:", now)
else:
    print("Неверный ввод!")




import my_module as m
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
print("Сумма =", m.sm(a, b))



from my_module import mult
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
print("Произведение =", mult(a, b))

from my_package.strings_module import lw
s = input("Введите строку: ")
print("Количество слов:", lw(s))
