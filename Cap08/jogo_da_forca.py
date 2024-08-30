'''
1 - Escolher palavra randomica
2 - esconder as letras
3 - Adivinhar as letras
    a - recebe a letra
        mostra todas as letras sugeridas
    b - verifica a letra
        - se certo abre o 2
            mostra a letra correta na lista
        - se errado abre o 3 
            mostra a letra errada na lista
            derruba uma vida
4 - Revelar as letras
5 - Enforcar o personagem
6 - Resultado
    a - Encontrou todas as letras Ganhou
    b - esgotaram as vidas perdeu

'''

import random
import os


#Parte Visual
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========''']

#parte lógica

def random_word():
    palavras = ['alambique', 'macaco', 'carro', 'bicicleta', 'cachorro']
    palavra = random.choice(palavras)
    return palavra

def shadow_word(palavra):
    shadow = len(palavra) * "_ "
    return shadow

def lives ():
    vidas = 6
    if not palpite in palavra:
        vidas -=1
    return vidas    


palpite = str(input("Digite uma letra: "))
palavra = random_word()
vida = lives()
shadow = shadow_word(palavra)
tabuleiro = board[6-vida]

print(palpite)
print(tabuleiro)
print(shadow)
print(palavra)
