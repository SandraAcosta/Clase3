def suma(a,b):
    return a + b
def resta (a,b):
    return a-b
def producto (a,b):
    return a*b
def division (a,b):
    return a/b
def factorial (n):
    temp = 1
    for a in range (1,n+1):
        temp *= a
    return temp
def factorial2 (n):
    if n==0:
        return 1
    return n * factorial2 (n-1)
def fibo (n):
    if n in (1,2):
        return 1
    return fibo(n-1)+fibo(n-2)
def contar_sub(lista):
    if lista==[]:
        return 0
    return len(lista[0])+contar_sub(lista[1:])
def sumar_lista(lista):
    if lista ==[]:
        return 0
    return lista [0] + sumar_lista(lista[1:])
def suma_sublistas(lista):
    if lista ==[]:
        return 0
    return sumar_lista(lista[0])+ suma_sublistas(lista[1:])
                   
    
    



