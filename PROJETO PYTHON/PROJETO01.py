# Variáveis
velocidade_internet = 600
print (velocidade_internet)
idade = 16
print (type(idade))

#Problema 1- Valor por hora 
#Escreva um programa que retorna o valor hora de um funcionário 
#Com base no seu sálario mensal e horas trabalhadas por mês
#1º Sálario mensal e  Quantidade de horas trabalhadas 
#2º Calcular o valor hora
#3º Precisa ter um valor do sálario mensal e um valor da quantidade de horas trabalhadas 
#4º Exibir o valor hora da pessoa com base no cáculo de valor
#5º Receber salario mensal // receber a quantidade de horas trabalhadas // calcular o valor hora // exibir o valor hora// valor hora = salario mensal/ quantidade de horas trabalhadas// exibir o valor hora 

salario_mensal = input('Qual é o seu sálario mensal?')
horas_trabalhadas = input('Quantas horas trabalhadas por mês?')
valor_hora = float(salario_mensal) / int(horas_trabalhadas)
print('O valor hora do funcionário é:', valor_hora) 