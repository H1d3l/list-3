arquivo = open("test.txt","r")
linha = arquivo.readlines()
login = raw_input("Digite login: ")

for i in linha:
	if i == login:
		cont = cont+1
		print cont		
	else:
		print "n tem login"


