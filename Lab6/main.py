class UserAccount:
    def __init__(self, username=None, email=None, password=None):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password_to_check):
        return password_to_check == self.__password


password = input()

user1 = UserAccount(username="john", email="", password="")
user1.set_password(password)

check = input()
print(user1.check_password(check))


class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model
    def get_info(self):
        print(self.make,self.model)

class Car(Vehicle):
    def __init__(self, make=None, model=None, fuel_type=None):
        super().__init__(make,model)
        self.fuel_type = fuel_type
    def get_info(self):
        return f"Марка : {self.make} ,Модель : {self.model}; Тип топлива :{self.fuel_type}"
Car1=Car()

print(Car1.get_info())

