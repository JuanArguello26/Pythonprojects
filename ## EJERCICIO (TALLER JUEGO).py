# EJERCICIO (TALLER JUEGO)

numeros = []


for i in range(1, 11):
    numeros.append(i)

print("Imprimiendo cada número:")
i = 0
while i < len(numeros):
    print(numeros[i])
    i += 1


i = 0
while i < len(numeros):
    if numeros[i] % 2 == 0:
        numeros.remove(numeros[i])
    
    else:
        i += 1

print("\nLista resultante sin los números pares:", numeros)

## EJERCICIO 2

colores = ["rojo", "verde", "azul"]

nuevos_colores = ("amarillo", "naranja")


colores.extend(nuevos_colores)


print("\nLista de colores:")
for color in colores:
    print(color)

## EJERCICIO 3: Insert y pop


animales = ["perro", "gato", "pajaro"]


animales.insert(1, "Hamster")


elemento_eliminado = animales.pop()
print("\nElemento eliminado:", elemento_eliminado)


print("Lista de animales resultante:", animales)
