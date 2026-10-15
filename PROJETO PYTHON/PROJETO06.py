# While

''' syntaxe
while condicao:
    # código a ser executado
'''

# Criar um programa que permite 3 tentativas, antes de fechar
tentativas = 0
while tentativas < 3:
    print("tente novamente")
    tentativas = tentativas + 1

#Quando queremos que uma ação continue acontecendo, até que um critério seja satisfeito 
#Só pode logar, se digitar a senha correta
senha = ''
while senha != "123456":
    senha = input("Digite a senha correta: ")
print("Senha correta, você está logado!")
#garantir que algo esteja preenchido
#Só deve continuar, quando o usuário informar seu nome
nome = ''
while nome == '':
    nome = input("Digite seu nome: ")
print(f"Olá {nome}, seja bem-vindo(a)!")

#Contadores dentro do while
#Ser avisado as 17hrs do por do sol
#Contar de hora em hora até chegar as 17hrs
# Ao chegar as 17hrs, exibir: "hora de ver o por do sol"
horario = 0
while horario <= 17:
    print(horario)
    horario = horario + 1
print("Hora de ver o por do sol!")