# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import random
#random.seed(3)
#numero = random.randint(1, 10)

from random import randint, choice,seed
numero = randint(1, 10)
fruta = choice(['maçã', 'banana', 'laranja'])

def adivinhe_o_numero():
    seed(24)
    numero_aleatorio = randint(1, 100)
    tentativas = 0
    acertou = False
    print("Adivinhe o número entre 1 e 100")

    while not acertou:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1
     
        if palpite < numero_aleatorio:
             print("Muito baixo!")
        elif palpite > numero_aleatorio:
             print("Muito alto!")
        else:
                 print(f"Você adivinhou em {tentativas} tentativas.")
                 acertou = True
 
#adivinhe_o_numero()

def sorteie_dado(): 
    sorteado = randint(1,6)
    print(f"o numero sorteado foi {sorteado}") 
    
def sorteio_dado(lados=6): 
    sorteado = randint(1,lados)
    print(f"o numero sorteado foi {sorteado}") 