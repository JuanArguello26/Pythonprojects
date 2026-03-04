## EJERCICIO 4

numeros = [1, 5, 8, 3, 5, 9, 5, 2]
numero_ingresado = int(input("Ingresa un número para contar cuántas veces aparece: "))
contador = 0

for num in numeros:
    if num == numero_ingresado:
        contador += 1

print("El número aparece", contador, "veces en la lista.")

## EJERCICIO 5

lista1 = [10, 20, 30, 40, 50]
lista2 = [30, 40, 50, 60, 70]
lista_combinada = []

for num in lista1:
    if num not in lista_combinada:
        lista_combinada.append(num)

for num in lista2:
    if num not in lista_combinada:
        lista_combinada.append(num)

lista_combinada.sort()
print("Lista combinada ordenada:", lista_combinada)

## EJERCICIO 6

dias_semana = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")
dia_ingresado = input("Ingresa un día de la semana: ").lower()

if dia_ingresado in dias_semana:
    print("Es un día válido")
else:
    print("Día inválido")

## EJERCICIO 7

frutas = ["manzana", "banana", "naranja", "uva"]
fruta_ingresada = input("Ingresa el nombre de una fruta: ")

for i in range(len(frutas)):
    if frutas[i] == fruta_ingresada:
        frutas[i] = "kiwi"

print(frutas)

## EJERCICIO 8

listaA = [1, 2, 3, 4, 5]
listaB = [4, 5, 6, 7, 8]
lista_comun = []

for num in listaA:
    if num in listaB:
        if num not in lista_comun:
            lista_comun.append(num)

print(lista_comun)

## EJERCICIO 9

precios = [10.5, 20.0, 15.5, 5.0]
total = 0

for precio in precios:
    total += precio

print(total)

## EJERCICIO 10

vocales = ("a", "e", "i", "o", "u")
lista_vocales = list(vocales)
lista_vocales.append("y")

print(lista_vocales)

## EJERCICIO 11

edades = [15, 22, 12, 18, 30, 17, 45, 16]

i = 0
while i < len(edades):
    if edades[i] < 18:
        edades.remove(edades[i])
    else:
        i += 1

print(edades)

## EJERCICIO 12

palabras = ["python", "es", "genial", "aprender"]
palabras_invertidas = []

for i in range(len(palabras) - 1, -1, -1):
    palabras_invertidas.append(palabras[i])

print(palabras_invertidas)

