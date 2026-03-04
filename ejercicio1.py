# --- Actividad 1 ---
print("--- Actividad 1 ---")
# Crea una lista con 8 números
numeros = [10, 15, 22, 33, 40, 55, 60, 71]

print("Tus números son:" + str(numeros))

impares = 0

print("Números pares:")

for num in numeros:
   
    if num % 2 == 0:
        print(num)
    else:
        impares += 1

print(f"Cantidad de impares: {impares}")


# --- Actividad 2 ---
print("\n--- Actividad 2 ---")
 
nombres = ["Ana", "Pedro", "Luis", "Juan", "Maria", "Carlos"]
i = 0

while i < len(nombres):
    
    print(nombres[i])
    
    if nombres[i] == "Juan":
        break
    
    i += 1

# --- Actividad 3 ---
print("\n--- Actividad 3 ---")

estudiantes = {
    "Ana": 4.5,
    "Luis": 3.2,
    "Carlos": 2.8,
    "Maria": 4.0
}

reprobados = 0

print("Estudiantes aprobados:")

for nombre, nota in estudiantes.items():
   
    if nota >= 3.0:
        print(f"{nombre}: {nota}")
    else:
       
        reprobados += 1

print(f"Cantidad de reprobados: {reprobados}")


