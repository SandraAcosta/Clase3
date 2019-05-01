lista = [[25,34,128],[256,77,99],[365,4,128]]
lista1 = lista[0]
lista2 = lista [1]
lista3 = lista [2]
suma1 = lista1[0] + lista1[1] + lista1[2]
suma2 = lista2[0] + lista2[1] + lista2[2]    
suma3 = lista3[0] + lista3[1] + lista3[2]
print suma1 + suma2 + suma3
print suma1
print suma2
print suma3
listafinal= [lista1[0],lista1[1],lista1[2],lista2[0],lista2[1],lista2[2],lista3[0],lista3[1],lista3[2]]
#listafinal.sort()
#listafinal.reverse()
print listafinal
#x = input("ingrese un numero")
#div =[]
#for n in listafinal:
    #if n % x == 0:
#print div
#for o in listafinal:
for o in range(len(listafinal)):
    for j in range (o, len(listafinal)):
        if listafinal [o] < listafinal[j]:
            listafinal[j] 
print listafinal            

    


    


