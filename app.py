import random
print("Jogo adivinhe o numero")
numero_secreto=random.randint(1,15)

while True:
 chute=int(input("Digite um numero de 1 a 15:"))
 if chute==numero_secreto:
   print("Voce acertou!")
   break 
 else:
   print(" Errou tente novamente!")