def main():
	while True:

		cod = input("CODIGO DO FUNCIONARIO:")
		n_horas_trabalhadas = input("HORAS TRABALHADAS: ")
		n_dependentes = input("NUMERO DE DEPENDENTES: ")
		x=salario_liquido(n_horas_trabalhadas,n_dependentes	)
		print "Salario Liquido: R$ %.2f" % x
		descontos(x)
		print"DESEJA CONTINUAR PROGRAMA ? "
		entrada = raw_input("\nTecle Enter para finalizar:\n ")
		if entrada == "" :
			print "FINALIZANDO PROGRAMA ..."
			break



def salario_liquido(n_horas_trabalhadas,n_dependentes,valor_dependente=40.0,valor_horas = 12.00):
	salario = (n_horas_trabalhadas*valor_horas)+(n_dependentes*valor_dependente)
	return salario

def descontos(salario_liquido,descont_ir=0.05,descont_inss = 0.085):
	inss = salario_liquido*descont_inss
	ir = salario_liquido*descont_ir
	print "INSS: R$ %.2f" % inss 
	print "IR - Imposto de Renda: R$ %.2f" % ir
if __name__ == '__main__':
	main()