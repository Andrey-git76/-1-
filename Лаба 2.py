##Лабораторка №2
def greet(name, msg=" Доброе утро!"):
    print("Привет ," + name + "." + msg)
greet("Andrey")

def square(number):
    print(number*2)
square(5)

def max_of_two(num1, num2):
    return max(num1, num2)
num1 = int(input())
num2 = int(input())
print(max_of_two(num1, num2))


def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

describe_person(age=18, name="Andrey", city="Moscow")




def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d  <= a and a % d != 0:
        d += 2
    return d * d > a

print(is_prime(int(input("Введите число:")))) 
