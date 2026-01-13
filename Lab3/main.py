def read_file(filename, mode='full'):
    try:
        if mode == 'full':
            with open(filename, 'r', encoding='utf-8') as file:
                return file.read()

        elif mode == 'line':
            with open(filename, 'r', encoding='utf-8') as file:
                lines = [line.strip() for line in file]
            return "Построчное чтение файла:\n" + "\n".join(f"Строка: {line}" for line in lines)

        else:
            return "Неправильный режим. Доступные варианты: full или line."

    except FileNotFoundError:
        return f"Ошибка: файл '{filename}' не найден."


def append_to_file(filename, text):
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(text + '\n')
        return f"Текст успешно добавлен в файл {filename}."

    except FileNotFoundError as e:
        return f"Произошла ошибка при записи в файл: {e}"



with open('../example.txt', 'w', encoding='utf-8') as f:
    f.write("geraageegrgreevigeiubhn\n")
    f.write("velqivejounvnmtjvnjtmvt\n")
    f.write("getiegiqormkgepmlvrorit\n")



method = input("Выберите режим чтения файла example.txt (full / line): ").strip().lower()
print(read_file('../example.txt', mode=method))



new_text = input("Введите текст для записи в файл user_input.txt: ")
print(append_to_file('user_input.txt', new_text))

# def count_chars(filename):
#     with open("laba3.txt", "r") as file:
#         text = file.read()
#         return("Кол-во символов в файле",len(text))
# def count_lines(filename):
#     with open("laba3.txt", "w") as file:
#         lines = file.readlines()
#         return("Кол-во строк в файле",lines)
# def count_words(filename):
#     with open("laba3.txt", "w") as file:
#         text = file.read()
#         words = text.split()
#         return("Кол-во слов в файле:",len(words))
# print("Введите число,чтобы увидеть  \n"+"1)Количество символов \n"+"2)Количество строк \n"+"3)Количество слов ")
# answ=input("Введите число:")
# if answ=="1":
#     print(count_chars())
# elif answ=="2":
#     print(count_lines())
# elif answ=="3":
#     print(count_words())
# else:
#     print("Некоректное число")