def main():
	import os
	cont1,cont2,cont3,cont4=0.0,0.0,0.0,0.0
	total1,total2,total3,total4=0,0,0,0
	while True:
	
		idade= input("Insira a idade: ")
		if idade >-1:
			opiniao= input("Insira a opiniao: ")
			if opiniao == 1: #otimo
				total1 +=idade
				cont1 +=1
			elif opiniao == 2: #bom
					total2 +=idade
					cont2 +=1
			elif opiniao == 3: #regular
					total3 +=idade
					cont3 +=1
			elif opiniao == 4: #pessimo
					total4 +=idade
					cont4 +=1
		else:
			break

	media_otimo=total1/cont1
	total=cont1+cont2+cont3+cont4
	
	os.system('clear')
	print "Media Idade Otimo: ",media_otimo
	print "Pessoas regular: ",cont3
	print "Percentualde Bom: ",(cont2/total)*100	

if __name__=='__main__':
	main()
