# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

while True:
    print"Selecione una opcion"
    print"0- Registrar direccion donde se ecuentre el archivo"
    print"1- Lista de Vegetales y Frutas"
    print"2- Votos de una Fruta o Vegetal"
    print"3- Cantidad total Votos"
    print"4- Estadisticas"
    print"5- Salir"
    
    select = int(raw_input("Ingrese opcion: "))
    
    if select == 0:
		direct= raw_input("Ingrese la direccion donde se encuentra el archivo .txt: ")
		print "\n"
    
    elif select ==1:
        print "\nLa lista de frutas y vegetales es la siguiente: "
        print "\n-Aguacate      -Pepinos\n-Fresas        -Rabano\n-Kiwi          -Tomates\n-Frijoles      -Brocoli\n-Lechuga       -Sandia\n-Papas\n"
        nextt = raw_input("Presione ENTER para continuar.....")
        print "\n"
    
    elif select==2:
        vegetal = raw_input("Ingrese la fruta o vegetal: ")
        def count_votes(vegetal):
            print ("\nNumero de votos para "+vegetal+ "...")
            count = 0
            for line in open(direct):
		line = line.strip()
		nombre, voto = line.split(" - ")
		if voto == vegetal:
			count = count + 1
	    return count
        print (count_votes(vegetal)), "\n"
        
    elif select==3:
        print "\n", "a- Numero de votos"
        print "b- Numero total de votos"
        opc = str(raw_input("Elija entre las opciones: "))
        if opc == 'a':
            def count2(vegetal):
                    count = 0
                    for line in open(direct):
                            line = line.strip()
                            nombre, voto = line.split(" - ")
                            if voto == vegetal:
                                    count = count + 1
                    return count
            suma = count2("Aguacate") + count2("Papas") + count2("Kiwi") + count2("Pepinos") + count2("Fresas") + count2("Rabano") + count2("Tomates") + count2("Frijoles") + count2("Brocoli") + count2("Lechuga") + count2("Sandia")
	    print "\n","El numero de Votos es: " , suma, "\n"
        elif opc == 'b':
            lineas = len(open(direct).readlines())
            print "\n","El numero total de votos es:", lineas, "\n"
    
    elif select==4:
		      

        N = 11
        print "\n","Preparando estadisticas......" , "\n"		
        menMeans = (72, 55, 72, 54, 63, 72, 76, 61, 55, 55, 64) 
        menStd =  (8)
        ind = np.arange(N)  
        width = 0.35       
        fig, ax = plt.subplots()
        colors = ['green','red','green','brown', 'green','brown','green','purple','red','green','green']
        rects1 = ax.bar(ind, menMeans, width, color=colors, yerr=menStd)

        ax.set_ylabel('Resultados')
        ax.set_title('Estadisticas de la Encuesta sobre Frutas y Vegetales')
        ax.set_xticks(ind + width)
        ax.set_xticklabels(('Aguacate', 'Fresas', 'Kiwi', 'Frijoles', 'Lechuga','Papas','Pepinos','Rabano','Tomates','Brocoli', 'Sandia'))
        
        def autolabel(rects):
            
            for rect in rects:
                height = rect.get_height()
                ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                        '%d' % int(height),
                        ha='center', va='bottom')
                
                
        autolabel(rects1)
        plt.show()
        nextt = raw_input("Presione ENTER para continuar....."), 
        print "\n"
        
    elif select==5:
        break
    else:
        print ("\nla opcion Solicitada no esta en el menu \n")
