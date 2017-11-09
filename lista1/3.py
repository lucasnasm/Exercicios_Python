# @Author: Francisco Lucas <lucas>
# @Date:   2017-11-07T15:50:11-03:00
# @Filename: 3.py
# @Last modified by:   lucas
# @Last modified time: 2017-11-09T03:03:13-03:00

valorConta = input("Informe o valor da conta: ")
diasAtraso = input("Informe os dias dem atraso: ")
multa = (valorConta * 2) / 100
resultado = (diasAtraso * 0.50) + multa

print "A multa a ser paga eh: R$", resultado
