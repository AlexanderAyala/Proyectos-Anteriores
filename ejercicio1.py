lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
par = []
impar = []
 
for x in lista:
	if x % 2 == 0:
		par.append(x)
	else:		
	        impar.append(x)
	        
print (par)
print (impar)