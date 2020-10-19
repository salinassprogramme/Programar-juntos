#coding:utf8
N=int(input("Introduzca un número entero:"))
bandera=0
if (N<1):
	bandera=1
elif (N==2):
	bandera=0
else:
	for i in range(2,N):
		if (N%i==0):
			bandera=1
if bandera==0:
	print ("El número sí es primo")
else:
	print ("El número no es primo")

