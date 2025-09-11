num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

if num1>num2:
    print(f"The number {num1} is greater than the number {num2}")
else:
    print(f"The number {num2} is greater than the number {num1}")

n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))

def retMax(n1,n2):
    if n1 < n2:
        print(n2)
    elif n2 < n1:
        print(n1)
    else:
        print("Son iguales")

print("the greater number is: ")

retMax(n1,n2)





