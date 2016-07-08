#_*_ coding:utf-8 _*_
def progressao(a0,limite,constante):
	print a0*(constante)**limite

def main():
    a0=input("Insira valor de a0: ")
    limite=input("Insira limite da progressao: ")
    constante=input("Insira valor de R: ")
    progressao(a0,limite,constante)

if __name__ == '__main__':
    main()