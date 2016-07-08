def main():
	while True:

		cod = input("CODIGO DO FUNCIONARIO:")
		n_horas_trabalhadas = input("HORAS TRABALHADAS: ")
		n_dependentes = input("NUMERO DE DEPENDENTES: ")
		salario_liquido(n_horas_trabalhadas,n_dependentes,,valor_dependente)
		descontos(salario_liquido,descont_ir,descont_inss)
		print"DESEJA CONTINUAR PROGRAMA ? "
		entrada = raw_input("S/N")
		if entrada == "N" :
			print "FINALIZANDO PROGRAMA ..."
			break



def salario_liquido(n_horas_trabalhadas,n_dependentes,valor_horas = 12.00,valor_dependente):
	salario_liquido = (n_horas_trabalhadas*valor_horas)+(n_dependentes*valor_dependente)
	print salario_liquido

def descontos(salario_liquido,descont_ir,descont_inss):
	inss = salario_liquido*descont_inss
	ir = salario_liquido*descont_ir
	print inss 
	print ir

if __name__ == '__main__':
	main()