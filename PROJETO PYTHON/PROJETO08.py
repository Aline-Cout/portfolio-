# - Chute o número
'''
Escreva um programa que, ao iniciar, gere um valor aleatório de 1 a 10 e permita
que o usuário chute números até acertar o valor gerado.

O programa deve informar se o chute foi maior, menor ou igual ao valor aleatório
gerado no início.
'''
import random

valor_aleatorio = random.randint(1, 10)
acertou = False
while acertou == False:
    chute = int(input('Chute um número de 1 a 10: '))
    if chute > valor_aleatorio:
       print('chute um valor mais baixo')
    elif chute < valor_aleatorio:
       print('chute um valor mais alto')
    else:   
       print('Parabéns, você acertou!')
       acertou = True

