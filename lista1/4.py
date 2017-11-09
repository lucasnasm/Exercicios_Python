# @Author: Francisco Lucas <lucas>
# @Date:   2017-11-08T02:32:24-03:00
# @Project: Disciplina: Algoritmos e Programação I
# @Filename: 4.py
# @Last modified by:   lucas
# @Last modified time: 2017-11-09T02:02:57-03:00

saldo = input("Informe o saldo disponivel para viajar: ")
dias = input("Informe a quantidade de dias: ")
#variavel com valores predefinidos
gastoComViagem = 1200+(45*dias)+(25*dias)+400
restante = gastoComViagem-saldo

if(gastoComViagem < saldo):
	print "Parabens, voce podera viajar!!!"
else:
	print "Infelizmente voce nao podera viajar:"
	print "Para viajar voce precisa de R$",restante,"a mais!!!"
