
#Importação da biblioteca colorama
from colorama import Fore, Style, init

# Inicializa o colorama para garantir o funcionamento correto nos terminais
init()

def obter_mensagem_nivel(nivel):
    """
    Função responsável por definir a cor e a mensagem da situação
    conforme o nível do reservatório informado.
    """
    if nivel == 1:
        return Fore.RED + "Nível 1 - Muito baixo (crítico)"
    elif nivel == 2:
        return Fore.YELLOW + "Nível 2 - Baixo"
    elif nivel == 3:
        return Fore.GREEN + "Nível 3 - Médio"
    elif nivel == 4:
        return Fore.CYAN + "Nível 4 - Alto"
    elif nivel == 5:
        return Fore.BLUE + "Nível 5 - Muito alto (alerta)"
    else:
        return Fore.WHITE + "Nível Desconhecido"

def simular_monitoramento():
    """
    Simula o monitoramento exibindo a situação do reservatório para cada nível.
    """
    # Lista armazenando os 5 níveis de água do reservatório
    niveis_reservatorio = [1, 2, 3, 4, 5]

    print("=== SISTEMA DE MONITORAMENTO DE NÍVEIS DE ÁGUA ===\n")

    # Percorre a lista de níveis e exibe a mensagem correspondente
    for nivel in niveis_reservatorio:
        mensagem_colorida = obter_mensagem_nivel(nivel)
        print(f"Situação atual: {mensagem_colorida}")
        
        # Restaura o estilo padrão do terminal após a exibição de cada mensagem
        print(Style.RESET_ALL, end="")

    print("\nSimulação concluída com sucesso!")

# Execução do sistema
if __name__ == "__main__":
    simular_monitoramento()