# @Author: Francisco Lucas <lucas>
# @Date:   2017-11-08T19:39:03-03:00
# @Project: Disciplina: Algoritmos e Programação I
# @Filename: 6.py
# @Last modified by:   lucas
# @Last modified time: 2017-11-09T02:37:58-03:00

salAtual = float(input("Informe o salario atual: "))
if (salAtual <= 280):
	perc = 20
	aumento = (salAtual*perc)/100

elif(salAtual > 280 and salAtual <= 700):
	perc = 15
	aumento = (salAtual*perc)/100

elif (salAtual > 700 and salAtual <= 1500):
	perc = 10
	aumento = (salAtual*perc)/100

else:
	perc = 5
	aumento = (salAtual*perc)/100

novoSal = salAtual+aumento

print "Salario atual: R$", salAtual
print "Percentual de aumento: ",perc,"%"
print "Valor do aumento: R$",aumento
print "Novo salario: R$",novoSal
