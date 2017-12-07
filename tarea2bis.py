#Cabrera Balderas Carlos Eduardo
#UNAM-CERT

import random
import string
import re

def pass_gen():

	pw = []
	min = string.ascii_lowercase
	may = string.ascii_uppercase
	n = string.digits

	pass_len = int(raw_input('Longitud de la password: '))
	may_len = int(raw_input('Numero de mayusculas que tendra: '))
	min_len = int(raw_input('Numero de minusculas que tendra: '))
	n_len = int(raw_input('Numero de numeros que tendra: '))
	
	pass_tot = may_len + min_len + n_len
	len_tot = pass_len - may_len - min_len - n_len 
	
	if len_tot < 0:
		print 'Intente de nuevo.'
		pass_gen()
	else:
			lsa = pw.append(random.choice(min))
			lse = pw.append(random.choice(may))
			lsi = pw.append(random.choice(n))
			#pw_list.insert(str(''.join(random.sample(min))))
			#pw_list.insert(str(''.join(random.sample(may))))
			#pw_list.insert(str(random.randint(n)))
			ls_tot = lsa + lse + lsi
			print ls_tot
pass_gen()

