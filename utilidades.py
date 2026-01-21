#!/usr/bin/env python3
"""
Arquivo de utilidades para o jogo de adivinhação
Contém funções auxiliares reutilizáveis
"""

import random


def gerar_numero_secreto(minimo=1, maximo=100):
    """
    Gera um número aleatório entre mínimo e máximo
    
    Args:
        minimo: número mínimo (padrão: 1)
        maximo: número máximo (padrão: 100)
    
    Returns:
        Um número aleatório
    """
    return random.randint(minimo, maximo)


def validar_tentativa(tentativa, minimo=1, maximo=100):
    """
    Valida se a tentativa do usuário está dentro do intervalo válido
    
    Args:
        tentativa: número que o usuário tentou
        minimo: número mínimo permitido
        maximo: número máximo permitido
    
    Returns:
        True se válido, False caso contrário
    """
    return minimo <= tentativa <= maximo


def dar_dica(tentativa, numero_secreto):
    """
    Fornece uma dica ao usuário sobre sua tentativa
    
    Args:
        tentativa: número que o usuário tentou
        numero_secreto: número que precisa ser adivinhado
    
    Returns:
        Uma mensagem de dica
    """
    diferenca = abs(tentativa - numero_secreto)
    
    if tentativa < numero_secreto:
        if diferenca > 20:
            return "Muito baixo! Tente um número maior."
        elif diferenca > 10:
            return "Baixo! Você está chegando perto."
        else:
            return "Quase! Um pouco mais alto."
    else:
        if diferenca > 20:
            return "Muito alto! Tente um número menor."
        elif diferenca > 10:
            return "Alto! Você está chegando perto."
        else:
            return "Quase! Um pouco mais baixo."


def mostrar_mensagem_boas_vindas():
    """Exibe uma mensagem de boas-vindas ao jogo"""
    print("=" * 50)
    print("🎮 Bem-vindo ao Jogo de Adivinhação! 🎮")
    print("=" * 50)
    print("Eu pensei em um número entre 1 e 100.")
    print("Você consegue adivinhar qual é?")
    print()


def mostrar_resultado_final(acertou, tentativas, numero_secreto):
    """
    Mostra o resultado final do jogo
    
    Args:
        acertou: True se o usuário acertou, False caso contrário
        tentativas: número de tentativas realizadas
        numero_secreto: o número secreto
    """
    print()
    print("=" * 50)
    if acertou:
        print(f"🎉 Parabéns! Você acertou em {tentativas} tentativa(s)!")
        print(f"O número era {numero_secreto}!")
    else:
        print(f"😔 Que pena! O número era {numero_secreto}.")
        print("Não desista, tente novamente!")
    print("=" * 50)
