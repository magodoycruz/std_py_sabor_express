import os

def exibir_nome_restaurante():
    # Frescurinha de FSymbol para título bonitinho
    print('''
    █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
    ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
    ''')

def listar_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar Restaurante')
    print('4. Sair \n')

def escolher_opcoes():
    opcao_escolhida = int(input('Escolha uma opção: '))
    match opcao_escolhida:
        case 1: 
            cadastrar_restaurante()
        case 2:
            listar_restaurante()
        case 3:
            ativar_restaurante()
        case _:
            finalizar_app()

def finalizar_app():
    os.system('clear')
    print('Finalizando o programa...\n')

def cadastrar_restaurante():
    print('Cadastrar restaurante')

def listar_restaurante():
    print('Listar restaurantes')

def ativar_restaurante():
    print('Ativar restaurante')

def main():
    exibir_nome_restaurante()
    listar_opcoes()
    escolher_opcoes()

## Definindo como arquivo principal (main)
if __name__ == '__main__':
    main()