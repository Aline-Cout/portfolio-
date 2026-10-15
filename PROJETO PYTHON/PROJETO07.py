'''"Crie um gerenciador de login simples, com o máximo de 3 tentativas.
(teremos apenas um único usuário e senha permitido)

usuário - jhonatan
senha - senha123

Após 3 tentativas, se o usuário estiver errado exibir:
"Aguarde 30 mins antes de tentar novamente!"

se o usuário acertar o usuário e senha antes disso, exibir "Login feito com sucesso"'''

'''
Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais
informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
- usuário
- senha

2. O que devo fazer com estes dados?
- verificar se o usuário é 'aline'
- verificar se a senha é 'senha123'

3. Quais são as restrições deste problema?
- o usuário possui apenas 3 tentativas

4. Qual é o resultado esperado?
- Se o usuário acertar o usuário e senha antes de 3 tentativas, exibir "login feito com sucess
- Se o usuário não acertar antes das 3 tentativas, exibir "favor aguardar 30 min'''

usuario = ''
senha= ''
tentativas = 0

while (usuario != 'aline' or senha != 'senha123') and tentativas < 3:
    usuario = input('Digite o seu usuário: ')
    senha = input('Digite a sua senha: ')
    tentativas += 1
    
if usuario == 'aline' and senha == 'senha123':
    print('Login feito com sucesso!')
else:
    print('Aguarde 30 minutos antes de tentar novamente!')


