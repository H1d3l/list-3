def main():
	num = input("Digite um numero: ")
	numero(num)

def numero():
	total = 0
	for i in range(1,num+1):
		total = i + total
		print"A soma dos valores entre 1 e %d eh %d "%(num,total)



if __name__ == 'main':
	main()