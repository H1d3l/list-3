def main():
	print "Q9"
	numero = raw_input("Digite:")
	multiplos(numero, 1)

def multiplos(numero,order):
	if order > 10:
		print"fim"
	else:
		mult = numero*order
		print"m = %d"% mult
		multiplos(numero,order+1)

if __name__ == '__main__':
	main()