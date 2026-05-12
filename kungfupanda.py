import pandas as pd

# Crear una Series con temperaturas de la semana
temperaturas = pd.Series(
    [21, 22, 23, 24, 20, 19, 18],
    index=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
)

# Mostrar toda la serie
print("Temperaturas de la semana:")
print(temperaturas)

# Mostrar temperatura de un día
print("\nTemperatura del miércoles:")
print(temperaturas["Miércoles"])

# Calcular promedio
print("\nPromedio de temperatura:")
print(temperaturas.mean())

# Mostrar temperatura máxima
print("\nTemperatura máxima:")
print(temperaturas.max())

# Filtrar temperaturas mayores a 22
print("\nTemperaturas mayores a 22:")
print(temperaturas[temperaturas > 22])