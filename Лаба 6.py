class UserAccount:
    def __init__(self, username, email, password):
            self.username = username
            self.email = email
            self.__password = password 

    def set_password(self, new_password):
            self.__password = new_password
            return("Пароль успешно изменен.")

    def check_password(self, password):
        if self.__password == password:
            return('yes')
        else:
            return('no')


username = input('введите имя:')
email = input('введите почту:')
password = input('введите пароль:')
user = UserAccount(username,email, password)
user.check_password(password)
new_password = input('введите новый пароль:')
user.set_password(new_password)
user.check_password(new_password)

class Vehicle:
    def __init__(self, mark, model):
        self.mark = mark
        self.model = model
    def get_info(self):
        return f"Марка: {self.mark}, Модель: {self.model}"
class Car(Vehicle):
    def __init__(self, mark, model, fuel_type):
        super().__init__(mark, model)
        self.fuel_type = fuel_type 

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Тип топлива: {self.fuel_type}"

if __name__ == "__main__":
    my_car = Car("Toyota", "Camry", "Бензин")
    print(my_car.get_info())
