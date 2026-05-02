# Sistema de monitoramento de um reservatório de água

import time
from random import randint
from colorama import Fore, Style

situacao = ["Muito baixo (crítico)", "Baixo", "Médio", "Alto", "Muito alto (alerta)"]

# função criada para definir as cores de cada mensagem informativa
def monitoramento(nivel):

    # ajusta o nível para o índice da lista (listas começam em 0)
    mensagem = situacao[nivel-1]

    if nivel == 1:
        print(Fore.RED + mensagem)
    elif nivel == 2:
        print(Fore.YELLOW + mensagem)
    elif nivel == 3:
        print(Fore.GREEN + mensagem)
    elif nivel == 4:
        print(Fore.CYAN + mensagem)
    elif nivel == 5:
        print(Fore.BLUE + mensagem)

    print(Style.RESET_ALL)

while True:
    nivel_reservatorio = randint(1, 5)
    monitoramento(nivel_reservatorio)
    
    # timer para a mensagem ser exibida a cada 5 segundos na tela
    time.sleep(5)