# -*- coding: utf-8 -*-
import os
import os.path as path
import wget
from os import popen

while True:
    print"Selecione una opcion"
    print"1- Crear directorio de trabajo"
    print"2- Descargar sitio HTML"
    print"3- Descargar Imagenes"
    print"4- Buscar Archivo HTML"
    print"5- Mostrar capacidad en MB"
    print"6- Salir"
    
    literal = int(raw_input("Ingrese opcion: "))
    
    if literal ==1:
        print "\n", "a) - Crear directorio"
        print "b) - Crear directorios IMG y HTML en el directorio creado"
        print "c) - Consultar existencia de directorio", "\n"
        opc = str(raw_input("Elija entre las opciones: "))       
        if opc == 'a':
            directorio =raw_input("Ingrese el directorio que desea crear: ")
            os.mkdir(directorio)
            print "\n", "Directorio creado satisfactoriamente", "\n"
        
        elif opc == 'b':
            directorio1=raw_input("Ingrese solamente el nombre del directorio: ")
            user = raw_input ("ingrese solamente el nombre de su usuario: ")
            
            directorio_img= '/home/'+user+'/Escritorio/'+directorio1+'/IMG'
            directorio_html= '/home/'+user+'/Escritorio/'+directorio1+'/HTML'
            os.mkdir(directorio_img)
            os.mkdir(directorio_html)
            
        
        elif opc == 'c':
            existn =str(raw_input("Ingrese el directorio que desea consultar: "))
            if path.exists(existn):
                print "\n", "El directorio ya existe", "\n"
            else:
                print "\n", "El directorio aun no existe", "\n"
                   
            
    
    elif literal ==2:
	url_html=raw_input("Ingrese el enlace del archivo HTML que desea descargar: ")
        dest1 = '/home/'+user+'/Escritorio/'+directorio1+'/HTML'
        down_html = ['wget','-r', '-l1','-np','-nd','-A.html','-N','-P', dest1, url_html]
        var1 = popen(' '.join(down_html))
        print "Archivo descargado con exito","\n"
        
    elif literal==3:
		
        url_img=raw_input("Ingrese el enlace de la imagen que desea descargar: ")
        dest = '/home/'+user+'/Escritorio/'+directorio1+'/IMG'
        down_img = ['wget','-r', '-l1','-np','-nd','-A.jpg,.png,.gif','-N','-P' , dest, url_img]
        var = popen(' '.join(down_img))
        print "Imagen descargada con exito","\n"
    
    elif literal==4:
        brow_ff= raw_input("Ingrese el nombre del archivo HTML: ")
        brow= '/home/'+user+'/Escritorio/'+directorio1+'/HTML/'+brow_ff
        os.system('firefox '+brow)
        print "Cargando archivo en el navegador.....","\n"
    
    elif literal==5:
        tamano = raw_input("Ingrese el directorio el cual desea saber su capacidad: ")
        path.getsize(tamano)
        print path.getsize(tamano)    
        
    elif literal==6:
		break
    else:
        print ("ingrese un valor valido")
