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
print("Cuadrante del punto a: ", a.cuadrantes())
print("Cuadrante del punto c: ", c.cuadrantes())
print("Cuadrante del punto d: ", d.cuadrantes())

#vector
print("Vector entre a y b: ", a.vector(b))
print("Vector entre b y a: ", b.vector(a))

#distancia
print("Distancia entre a y b: ", a.distancia(b))
print("Distancia entre b y a: ", b.distancia(a))

#cual se encuantra mas lejos de d
print("Distancia entre a y d: ", a.distancia(d))
print("Distancia entre b y d: ", b.distancia(d))
print("Distancia entre c y d: ", c.distancia(d))

#crear rectangulo
print("Rectangulo")
r= Rectangulo(a, b)
print("Base: ", r.base())
print("Altura: ", r.altura())
print("Area: ", r.area())

