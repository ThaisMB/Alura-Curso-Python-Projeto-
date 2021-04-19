def jogar():
    from random import randrange

    print('*'*60)
    print('Bem vindo ao jogo de adivinhação!'.center(60))
    print('*'*60)

    rodada= 1
    numero_secreto = randrange(1,101)

    n_tentativas = 0
    pontos = 1000
    pontuacao = 0

    print('Qual nível de dificuldade?')
    print('(1)Fácil (2)Médio (3)Díficil')

    nivel_dificuldade =int(input('Escolha um nível:'))
    if (nivel_dificuldade == 1):
        n_tentativas = 10
    elif (nivel_dificuldade == 2):
        n_tentativas = 5
    elif (nivel_dificuldade == 3):
        n_tentativas = 3

    print(f'Sua pontuação inicial é {pontos} pontos.')
    while (rodada<= n_tentativas):
        print('Eu escolhi um número de 1 a 100. Você consegue adivinhar?')

        print(f'Tentativa {rodada} de {n_tentativas}:')
        chute = int(input(f'Dê seu {rodada}º chute:'))

        pontos_perdidos = abs(numero_secreto - chute)
        pontuacao = pontos - pontos_perdidos
        pontos = pontuacao
        if (chute == numero_secreto):
            print('Você acertou!')
            break

        elif (chute> numero_secreto):
            print('Você errou! O número secreto é menor que seu chute.')

        else:
            print('Você errou! O número secreto é maior que seu chute!')
        rodada += 1
    print(f'Fim do jogo! O número secreto era {numero_secreto}.')
    print(f'Sua pontuação foi: {pontuacao}')

if (__name__ == '__main__'):
    jogar()
