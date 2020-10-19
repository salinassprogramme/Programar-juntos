
#coding:utf8

print("Calcular la sumatoria de n hasta k de x")
k=float(input("Introduzca el número de iteraciones:"))
if not isinstance(k, (float)):
	raise TypeError, "Un número, gilipollas"
x=1
suma=0
while x<=k:
	suma=suma+x
	x=x+1
print(suma)

b=float(input("Introduzca otro número:"))
print "Checho es puto"
c=input("Introduzca otro número:")
print "Usted no aprende,¿verdad?"

