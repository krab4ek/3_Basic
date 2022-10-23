from ast import ExceptHandler


a=b=c=0
print(id(a),id(b),id(c))

d,e = 1,2
print(id(d), id(e))
print(d,e)
d,e = e,d
print(d,e)

print (type(e))
slovo = "Вывод такой вот строки"
print(type(slovo))
fl_e = 5.8
print(type(fl_e))

isMarried = False
print(isMarried)

isAlive = True
print(isAlive)

age = 32
print("Возраст: ", age)
count = 15
print("Колличество: ",count)

a = 0b11
b = 0b1000
c = 0b0011001111
print(a, b, c)

a = 0x0A
b = 0x0F
c = 0xA5
print(a, b, c)

height = 1.67
weight = 89.83
pi = 3.14
print(height, weight, pi)

x = 3.14e4
print(x)

x = 3.14e-4
print(x)

complexNumber = 1+3j
print(complexNumber)

text = ("Я видел чудное мгновенье "
"Перед мной явилась ты")
print(text)

text_mnogo_strok = '''Laudate omnes gentes laudate
Magnificat in secula
Et anima mea laudate
Magnificat in secula'''
print(text_mnogo_strok)

ekran_msg = "\t\"Hello\n\tWorld\""
print(ekran_msg)
path = "C:\python\name.txt"
print(path)
#Экранировали строку
path = r"C:\python\name.txt"
print(path)

userName = "Andrei"
userAge = 32
msg = f"name: {userName}, age: {userAge}"
print(msg)

h_w = "Hello World"
h_w1 = "HELLO WORLD"
h_p = "Hello Python"

print(h_w, end=" ")
print(h_w1, end=" and ")
print(h_p, end="")

input_name = input("\nВведите Ваше имя: ")
print(f"Ваше имя: {input_name}")
input_lastName = input("Введите Вашу фамилию: ")
print (f"Ваша фамилия {input_lastName}")
input_age = input("Введите ваш возраст: ")
print(f"Ваш возраст: {input_age}")
print(f"Тип переменной input_name: {type(input_name)}", end=", ")
print(f"Тип переменной input_lastName: {type(input_lastName)}", end=", ")
print(f"Тип переменной input_age: {type(input_age)}", end="\n")
