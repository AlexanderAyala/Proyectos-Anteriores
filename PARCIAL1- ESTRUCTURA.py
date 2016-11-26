# -*- coding: utf-8 -*-
productos={
0:{'Dulces':[0.05,"bolsa",30]},
1:{'Pan':[0.15,"unidad",50]},
2:{'Leche':[2.50,"galon",10]},
3:{'Queso':[3.0,"libra",10]},
4:{'Frijol':[0.78,"libra",200]},
5:{'Arroz':[0.40,"libra",100]},
6:{'Cereal':[3.40,"caja",100]},
7:{'Jabon':[0.80,"unidad",30]},
8:{'Embutidos':[1.20,"Libra",55]}}

def buscar():
    valor = raw_input("buscar:")
    for k1 in productos.keys():
        for k, v in productos[k1].iteritems():
            if k == valor:
                print k
                print "precio:",v[0]
                print "pos:" ,v[1]
                print "Existencias",v[2]

while True:
    print"1- Modificar Producto"
    print"2- Eliminar Producto"
    print"3- Buscar Producto"
    print"4- Vender Producto"
    print"5- Consulta de Productos disponibles"
    print"6- Salir"
    
    opciones = int(raw_input("Ingrese opcion: "))
    
    if opciones ==1:
        
        insertar = int(raw_input("ingrese el ID del producto que desea modificar: "))
        
        if insertar == 0:
            descr = str(raw_input("Ingrese descripcion: "))
            precio = float(raw_input("Ingrese precio: "))
            exist = int(raw_input("Ingrese cantidad exitencias: "))     
            for k1 in productos.keys():
                for k, v in productos[k1].iteritems():
                    if k == descr:
                        productos[insertar]= {k:[precio,v[1],v[2]+exist]}
        
        elif insertar == 1:
            descr = str(raw_input("Ingrese descripcion: "))
            precio = float(raw_input("Ingrese precio: "))
            exist = int(raw_input("Ingrese cantidad exitencias: "))     
            for k1 in productos.keys():
                for k, v in productos[k1].iteritems():
                    if k == descr:
                        productos[insertar]= {k:[precio,v[1],v[2]+exist]}
                        
        elif insertar == 2:
            descr = str(raw_input("Ingrese descripcion: "))
            precio = float(raw_input("Ingrese precio: "))
            exist = int(raw_input("Ingrese cantidad exitencias: "))     
            for k1 in productos.keys():
                for k, v in productos[k1].iteritems():
                    if k == descr:
                        productos[insertar]= {k:[precio,v[1],v[2]+exist]}
        
        elif insertar == 3:
            descr = str(raw_input("Ingrese descripcion: "))
            precio = float(raw_input("Ingrese precio: "))
            exist = int(raw_input("Ingrese cantidad exitencias: "))     
            for k1 in productos.keys():
                for k, v in productos[k1].iteritems():
                    if k == descr:
                        productos[insertar]= {k:[precio,v[1],v[2]+exist]}
        
        elif insertar == 4:
            descr = str(raw_input("Ingrese descripcion: "))
            precio = float(raw_input("Ingrese precio: "))
            exist = int(raw_input("Ingrese cantidad exitencias: "))     
            for k1 in productos.keys():
                for k, v in productos[k1].iteritems():
                    if k == descr:
                        productos[insertar]= {k:[precio,v[1],v[2]+exist]}
        
        elif insertar == 5:
            descr = str(raw_input("Ingrese descripcion: "))
            precio = float(raw_input("Ingrese precio: "))
            exist = int(raw_input("Ingrese cantidad exitencias: "))     
            for k1 in productos.keys():
                for k, v in productos[k1].iteritems():
                    if k == descr:
                        productos[insertar]= {k:[precio,v[1],v[2]+exist]}
        
        elif insertar == 6:
            descr = str(raw_input("Ingrese descripcion: "))
            precio = float(raw_input("Ingrese precio: "))
            exist = int(raw_input("Ingrese cantidad exitencias: "))     
            for k1 in productos.keys():
                for k, v in productos[k1].iteritems():
                    if k == descr:
                        productos[insertar]= {k:[precio,v[1],v[2]+exist]}
        
        elif insertar == 7:
            descr = str(raw_input("Ingrese descripcion: "))
            precio = float(raw_input("Ingrese precio: "))
            exist = int(raw_input("Ingrese cantidad exitencias: "))     
            for k1 in productos.keys():
                for k, v in productos[k1].iteritems():
                    if k == descr:
                        productos[insertar]= {k:[precio,v[1],v[2]+exist]}
                        
        elif insertar == 8:
            descr = str(raw_input("Ingrese descripcion: "))
            precio = float(raw_input("Ingrese precio: "))
            exist = int(raw_input("Ingrese cantidad exitencias: "))     
            for k1 in productos.keys():
                for k, v in productos[k1].iteritems():
                    if k == descr:
                        productos[insertar]= {k:[precio,v[1],v[2]+exist]}
        else:
            modificar = int(raw_input("ingrese el id del producto que desea modificar: "))
            descr = str(raw_input("ingrese nueva descripcion: "))
            precio = float(raw_input("ingrese nuevo precio: "))
            pres = str(raw_input("ingrese nueva presentacion : "))
            exist = int(raw_input("ingrese nueva cantidad exitencias: "))
        
            productos[modificar]= {descr:[precio,pres,exist]}
            
            
        
        
    elif opciones == 2:
        print ""
        try:
            eliminar = int(raw_input("ingrese el id del producto que desea eliminar: "))
        except:
            print "El tipo de dato ingresado es invalido"
            
        del productos[eliminar]
        
        
        
    elif opciones==3:
        buscar()
            
    elif opciones==4:
        print productos
        
        Ide = int(raw_input("introduzca ID del producto a vender:"))
        valor = raw_input("introduzca descr del producto a vender:")
        cant = int(raw_input("introduzca cantidad a vender:"))
        for k1 in productos.keys():
            for k, v in productos[k1].iteritems():
                if k == valor:                    
                    productos[Ide] = {k:[v[0],v[1],v[2]-cant]}                                    
                       
    elif opciones == 5:
        print productos   
        salir = raw_input("PRESIONE ENTER PARA VOLVER AL MENU")
        print "\n"
        
        
    elif opciones == 6:
        break
    else:
        print ("La opcion ingresada no esta en el menu intente e nuevo")
