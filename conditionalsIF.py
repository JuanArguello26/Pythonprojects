print("Program to evaluate the notes of the students")

notaalumno=input("Enter your note to continue:")

def evaluation(nota):
    valoration="Aprobado"
    if nota < 5:
        valoration = "Reprobado"
    return valoration

print(evaluation(int(notaalumno)))  # we need to use int 'cause the input always throw a string and it can't be combinated with an int




