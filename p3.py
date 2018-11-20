matriz = []
numero_filas=3
numero_columnas=3

for i in range(numero_filas):
    fila = int(input("ingrese un numero"))
    
    matriz.append([])

    for j in range(numero_columnas):
        matriz[i].append([])

print(matriz)