from punto import Punto
from rectangulo import Rectangulo

a= Punto(1, 2)
b= Punto(5, 5)
c= Punto(-3, -1)
d= Punto(0, 0)

#coordenadas
print("Coordenadas del punto a: ", a)
print("Coordenadas del punto b: ", b)
print("Coordenadas del punto c: ", c)   
print("Coordenadas del punto d: ", d)
 #cuadrantes
print("Cuadrante del punto a: ", Punto.cuadrantes(a))
print("Cuadrante del punto c: ", Punto.cuadrantes(c))
print("Cuadrante del punto d: ", Punto.cuadrantes(d))

#vector
print("Vector entre a y b: ", Punto.vector(a,b))
print("Vector entre b y a: ", Punto.vector(a,b))

#distancia
print("Distancia entre a y b: ", Punto.distancia(b,a))
print("Distancia entre b y a: ", Punto.distancia(a,b))

#cual se encuantra mas lejos de d
print("Distancia entre a y d: ", Punto.distancia(d,a))
print("Distancia entre b y d: ", Punto.distancia(d,b))
print("Distancia entre c y d: ", Punto.distancia(d,c))

#crear rectangulo
print("Rectangulo")
r= Rectangulo(a, b)
print("Base: ", Rectangulo.base(r))
print("Altura: ", Rectangulo.altura(r))
print("Area: ", Rectangulo.area(r))

