def play_01():
    print('Python na Escola de Programação Alura \n')

    nome = 'Marcela'
    idade = 36

    print(f'Meu nome é {nome} e eu tenho {idade} anos.\n')

    print('a\nl\nu\nr\na\n')

    pi = 3.14159
    pi_arredondado = round(pi, 2) # Arredonda, exibindo 2 casas decimais (segundo parametro)
    print(f'O valor arredondado de pi é {pi_arredondado}')

def play_02():
    # Determinar se o numero solicitado é par ou impar:
    numero_escolhido = int(input('Digite um número:'))
    resto_da_divisao_por_dois = numero_escolhido%2

    if resto_da_divisao_por_dois == 0:
        print('Este numero é PAR')
    else: 
        print('Este numero é IMPAR')

def play_03():
    # Classificar conforme idade do usuario se ele é uma criança, adolescente ou adulto
    idade = int(input('Digite a sua idade:'))
    if idade <=12:
        print('Você é uma criança')
    elif idade > 12 and idade <= 18:
        print('Vocẽ é um adolescente')
    else:
        print('Você é um adulto')

def play_04():
    # a partir de coordenadas x e y dadas pelo usuário, determinar em qual quadrante do plano cartesiano o ponto se encontra
    coordenada_x = int(input('Digite o valor da coordenada X:'))
    coordenada_y = int(input('Agora digite o valor da coordenada Y:'))

    if coordenada_x > 0 and coordenada_y > 0:
        print('Coordenada está no primeiro quadrante')
    elif coordenada_x < 0 and coordenada_y > 0:
        print('Coordenada está no segundo quadrante')
    elif coordenada_x < 0 and coordenada_y < 0:
        print('Coordenada está no terceiro quadrante')
    elif coordenada_x > 0 and coordenada_y < 0:
        print('Coordenada está no quarto quadrante')
    else:
        print('Coordenada está no centro de origem')
play_04()