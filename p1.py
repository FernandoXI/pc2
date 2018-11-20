import math
x = int(input("ingrese un numero"))
y = int(input("ingrese otro numero"))

cuadrados= (x*x + y*y)
distancia = math.sqrt(cuadrados)
print("la distancia al (0,0) es: ", distancia, "desde",(x,y) )