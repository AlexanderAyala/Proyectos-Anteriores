lista = [1,3,4,5,7,8,9,2,5,6,4,12,20,3,7,9,0,1,4,3,8]
lista2 = []
lista3 = []
 
for x in lista:
	if x not in lista3:
		lista3.append(x)
	else:
		if x not in lista2:
			lista2.append(x)
print sorted (lista)
print sorted (lista2, reverse = True),