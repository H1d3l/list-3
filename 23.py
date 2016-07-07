def valores(valor_dependente,valor_horas,descont_inss,descont_ir)
	valor_dependente = 40.00
	valor_horas = 12.00
	descont_inss = 8.5/100
	descont_ir = 5.0/100

def salario_liquido(n_horas_trabalhadas,n_dependentes,valor_horas,valor_dependente):
	salario_liquido = (n_horas_trabalhadas*valor_horas)+(n_dependentes*valor_dependente)
	print salario_liquido

def descontos(salario_liquido,descont_ir,descont_inss):
	inss = salario_liquido*descont_inss
	ir = salario_liquido*descont_ir
	print inss 
	print ir

if __name__ == '__main__':
	main()
salario_liquido(2,1,12.00,40.00)
descontos(64.0,8.5/100,5.0/100)