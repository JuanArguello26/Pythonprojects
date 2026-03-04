mydiccionario = {"Colombia":"Bogotá", "Francia": "París", "Canadá":"Otawa", "Ecuador":"Guayaquil"}

mydiccionario["Venezuela"]="Perú" # add a element in my diccionary

print(mydiccionario)

mydiccionario["Venezuela"]="Caracas" # use this to correct a mistake or something similar

print(mydiccionario.get("Colombia")) # or print(mydiccionario["Colombia"]) // to print a specific date

print(mydiccionario) # to print all my diccionary

del mydiccionario["Venezuela"] # use this to delete a data from the diccionary

print(mydiccionario)

my2diccionary={23:"Juan", "Nombre":"Esteban", "Equipo":"Colombia", "Aguacate":{"Temporadas":[1992,1993,1999,2000]}}

print(my2diccionary) # If i wanna search a specific data, we could use ["Aguacate"]

print(my2diccionary.keys()) # print the keys

print(my2diccionary.values()) # print the values of my diccionary

print(len(my2diccionary)) #the number of values in my diccionary





