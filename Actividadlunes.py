# ============================================================
# Actividad 1: Lista de 8 números, pares e impares
# ============================================================
print("=" * 50)
print("ACTIVIDAD 1 - Números pares e impares")
print("=" * 50)

numeros = [12, 7, 24, 3, 18, 5, 30, 11]
impares = 0

print(f"\nLista de números: {numeros}\n")

for num in numeros:
    if num % 2 == 0:
        print(f"  {num} es PAR")
    else:
        impares += 1

print(f"\nCantidad de números impares: {impares}")


# ============================================================
# Actividad 2: Lista de nombres con while y parada en "Juan"
# ============================================================
print("\n" + "=" * 50)
print("ACTIVIDAD 2 - Nombres con while")
print("=" * 50)

nombres = ["Ana", "Pedro", "Luisa", "Juan", "Carlos", "Maria"]
i = 0

print(f"\nLista de nombres: {nombres}\n")

while i < len(nombres):
    print(f"  -> {nombres[i]}")
    if nombres[i] == "Juan":
        print("\n  ¡Se encontró a Juan! Deteniendo el ciclo...")
        break
    i += 1


# ============================================================
# Actividad 3: Diccionario de estudiantes y notas
# ============================================================
print("\n" + "=" * 50)
print("ACTIVIDAD 3 - Estudiantes y notas")
print("=" * 50)

estudiantes = {
    "Ana": 4.5,
    "Luis": 3.2,
    "Carlos": 2.8,
    "Maria": 4.0
}

reprobados = 0

print("\nEstudiantes que aprobaron (nota >= 3.0):\n")

for nombre, nota in estudiantes.items():
    if nota >= 3.0:
        print(f"  {nombre}: {nota}")
    else:
        reprobados += 1

print(f"\nCantidad de estudiantes reprobados: {reprobados}")

