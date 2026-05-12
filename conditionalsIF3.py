#age=100

#if age>0 and age<=100:
    #print("Correct age")
#else:
    #print("Incorrect age")

salario_presidente=int(input("enter the salario presidente: "))
print("Salario presidente: ", salario_presidente)

salario_director=int(input("enter the salario director: "))
print("Salario director: ", salario_director)

salario_jefedearea=int(input("enter the salario jefe de area: "))
print("Salario jefe de area: ", salario_jefedearea)

salario_administrativo=int(input("enter the salario administrativo: "))
print("Salario administrativo: ", salario_administrativo)

if salario_administrativo < salario_jefedearea < salario_director < salario_presidente:
    print("Todo funciona correctamente")

else:
    print("Algo falla en la nómina")