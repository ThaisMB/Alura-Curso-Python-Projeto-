import random

def jogar():
    
    cria_cabecalho()
    palavra_secreta = escolhe_palavra_secreta()
    letras_acertadas = arruma_letras(palavra_secreta)


    

    acertou = False
    enforcou = False
    erro = 0
 

    while (not enforcou or not acertou):
        print(letras_acertadas)
        chute = input('Tente uma letra:').strip()
        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = chute
        
            index += 1
        
        if chute not in palavra_secreta:
            erro+=1
            mensagem_errou()
            desenha_forca(erro)
        

        acertou = "_" not in letras_acertadas
        enforcou = erro==7

        if (acertou):
            mensagem_ganhou()
            break
        
        elif(enforcou):
            mensagem_perdeu(palavra_secreta)
            break

    
            


        

        

def desenha_forca(erro):
    print("  _______     ")
    print(" |/      |    ")

    if erro==1:
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if erro==2:
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if erro==3:
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if erro==4:
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")
        
    if erro==5:
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if erro==6:
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if erro==7:
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
                

        

        

    print ('Jogando...')

print('Fim do jogo!')

def cria_cabecalho():
    print('*'*60)
    print('Bem vindo ao jogo de forca!'.center(60))
    print('*'*60)

def escolhe_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha)
        linha = linha.strip()

    indice = random.randrange(0, len(palavras))
    palavra_secreta = palavras[indice]

    return palavra_secreta

def arruma_letras(palavra_secreta):
    quantidade_letras = 0
    letras_acertadas = []

    while quantidade_letras< len(palavra_secreta):
        letras_acertadas.append ('_')
        quantidade_letras += 1
    return letras_acertadas


    

def mensagem_errou():
    print('Você errou! Tente novamente!')

def mensagem_perdeu(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def mensagem_ganhou():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

if (__name__ == '__main__'):
    jogar()