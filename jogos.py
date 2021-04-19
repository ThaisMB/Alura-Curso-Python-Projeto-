import forca
import adivinhacao
from time import sleep

print('*'*60)
print("******************** Escolha seu jogo: *********************")
print('*'*60)

print('(1)Forca (2)Adivinhação')

jogo = int(input( 'Escolha o jogo:'))

if (jogo == 1):
    print('Carregando o jogo Forca...')
    sleep(3)
    forca.jogar()

elif (jogo == 2):
    print('Carregando o jogo Adivinhação...')
    sleep(3)
    adivinhacao.jogar()