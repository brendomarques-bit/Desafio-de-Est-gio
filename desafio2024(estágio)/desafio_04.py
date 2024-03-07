def descobrir_interruptores():
    # Inicialmente, todos os interruptores estão desligados
    interruptor1 = False
    interruptor2 = False
    interruptor3 = False

    # Primeira ida
    interruptor1 = True  # Ligar o primeiro interruptor por alguns minutos
    interruptor2 = True  # Ligar o segundo interruptor
    # O terceiro interruptor permanece desligado

    # Segunda ida
    # Verificar o estado das lâmpadas
    l1 = interruptor1  # Estado da lâmpada controlada pelo primeiro interruptor
    l2 = interruptor2  # Estado da lâmpada controlada pelo segundo interruptor
    l3 = interruptor3  # Estado da lâmpada controlada pelo terceiro interruptor

    # Identificar qual interruptor controla cada lâmpada
    if l1:
        print("O interruptor 1 controla a primeira lâmpada.")
    if l2:
        print("O interruptor 2 controla a segunda lâmpada.")
    if not l3:
        print("O interruptor 3 controla a terceira lâmpada.")

# Chamar a função para descobrir os interruptores
descobrir_interruptores()