#Cabrera Balderas Carlos Eduardo
#UNAM-CERT

lrg = ""

def pali(cadena):
	
	"""Descripcion: Regresa el palindromo mas grande de la cadena dada."""
	"""Que recibe: Cadena con palindromo."""
	"""Que regresa: Solo el palindromo mas grande."""

	if cadena == cadena[::-1]:
		return True

	#"""Checa que la cadena sea palindroma, si lo es, 
            #regresa True y entra al for"""

cadena = ("aaaaaaaaaaatttttfff")

	#"""Asigna dos contadores llamados cnt1 y cnt2,
            #para enumerar los elementos en cadena"""
for cnt1, item in enumerate(cadena):
	for cnt2, item in enumerate(cadena):
	#"""A la variable busca, le asigna el valor de cnt1
            #el cual sera el primer elemento mas el segundo
            #de nuestra cadena dada."""
		busca = cadena[cnt1:cnt2+1]
	#"""Si busca y su longitud son mayores a lo que ya 
	    #estaba guardado en lrg igualara lrg a busca"""
		if pali(busca) and (len(busca) > len(lrg)):
			lrg = busca
print(lrg)

