#1st Exercise
mymessage="Hello World"

print(mymessage)

#2nd Exercise

name="Juan"
age= 25

print(f"Hola, {name}, tienes {age} años.")

#3rd Exercise

def greetings(name):
    print(f"Hello, {name}")
greetings("Juan")

#4th Exercise

def sumar(num1, num2):
    return num1 + num2

resultado= sumar(2, 5)
print(resultado)

#5th Exercise

mylist=["Movie 1", "Movie 2", "Movie 3", "Movie 4"]
print(mylist[2])

mylist.append("Movie 5")
print(mylist)

#6th Exercise
mi_informacion = {
    "nombre": "Carlos",
    "edad": 25,
    "ciudad": "Pereira"
}

print("Edad inicial:")
print(mi_informacion["edad"])

mi_informacion["profesión"] = "Estudiante"


mi_informacion["ciudad"] = "Bogotá"

#
print("\nDiccionario actualizado:")
print(mi_informacion)

#7th Exercise

age_str=input("Enter your age: ")
edad= int(age_str)

if edad>18:
    print("\nYou are old enough")
else:
    print("\nYou are young")

#Exercise 8
password= "Juan"
passworduser=input("Enter your password: ")

if  password == passworduser:
    print("\nYou are okay")
else:
    print("\nYou are not okay")













