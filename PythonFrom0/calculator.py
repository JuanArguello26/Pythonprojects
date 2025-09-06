def sumar(x, y):

    return x + y


def restar(x, y):

    return x - y


def multiplicar(x, y):

    return x * y


def dividir(x, y):

    if y == 0:
        return "Error: No se puede dividir por cero"
    return x / y


def calculadora():

    print("---------------------------------")
    print("   Calculadora Básica en Python  ")
    print("---------------------------------")

    while True:
        print("\nSelecciona la operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")


        opcion = input("Ingresa tu opción (1/2/3/4/5): ")


        if opcion == '5':
            print("\n¡Adiós! ")
            break


        if opcion in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("\n Entrada inválida. Por favor, ingresa solo números.")
                continue


            if opcion == '1':
                print(f"\n✅ Resultado: {num1} + {num2} = {sumar(num1, num2)}")
            elif opcion == '2':
                print(f"\n✅ Resultado: {num1} - {num2} = {restar(num1, num2)}")
            elif opcion == '3':
                print(f"\n✅ Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
            elif opcion == '4':
                print(f"\n✅ Resultado: {num1} / {num2} = {dividir(num1, num2)}")
        else:
            print("\n Opción no válida. Por favor, elige una opción del 1 al 5.")



if __name__ == "__main__":
    calculadora()