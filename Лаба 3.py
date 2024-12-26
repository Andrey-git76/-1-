## Задание №1
a = input('Choose 1 or 2: ')
print(a)
if int(a)==1:
    f=open(r"example.txt").read()
    print (f)
else:
    f=open(r"example.txt").readlines ()
    print (f)
## Задание №2
us = input()
with open("user_input.txt","a") as file:
    file.writelines(f"{us} \n")

with open("user_input.txt","r") as file:
    cont = file.read()
print(cont)

## Задание №3
fn = input("Enter file name: ")
try: 
    with open(fn, "r") as file:
        cont = file.read()
except FileNotFoundError:
    print("File not found, try again")
    exit()
print(cont)

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Название:{self.title},Автор :{self.author},Год выпуска:{self.year}"

title, author, year = input().strip(), input().strip(), int(input().strip()) 
book = Book(title, author, year) 
print(book) 
