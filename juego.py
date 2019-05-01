import random 
def aleatorio(x):
    lista = []
    for a in range (x):
        lista.append(random.randint(1,100))
    return lista
def num_veces(lista):      
    return len (lista)*2
     
def num_lista(lista, valor):
    return valor in lista

def jugar(n):
    lista = aleatorio(n)
    print lista
    for i in range(num_veces(lista)):
        numero = input("ingrese un numero")
        if num_lista(lista, numero):
            return "gano"
    return "perdiste"
    

        
