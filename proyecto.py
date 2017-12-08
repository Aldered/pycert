#Becerra Alvarado Hugo Alonso
#Cabrera Balderas Carlos Eduardo

from requests import get 
from requests.exceptions import ConnectionError
import sys
import optparse

def printError(msg, exit = False):
	sys.stderr.write ('Error:\t%s\n' % msg)
	if exit:
		sys.exit(1)
def addOptions():
	parser = optparse.OptionParser()
	parser.add_option('-v','--verbose', dest='verbose', default=None, action= 'store_true', help='Detalles.') 
	parser.add_option('-c', '--correo', dest='correo', default=None, action='store_true', help='Obtenemos el correo.')
	parser.add_option('-s', '--server', dest='server', default=None, action='store_true', help='Nos da la version del servidor')
	parser.add_option('-p', '--python', dest='python', default=None, action="store_true", help="Nos da la version de Python.")
	parser.add_option('-m', '--http', dest= 'http', default=None, action="store_true", help="Nos da los metodos http usados.")
	parser.add_option('-C', '--cms', dest='cms', default=None, action="store_true", help="Nos da los cms.")
	parser.add_option('-r', '--reporte', dest='reporte', default=None, action="store_true", help="Nos genera un reporte.")
	parser.add_option('-t', '--tor', dest='tor', default=None, action="store_true", help="Se usara tor.")
	parser.add_option('-b', '--busqueda', dest='busqueda', default=None, action="store_true", help="Se hara la busqueda.")
	parser.add_option('-a', '--archivo', dest='archivo', default=None, action="store_true", help="Archivo de configuracion.")
	opts,args = parser.parse_args()
	return opts

def checkOption(option):
	if option.server is None:
		printError('Especifica un servidor.', True)

if __name__ == '__main__':
	try:
		opts = addOptions()
		checkOption(opts)
		
		archivo=open("opts.archivo", 'r'):
			
			close(archivo)
		if opts.verbose == True:
			print "Ingresaste verbose."
		if opts.correo == True:
			print "Ingresaste correo."
		if opts.server == True:
			print "Ingresaste server."
		if opts.python == True:
			print "Ingresaste python."
		if opts.http == True:
			print "Ingresaste http."
		if opts.cms == True:
			print "Ingresaste CMS."
		if opts.reporte == True:
			print "Ingresaste reporte."
		if opts.tor == True:
			print "Ingresaste tor."
		if opts.busqueda == True:
			print "Ingresaste busqueda."
	except Exception as e:
		printError('Ocurrio un error inesperado')
		printError(e, True)








