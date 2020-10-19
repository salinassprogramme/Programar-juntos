#coding:utf8
N=int(input("Introduzca un número entero:"))

def ep(N):
	if N<1:
		return False
	elif N==2:
		return True
	else:
		for i in range(2,N):
			if N%i==0:
				return False
		return True
if ep(N)==True:
	print("El número es primo")
else:
	print("El número no es primo")
if isinstance(N,(int)):
	ep(N)
else:
	raise TypeError ("Un número entero, por favor")


			
