from random import *
import time
floor = 1
x = randint(0,2)
acertou = False
pontos = 0
bala = 0
tempo = 30
print('Bem vindo ao jogo de tiro ao alvo!')
print('você tem 30 movimentos para acertar o maior número de pessoas possível')
print('você começa no andar do meio (1)')
print('Digite 1 para subir, 2 para descer e 3 para atirar')
print('Os seus alvos podem estar em qualquer um dos andares')
print('Mas, se você ficar no mesmo andar do inimigo por 1 segundo eles atiram e você morre')
print('O jogo começa em 5 segundos...')
print('Boa sorte!')
time.sleep(5)

if x == 2:
    print(".......X")
    print("I--.....")
    print("I.......")
elif x == 1:
    print("........")
    print("I--....X")
    print("I.......")
elif x == 0:
    print("........")
    print("I--.....")
    print("I......X")

while tempo > 0:    
    a = int(input("Up , Down or shoot? (1, 2 or 3) "))
#Up
    if a == 1:
        tempo -= 1
        if x == 2:
            if floor == 2:
                floor = 0
                print("I......X")
                print("........")
                print("I--.....")
            elif floor == 1:
                floor = 2
                print("I--....X")
                print("I.......")
                print("........")
            elif floor == 0:
                floor = 1
                print(".......X")
                print("I--.....")
                print("I.......")
        elif x == 1:
            if floor == 2:
                floor = 0
                print("I.......")
                print(".......X")
                print("I--.....")
            elif floor == 1:
                floor = 2
                print("I--.....")
                print("I......X")
                print("........")
            elif floor == 0:
                floor = 1
                print("........")
                print("I--....X")
                print("I.......")
        elif x == 0:
            if floor == 2:
                floor = 0
                print("I.......")
                print("........")
                print("I--....X")
            elif floor == 1:
                floor = 2
                print("I--.....")
                print("I.......")
                print(".......X")
            elif floor == 0:
                floor = 1
                print("........")
                print("I--.....")
                print("I......X")                
#Down
    elif a == 2:
        tempo -= 1
        if x == 2:
            if floor == 2:
                floor = 1
                print(".......X")
                print("I--.....")
                print("I.......")
            elif floor == 1:
                floor = 0
                print("I......X")
                print("........")
                print("I--.....")
            elif floor == 0:
                floor = 2
                print("I--....X")
                print("I.......")
                print("........")
        if x == 1:
            if floor == 2:
                floor = 1
                print("........")
                print("I--....X")
                print("I.......")
            elif floor == 1:
                floor = 0
                print("I.......")
                print(".......X")
                print("I--.....")
            elif floor == 0:
                floor = 2
                print("I--.....")
                print("I......X")
                print("........")
        if x == 0:
            if floor == 2:
                floor = 1
                print("........")
                print("I--.....")
                print("I......X")
            elif floor == 1:
                floor = 0
                print("I.......")
                print("........")
                print("I--....X")
            elif floor == 0:
                floor = 2
                print("I--.....")
                print("I.......")
                print(".......X")
#Shoot
    elif a == 3:
        tempo -= 1
        if floor == x:
            print("Você aceertou o alvo! +1 ponto")
            pontos += 1
            x = randint(0,2)
            if x == 2:
                if floor == 2:
                    print("I--....X")
                    print("I.......")
                    print("........")
                elif floor == 1:
                    print(".......X")
                    print("I--.....")
                    print("I.......")
                elif floor == 0:
                    print("I......X")
                    print("........")
                    print("I--.....")
            elif x == 1:
                if floor == 2:
                    print("I--.....")
                    print("I......X")
                    print("........")
                elif floor == 1:
                    print("........")
                    print("I--....X")
                    print("I.......")
                elif floor == 0:
                    print("I.......")
                    print(".......X")
                    print("I--.....")
            elif x == 0:
                if floor == 2:
                    print("I--.....")
                    print("I.......")
                    print(".......X")
                elif floor == 1:
                    print("........")
                    print("I--.....")
                    print("I......X")
                elif floor == 0:
                    print("I.......")
                    print("........")
                    print("I--....X")
        else:
            print("Você errou!")
            x = randint(0,2)
            bala += 1
            if x == 2:
                if floor == 2:
                    print("I--....X")
                    print("I.......")
                    print("........")
                elif floor == 1:
                    print(".......X")
                    print("I--.....")
                    print("I.......")
                elif floor == 0:
                    print("I......X")
                    print("........")
                    print("I--.....")
            elif x == 1:
                if floor == 2:
                    print("I--.....")
                    print("I......X")
                    print("........")
                elif floor == 1:
                    print("........")
                    print("I--....X")
                    print("I.......")
                elif floor == 0:
                    print("I.......")
                    print(".......X")
                    print("I--.....")
            elif x == 0:
                if floor == 2:
                    print("I--.....")
                    print("I.......")
                    print(".......X")
                elif floor == 1:
                    print("........")
                    print("I--.....")
                    print("I......X")
                elif floor == 0:
                    print("I.......")
                    print("........")
                    print("I--....X")                
    else:
        print("Inválido! Digite apenas 1, 2 ou 3.")

if tempo == 0:
    pontostotais = pontos * 10000 - bala * 10000
    print("você terminou seus movimentos possíveis! Você matou", pontos, "pessoas, parabéns mercenário!")
    print("Mas você errou", bala, "alvos e permitiu eles escaparem.")
    if pontostotais >= 0:
        print("Você ganhou R$", pontostotais, "pelo serviço.")
    else:
        print("Você perdeu R$", pontostotais, "pelo serviço.")