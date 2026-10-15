# Laços de repetição
'''print (0)
print (1)
print (2)
'''
#range nunca inclui o último valor, então se eu colocar range(0,3) ele vai imprimir 0,1,2
# range com passos, o terceiro valor é o passo, ou seja, de quanto em quanto ele vai pular
for item in range(2,12,2):
    print(item) 

#Lista de nomes
nomes = ['Aline', 'Jhonatan', 'Lucas', 'Maria', 'José']
'''dados = [1, 'jhonatan', True, 2.5]'''
for nome in nomes:
    print(nome)

'''for dado in dados:
    print(dado)'''

idades = [16, 17, 18, 19, 20]
#exiba somente os maiores de idade na tela
for idade in idades:
    if idade >= 18:
        print(f'{idade} é maior de idade.')
    else:
        print(f'{idade} é menor de idade.')

#Listas
precos = [20, 50, 100, 200]
'''[20, 50, 100]
0  1  2'''
print(precos[3])

nomes = ['Brazil', 'EUA', 'Mexico', 'Argentina']
print(nomes[2])

#encontrar indice automaticamente
print (nomes.index('EUA'))

'''#Manipular - add novos items na lista
salarios = [1000, 2000, 3000]
salario_usuario = float(input('Qual é o seu salário? '))
salarios.append(salario_usuario)
print(salarios)
'''
salarios = [2500, 900, 5000, 7500]
total = 0
for salario in salarios:
    total = total + salario
print(f'O total de salários é: {total}')


#FATORIAL
numero = int(input('Digite um número para calcular o fatorial: '))
if numero > 0 and type(numero) == int:
    fatorial = 1
    for item in range(1, numero + 1):
        print (f'{fatorial} * {item}')
        fatorial = fatorial * item
        print (f'{fatorial}')
    print (f'O fatorial de {numero} é: {fatorial}')
else:
    print('Não é possível calcular o fatorial de um número negativo ou não inteiro.')
