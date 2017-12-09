
#Cabrera Balderas Carlos Eduardo
#UNAM-CERT
""" 
Descripcion: Si no es multiplo de 2, 3, 5 o 7 es primo
imprime los numeros primos a partir de un inicio hasta n
Recibe: num que es el numero inicial del que se parte y 
m que es el rango o numeros primos a mostrar
Devuelve: Numeros primos solicitados en el rango
"""
def esPrimo(num,m):
	""" 
	Revisa que haya numeros primos por imprimir
	"""
	if m >= 1:
		""" 
		Revisa que el numero inicial sea mayor a 2, si lo es incrementa uno
		"""
		if num < 2:
			num = num + 1
			""" 
			Se llama a si misma en ese caso para volver a tratar.
			"""
			esPrimo(num,m)
			""" 
			No toma a 2, 3, 5, 7 porque son los numeros primos base y por
			los tanto tampoco tomara sus multiplos, si es este caso los
			imprime y avanza uno en el num y resta al contador de los 
			restantes.
			"""
		else:
			if (num is 2) or (num is 3) or (num is 5) or (num is 7):
				print(num)
				num = num + 1
				m = m - 1
				esPrimo(num,m)
				""" 
				Comprobamos que no sea un numero que sea divisible por un
				numero diferente de si mismo o de los base. Si no tiene
				divisor entonces es primo y lo imprime, avanza uno en num 
				y quita 1 al contador m.
				"""
			else:
				if (num % 2 != 0) and (num % 3 != 0 ) and (num % 5 != 0) and (num % 7 != 0):
					print(num)
					num = num + 1
					m = m - 1
					esPrimo(num, m)
					""" 
					Si encuentra divisor entonces no es primo y 
					avanza al siguiente y se vuelve a llamar a si
					misma.
					"""
				else:
					num = num + 1
					esPrimo(num, m)

esPrimo(10, 4)
