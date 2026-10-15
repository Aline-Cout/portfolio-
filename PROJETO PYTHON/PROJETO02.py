# Condicionais -  if elif else
'''
E ae jhonatan, bora dar uma saida hoje?
Se eu terminar meu trabalho aqui eu consigo.
'''
'''
trabalho_terminado = True
if trabalho_terminado == True:
    print('Bora sim, vamos sair!')  
    '''

trabalho_terminado = False
if trabalho_terminado == True:
    print('Bora sim, vamos sair!') 
else:
    print('Não posso sair, ainda tenho trabalho para fazer!') 

'''
Ei, Você consegue me ajudar a mover essas caixas lá para fora hoje a tarde?
Se eu estiver livre, sim. Mas se não der, pede meu irmão para te ajudar
'''
estou_livre = True
if estou_livre == True:
    print('Sim, posso te ajudar a mover as caixas!')
else:
    print('Não posso te ajudar, mas pede para meu irmão te ajudar!')

estou_livre = input('Você está livre para me ajudar a mover as caixas? (sim/não)')  
if estou_livre == 'sim':
    print('Sim, posso te ajudar a mover as caixas!')
else:
    print('Não posso te ajudar, mas pede para meu irmão te ajudar!')

'''
Eu cheguei atrasado na aula. Ainda posso entrar?
Se for a primeira ou segunda vez que você chega atrasado, pode sim. Mas se for a terceira vez, você será suspenso.'''

atrasos = int(input('Quantas vezes você chegou atrasado na aula?'))
if atrasos >=3:
    print('você está suspenso!')
elif atrasos == 2:
    print('mais uma falta e está suspenso!')
elif atrasos == 1:
    print('mais duas faltas e você será suspenso!')
else:
    print('Pode entrar, mas não se atrase mais!')


