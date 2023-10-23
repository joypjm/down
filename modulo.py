# Pedimos al usuario que ingrese el dividendo y el divisor
dividendo = int(input("Ingresa el dividendo: "))
divisor = int(input("Ingresa el divisor: "))

# Calculamos el módulo (residuo) de la división
resultado = dividendo % divisor

# Mostramos el resultado
print(f"El módulo de {dividendo} entre {divisor} es igual a: {resultado}")
