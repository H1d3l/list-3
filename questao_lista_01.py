def divisores(numero):
	div=''
	for i in range(1,numero+1,1):
		if numero%i==0:
			print i,'eh divisor'
		else:
			pass
	
def main():
	import os
	import time

	while True:
		numero=input('Insira o numero desejado: ')
		if numero>0:
			divisores(numero)
		else:
			print 'Adeus'
			break
		time.sleep(3)
		os.system('clear')
		

if __name__=="__main__":
	main()
