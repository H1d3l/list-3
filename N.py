
def Questao20_Lista3(N):

	Soma = 0

	for i in range(1, N+1):

		if i%2!=0:

			Soma += (1.0/i)

		else:


			Soma -= (1.0/i)
	print "S = %.2f" % Soma

def main():

	Num = input("Digite um numero: ")
	Questao20_Lista3(Num)

if __name__ == '__main__':
	main()