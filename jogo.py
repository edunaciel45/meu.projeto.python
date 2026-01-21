#!/usr/bin/env python3
"""
Jogo de Adivinhação de Números
Arquivo principal do jogo
"""

from utilidades import (
    gerar_numero_secreto,
    validar_tentativa,
    dar_dica,
    mostrar_mensagem_boas_vindas,
    mostrar_resultado_final
)


def obter_tentativa_usuario():
    """
    Solicita e retorna a tentativa do usuário
    
    Returns:
        Número digitado pelo usuário ou None se inválido
    """
    try:
        tentativa = int(input("Digite seu palpite: "))
        return tentativa
    except ValueError:
        print("❌ Por favor, digite apenas números!")
        return None


def jogar():
    """Função principal que executa o jogo"""
    # Configuração inicial
    numero_secreto = gerar_numero_secreto(1, 100)
    tentativas = 0
    max_tentativas = 7
    
    # Mensagem de boas-vindas
    mostrar_mensagem_boas_vindas()
    
    # Loop principal do jogo
    while tentativas < max_tentativas:
        tentativas += 1
        tentativas_restantes = max_tentativas - tentativas
        
        print(f"\n📊 Tentativa {tentativas} de {max_tentativas}")
        if tentativas_restantes > 0:
            print(f"💡 Você ainda tem {tentativas_restantes} tentativa(s) restante(s)")
        
        # Obtém a tentativa do usuário
        tentativa = obter_tentativa_usuario()
        
        # Verifica se a entrada foi válida
        if tentativa is None:
            tentativas -= 1  # Não conta tentativa inválida
            continue
        
        # Valida se está no intervalo
        if not validar_tentativa(tentativa, 1, 100):
            print("❌ Por favor, digite um número entre 1 e 100!")
            tentativas -= 1  # Não conta tentativa inválida
            continue
        
        # Verifica se acertou
        if tentativa == numero_secreto:
            mostrar_resultado_final(True, tentativas, numero_secreto)
            return
        
        # Fornece dica
        dica = dar_dica(tentativa, numero_secreto)
        print(f"💭 {dica}")
    
    # Se chegou aqui, esgotou as tentativas
    mostrar_resultado_final(False, tentativas, numero_secreto)


def main():
    """Função principal do programa"""
    jogar()
    
    # Pergunta se quer jogar novamente
    while True:
        resposta = input("\n🔄 Deseja jogar novamente? (s/n): ").lower()
        if resposta in ['s', 'sim', 'y', 'yes']:
            print("\n" + "=" * 50)
            jogar()
        elif resposta in ['n', 'não', 'nao', 'no']:
            print("\n👋 Obrigado por jogar! Até a próxima!")
            break
        else:
            print("❌ Por favor, digite 's' para sim ou 'n' para não.")


if __name__ == "__main__":
    main()
