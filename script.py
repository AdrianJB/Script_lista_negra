# -*- coding: utf-8 -*-

import sys
import os

# Con accion podemos añadir (-a) o borrar (-d)
# Con tipo definimos -url o -dom para dominios
# Con nombre definimos la url o dominio que queremos capar

accion = sys.argv[1] 
tipo = sys.argv[2]
nombre = sys.argv[3]+'\n'

if accion == '-a':
    if tipo == '-url':
    	url = open('/etc/squid3/urls.acl', 'a')
    	url.write(nombre)
	url.close() 
    elif tipo == '-dom':
    	dom = open('/etc/squid3/dominios.acl' ,'a')
	dom.write(nombre)
	dom.close()
    else:
	print 'Introduce un tipo valido'
		
elif accion == '-d':
    if tipo == '-url':
	url = open('/etc/squid3/urls.acl', 'r')
	fichero_url = url.readlines()
	url.close()
    for linea in fichero_url:
	if linea == nombre:
	    fichero_url.remove(nombre)
	    # Guardamos la lista con la url solicitada eliminada		
	    url = open('/etc/squid3/urls.acl', 'w')
	    for linea in fichero_url:
		url.write(linea)
		url.close()
		print 'Eliminada correctamente'
	elif tipo == '-dom':
		dominio = open('/etc/squid3/dominios.acl', 'r')
		fichero_dom = dominio.readlines()
		dominio.close()
		for linea in fichero_dom:
			if linea == nombre:
			    fichero_dom.remove(nombre)
		# Guardamos la lista con la url solicitada eliminada		
			    dominio = open('/etc/squid3/dominios.acl', 'w')
			    for linea in fichero_dom:
				dominio.write(linea)
				dominio.close()

			    print 'Eliminado correctamente'
	else:
		print 'Introduce un tipo valido'
else:
    print 'Introduce una accion valida'
