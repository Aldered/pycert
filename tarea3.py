#Becerra Alvarado Hugo Alonso
#Cabrera Balderas Carlos Eduado
#UNAM-CERT

from random import choice

caso_a = ".*[Aa4]*."
caso_e = ".*[Ee3]*."
caso_i = ".*[iI1lL]*."
caso_o = ".*[oO0]*."
caso_u = ".*[uUvV]*."

def letras_num(archivo, diccionario):

	"""A la variable lista, la separara por sus saltos de linea,
	para cada linea en el parametro archivo leera sus lineas
	y las guardara como una lista."""
	lista = [word.strip('\n').split('\n') for word in open (archivo, 'r').readlines()]
	"""Abrira el archivo diccionario y escribira en el lo que hay en la
	variable lista separando con saltos de linea cada palabra"""
	with open(diccionario, 'w') as output:
		output.write('\n'.join(str(line) for line in lista))
		#conv = ord(lista) - 96
		#output.write.append(conv)
letras_num('archivo.txt', 'diccionario.txt')

def trans(archivo, diccionario):

	for word in open (archivo, 'r').readlines():
		word.split(": ")
	for "a" in word:
		caso_a
	for "o" in word:
		caso_e
	for "i" in word
		caso_i
