# @Author: Francisco Lucas <lucas>
# @Date:   2017-11-09T01:55:00-03:00
# @Project: Disciplina: Algoritmos e Programação I
# @Filename: 5.py
# @Last modified by:   lucas
# @Last modified time: 2017-11-09T02:03:04-03:00

pesoPaciente = input("Informe o peso: ")
idadePaciente = input("Informe a idade: ")
#Setando valores da variavel para evitar erro variavel nao definida
mg=0
if (idadePaciente >= 15 and pesoPaciente >= 50):
	mg = (800*20)/100
elif(0 > pesoPaciente < 50):
	mg = (500*20)/100
else:
	if  pesoPaciente >= 5 and pesoPaciente <=10:
		mg = (200*20)/100
	elif pesoPaciente >= 10.1 and pesoPaciente <= 15:
		mg = (300*20)/100
	elif pesoPaciente >= 15.1 and pesoPaciente <= 30:
		mg = (400*20)/100
	elif pesoPaciente > 30:
		mg = (500*20)/100

print "Peso do paciente: ",pesoPaciente
print "O Paciente deve tomar:",mg,"Gotas"
