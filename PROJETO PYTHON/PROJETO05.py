'''#Exemplo prático com algoritmo real: Validador de senhas
Problema:
Você trabalha em um sistema que precisa verificar se todas as senhas digitadas por usuários são válidas.
Para uma senha ser válida, ela deve ter pelo menos 6 caracteres.'''

#len(variavel) -> quantidade de caracteres
# len(senha) -> 6 ou não

senhas = ["abc", "segura123", "12345", "python123", "oi"]
for senha in senhas:
    if len(senha) >= 6:
        print(f'A senha {senha} é válida.')
    else:
        print(f'A senha {senha} é inválida deve possuir no mínimo 6 caracteres.')