numero = int(input("Introduce un número entero: "))

for triangulo in range(1, numero+1):
    
    filas = [str(x) for x in range(2*triangulo - 1, 0, -2)]
    
    print(" ".join(filas))