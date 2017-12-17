#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
#Becerra Alvarado Hugo Alonso
#Cabrera Balderas Carlos Eduardo

import sys
import optparse
from requests import get 
from requests import options
import requests
from requests.exceptions import ConnectionError
import socks
from datetime import datetime
import socket
import re 
from re import search
from re import findall
import httplib                            
import urllib2

'''
Antes que nada profesor, no nos salió/dio tiempo: Tor, verbose, configuración de las banderas del archivo de configuración ;-;
'''

'''
Abrimos reporte.txt en modo de escritura de manera global para que en cualquier parte podamos llamarlo y escribir en el archivo.
'''
f1=open("reporte.txt",'w')

def printError(msg, exit = False):
	sys.stderr.write ('Error:\t%s\n' % msg)
	if exit:
		sys.exit(1)
	
def addOptions():
	'''
	Añadimos las opciones a usar.
	'''	
	parser = optparse.OptionParser()
	parser.add_option('-v','--verbose', dest='verbose', default=None, action= 'store_true', help='Detalles.') 
	parser.add_option('-c', '--correo', dest='correo', default=None, help='Obtenemos el correo.')
	parser.add_option('-s', '--server', dest='server', default=None, help='Nos da la version del servidor') #ya
	parser.add_option('-p', '--php', dest='php', action='store_true', default=None, help="Nos da la version de PHP.")#ya
	parser.add_option('-m', '--http', dest= 'http', default=None, action='store_true', help="Nos da los metodos http usados.")
	parser.add_option('-C', '--cms', dest='cms', default=None, action='store_true', help="Nos da los cms.") #ya
	parser.add_option('-r', '--reporte', dest='reporte', default=None, action="store_true", help="Nos genera un reporte.")
	parser.add_option('-t', '--tor', dest='tor', default=None, action="store_true", help="Se usara tor.")
	parser.add_option('-b', '--busqueda', dest='busqueda', default=None, action="store_true", help="Se hara la busqueda.")
	opts,args = parser.parse_args()
	return opts


def checkOption(option):
	'''
	Siempre nos tendrán que dar un host, por lo que si no se cumple esta condición nos mandará un mensaje de error.
    '''
	if option.server is None:
		printError('Especifica un servidor.', True)

def busqueda(opts):
	'''
	Recibirá como parámetro la opts para poner la url.
	Devolverá los archivos que hagan match con la condición.
	'''
	try:
		arch=open('archivos.txt','w') #Para guardar el contenido encontredo en el servidor
		with open('bfiles.txt', 'r') as lst: #Archivo que muestra el nombre de los posibles archivos que se pueden encontrar en el servidor
			listaB = lst.readline() #Variable a la que se le asigna la lectura del archivo.
			for l in listaB:
				url_files = opts.server + "/" + l #Estructura de la URL para que vaya haciendo el ciclo, encontrando matches.
				nope = 0 
				rqst=requests.get(url_files[:-1:])
				if rqst.status_code == 200:	#Filtramos las 200 y la 302, la variable nope es la que hará el "filtro".

					for mala in rqst.history:
						if mala.status_code==302:
							nope = 1

					if nope == 0: 
						print 'Abra el archivo "archivos.txt" para ver los archivos almacenados'
						f1.write(l)
						arch.write(l)

			lst.close()
	except Exception as e:
		printError("No hay archivos")

if __name__ == '__main__':
	try:
		opts = addOptions()
		checkOption(opts)

		if opts.verbose == True:
			print "This is a shame, don't use this option anymore...thanks for your understanding."
		if opts.correo == True:
			"""
			Busca dentro del código html los correos que se encuentren en este, usando findall y 
			expresiones regulares, mostrando los posibles correos encontrados.
			"""
			try:
				pet = urllib2.Request(opts.server) 
				html1 = urllib2.urlopen(pet).read()
				co = re.findall("[a-z]+\.*[a-z]*@.*\..*", html1)
				f1.write("\nLos correos son: %s\n" % co) 
				print 'Los correos son: %s' % co
			except:
				print 'No encontré correos :/'
		if opts.server != False:
			"""
			Busca en las cabeceras http el servidor y muestra el nombre de este.
			"""
			try:
				re_server = get(opts.server).headers['server'] #Trae la cabecera headers, y mestra el nombre
				f1.write("\nEl servidor que usa es: %s\n" % re_server)#guarda el resultado en el reporte.txt
				print "La version del servidor es %s" % re_server
			except:
				print 'No se puedo obtener la versión del servidor uwu' #Si no encuentra la cabecera, manda este error.

		if opts.php == True:
			"""
			Muestra la versión de PHP que maneja el servidor, obteniendo el nombre de la cabecera X-Powered-By
			y guardando el resultado en el reporte.txt
			"""
			try:
				re_php = options(opts.server).headers['X-Powered-By']
				f1.write("\nLa version de PHP que usa es: %s\n" % re_php)
				print "La version del servidor es %s" % re_php
			except:
				print 'No se pudo obtener la versión de php uwu'

		if opts.http == True:
			"""
			Obtiene los métdos https, a trevés de la cabecera Allow, esta nos muestra los métodos que permite y maneja el sitio web
			"""
			try:
				re_http = requests.options(opts.server).headers['allow']
				f1.write("\nLos métodos http que usa son: %s\n" % re_http)
				print "Los métodos http que usa son: %s " % re_http
			except:
				print 'No se encontraron los métodos :O'

		if opts.cms == True:
			"""
			Obtiene el CMS (content management system), buscando en el código HTML, su <meta name='Generator' content=*>
			después, sólo queremos lo que hay en content así que hacemos un split para obtener solo el content.
			"""
			try:
				req = urllib2.Request(opts.server)
				html = urllib2.urlopen(req).read()
				patron = re.findall('<meta name=\"Generator\" content=\".*\"', html)
				print "El cms es " + patron[0].split("\"")[3] + "\n"
			except:
				print 'No se pudo obtener el cms xS'

		if opts.reporte == True:
			"""
			Muestra el servidor y la fecha en la cual se realizó el escaneo.
			"""
			f1.write("\nFecha: " + str(datetime.now()) + "\nURL: " + opts.server)
		if opts.tor == True:
			print "Well...this is embarrassing."
		if opts.busqueda == True:
			try:
				busqueda(opts)
			except:
				print 'No hay busqueda xS'
	except Exception as e:
		printError('Ocurrio un error inesperado')
		printError(e, True)

f1.close()

#Feliz Navidad :D y próspero año nuevo
