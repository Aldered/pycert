#Cabrera Balderas Carlos Eduardo

from re import findall

def regex_ip(ip):

	reip = "^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$"
	holi = findall(reip, ip)
	print holi

def regex_correo(email):
	
	remail = "[a-z]+\.*[a-z]*@.*\..*"
	corr = findall(remail, email)
	print corr
regex_ip("192.168.1.11")
regex_correo("carlos.balderas@gmail.com")


