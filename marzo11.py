def puede_multiplicarse(filas1, cols1, filas2, cols2):
    return cols1 == filas2

def multiplicar_matrices(matriz1, matriz2):
    filas1 = len(matriz1)
    cols1 = len(matriz1[0])
    filas2 = len(matriz2)
    cols2 = len(matriz2[0])
    
    resultado = [[0 for _ in range(cols2)] for _ in range(filas1)]
    
    for i in range(filas1):
        for j in range(cols2):
            for k in range(cols1):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    
    return resultado

# Solicitar dimensiones
print("=== Multiplicación de Matrices ===")
filas1 = int(input("Ingrese número de filas de la matriz 1: "))
cols1 = int(input("Ingrese número de columnas de la matriz 1: "))
filas2 = int(input("Ingrese número de filas de la matriz 2: "))
cols2 = int(input("Ingrese número de columnas de la matriz 2: "))

# Verificar si se pueden multiplicar
if not puede_multiplicarse(filas1, cols1, filas2, cols2):
    print(f"Error: No se puede multiplicar. Las columnas de la matriz 1 ({cols1}) deben ser iguales a las filas de la matriz 2 ({filas2})")
else:
    # Ingresar datos matriz 1
    print("\nIngrese los elementos de la matriz 1:")
    matriz1 = []
    for i in range(filas1):
        fila = []
        for j in range(cols1):
            valor = float(input(f"Elemento [{i}][{j}]: "))
            fila.append(valor)
        matriz1.append(fila)
    
    # Ingresar datos matriz 2
    print("\nIngrese los elementos de la matriz 2:")
    matriz2 = []
    for i in range(filas2):
        fila = []
        for j in range(cols2):
            valor = float(input(f"Elemento [{i}][{j}]: "))
            fila.append(valor)
        matriz2.append(fila)
    
    # Multiplicar y mostrar resultado
    resultado = multiplicar_matrices(matriz1, matriz2)
    print("\n=== Resultado ===")
    for fila in resultado:
        print(fila)