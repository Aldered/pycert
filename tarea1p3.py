#Cabrera Balderas Carlos Eduardo
#UNAM-CERT

def esPrimo(num,m):
	if m >= 1:
		if num < 2:
			num = num + 1
			esPrimo(num,m)
		else:
			if (num is 2) or (num is 3) or (num is 5) or (num is 7):
				print(num)
				num = num + 1
				m = m - 1
				esPrimo(num,m)
			else:
				if (num % 2 != 0) and (num % 3 != 0 ) and (num % 5 != 0) and (num % 7 != 0):
					print(num)
					num = num + 1
					m = m - 1
					esPrimo(num, m)
				else:
					num = num + 1
					esPrimo(num, m)

esPrimo(50, 4)
