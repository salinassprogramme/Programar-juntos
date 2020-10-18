# coding: utf8
# programa en python que imprime los números primos entre 2 y N dado por el usuario. 

"""
1. pedir N
2. Verificar si N es primo (si lo es, guardar e imprimir)
	2.1 iniciar la variable k = 2
	2.2 MIENTRAS k < N, REPETIR:
		2.3  obtener el residuo de N/k.
		2.4  si residuo es 0, el número NO es primo. FIN.
		2.5  si residuo no es 0, pasamos al siguiente k
		2.6  regresar a paso 2.3. 
	2.7 Si el programa no terminó en 2.6, es primo.
3. Pasar al siguiente valor (N = N-1)
4. Repetir desde 1 mientras N >= 2. 
"""



N = input("N:")
while N >= 2:
	k = 2
	bandera = 0
	while(k < N):
		if( N % k == 0):
			bandera = 1
			break
		else:
			k = k + 1
	if bandera == 0:
		print "el número " , N, " es primo"
	else:
		print "el número ", N, " NO es primo"
	N=N-1



