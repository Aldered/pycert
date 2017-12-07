#Cabrera Balderas Carlos Eduardo
#UNAM-CERT

def od_num():
	dicc = {num: (hex(num), bin(num)) for num in range(50) if bin(num).count("1") % 2 == 0}
	print dicc
od_num()
