#_*_ coding:utf-8 _*_
def calculo(number):
    while number>1:
        number=number/2.0
    print"%.2f" % (number)    
def main():
    numero=input("Insira Valor à ser calculado: ")
    calculo(numero)

if __name__ == '__main__':
	main()