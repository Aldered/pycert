#Becerra Alvarado Hugo Alonso
#Cabrera Balderas Carlos Eduardo

from re import search
from requests import get 
from requests import options
from requests.exceptions import ConnectionError
import re
import sys
import optparse

f1=open("reporte.txt",'w')

f_corr = f1.write("Los correos encontrados son: ")
f_server = f1.write("El servidor es: ")
f_php = f1.write("La version de PHP que usa es: ")
f_http = f1.write("Los metodos http que usa son: ")
f_cms = f1.write("El cms que maneja es:" )

def printError(msg, exit = False):
	sys.stderr.write ('Error:\t%s\n' % msg)
	if exit:
		sys.exit(1)
def addOptions():
	parser = optparse.OptionParser()
	parser.add_option('-v','--verbose', dest='verbose', default=None, action= 'store_true', help='Detalles.') 
	parser.add_option('-c', '--correo', dest='correo', default=None, help='Obtenemos el correo.')
	parser.add_option('-s', '--server', dest='server', default=None, help='Nos da la version del servidor')
	parser.add_option('-p', '--php', dest='php', default=None, help="Nos da la version de PHP.")
	parser.add_option('-m', '--http', dest= 'http', default=None, help="Nos da los metodos http usados.")
	parser.add_option('-C', '--cms', dest='cms', default=None, help="Nos da los cms.")
	parser.add_option('-r', '--reporte', dest='reporte', default=None, action="store_true", help="Nos genera un reporte.")
	parser.add_option('-t', '--tor', dest='tor', default=None, action="store_true", help="Se usara tor.")
	parser.add_option('-b', '--busqueda', dest='busqueda', default=None, action="store_true", help="Se hara la busqueda.")
	parser.add_option('-a', '--archivo', dest='archivo', default=None, help="Archivo de configuracion.")
	opts,args = parser.parse_args()
	return opts

def checkOption(option):
	if option.server is None:
		printError('Especifica un servidor.', True)

if __name__ == '__main__':
	try:
		opts = addOptions()
		checkOption(opts)
				
		arch=open(opts.archivo,'r')		
		for n in arch.readlines():
			print n
		arch.close()

		if opts.verbose == True:
			print "Ingresaste verbose"
		if opts.correo == True:
			co = "[a-z]+\.*[a-z]*@.*\..*"
			re1 = get(opts.server, co)
			print "re1"
		if opts.server!=False:
			re_server = get(opts.server).headers['server']
			print re_server
			f1.write(re_server)
		if opts.php == True:
			re_php = get(opts.php).headers['x-powered-by']
			print "La version de PHP es: %s " % re_php
			f1.write(re_php)
		if opts.http == True:
			re_http = get(opts.http).headers['options']
			print "Los metodos que permite son: %s " % re_http
			f1.write(re_http)
		if opts.cms == True:
			patron = r"meta name=\"generator\" content=\".*\""
			print 'El cms que maneja es: %s ' % re.search(patron, get(opts.server))
		if opts.reporte == True:
			print "Ingresaste reporte."
		if opts.tor == True:
			print "Ingresaste tor."
		if opts.busqueda == True:
			print "Ingresaste busqueda."
	except Exception as e:
		printError('Ocurrio un error inesperado')
		printError(e, True)

f1.close()






