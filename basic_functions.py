def dividir(dividendo, divisor):
    """Divide dos números manejando división por cero.
    
    Args:
        dividendo: Número a dividir
        divisor: Número divisor
    
    Returns:
        float: Resultado de la división o mensaje de error
    """
    if divisor == 0:
        return "Error: división por cero"
    return dividendo / divisor


def mayor(a, b):
    """Retorna el número mayor entre dos valores.
    
    Args:
        a: Primer número
        b: Segundo número
    
    Returns:
        El número mayor (si son iguales, retorna cualquiera)
    """
    if a >= b:
        return a
    return b


def clasificar(numero):
    """Clasifica un número como positivo, negativo o cero.
    
    Args:
        numero: Número a clasificar
    
    Returns:
        str: "positivo", "negativo" o "cero"
    """
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "cero"


def validar_password(password):
    """Valida que una contraseña cumpla los requisitos.
    
    Args:
        password: Contraseña a validar
    
    Returns:
        bool: True si es válida (mínimo 8 caracteres y no vacía)
    """
    if not password:
        return False
    return len(password) >= 8


def retirar(saldo, monto):
    """Permite retirar dinero del cajero.
    
    Args:
        saldo: Saldo actual disponible
        monto: Monto a retirar
    
    Returns:
        float: Saldo restante o mensaje de error
    """
    if monto <= 0:
        return "Monto inválido"
    if monto > saldo:
        return "Fondos insuficientes"
    return saldo - monto


if __name__ == "__main__":
    print("=== Ejercicio 1: División segura ===")
    print(f"10 / 2 = {dividir(10, 2)}")
    print(f"-10 / 2 = {dividir(-10, 2)}")
    print(f"10 / 0 = {dividir(10, 0)}")

    print("\n=== Ejercicio 2: Número mayor ===")
    print(f"mayor(5, 3) = {mayor(5, 3)}")
    print(f"mayor(-2, -5) = {mayor(-2, -5)}")
    print(f"mayor(4, 4) = {mayor(4, 4)}")

    print("\n=== Ejercicio 3: Clasificación de número ===")
    print(f"clasificar(5) = {clasificar(5)}")
    print(f"clasificar(-3) = {clasificar(-3)}")
    print(f"clasificar(0) = {clasificar(0)}")

    print("\n=== Ejercicio 4: Validar contraseña ===")
    print(f"validar_password('abc12345') = {validar_password('abc12345')}")
    print(f"validar_password('abc1234') = {validar_password('abc1234')}")
    print(f"validar_password('') = {validar_password('')}")

    print("\n=== Ejercicio 5: Cajero automático ===")
    print(f"retirar(1000, 300) = {retirar(1000, 300)}")
    print(f"retirar(500, 600) = {retirar(500, 600)}")
    print(f"retirar(500, -10) = {retirar(500, -10)}")
    print(f"retirar(500, 0) = {retirar(500, 0)}")
    print(f"retirar(500, 500) = {retirar(500, 500)}")