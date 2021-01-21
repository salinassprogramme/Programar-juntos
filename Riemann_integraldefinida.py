#coding:utf8

def derecha():
    n=0
    for i in range(1,100000,1):
        x=((i/50000)/((i/50000)+1))*(1/50000)
        n+=x
    print(f'La suma de Riemann por la derecha da {n}')
    return(True)    

def izquierda():
    n=0
    for i in range(0,99,1):
        x=((i/50)/((i/50)+1))*(1/50)
        n+=x
    print(f'La suma de Riemann por la izquierda da {n}')
    return(True)  

def main():
    a=derecha()
    if a==True:
        izquierda()
    else:
        print('Error ejecutando el programa, contacte al programador para arreglarlo')

if __name__=='__main__':
    main()