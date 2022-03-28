# APENAS FUNÇÃO: Você está desenvolvendo um software de reconhecimento de caracteres de uma imagem.
# Cada sequência de textos retornados pelo software possui uma posição cartesiana X e Y de onde um texto
# se encontra na imagem. Crie uma função que recebe como entrada a altura e comprimento padrões do texto,
# a posição X e Y de um texto e a posição X e Y de outro texto. Como processamento da função, deve-se calcular
# se ambos os textos estão na mesma linha ou não, ao verificar se o espaço cartesiano Y que ocupam possui interseção.
# Como resposta da função, deve-se retornar um valor inteiro que representa 0 se os textos não estão na mesma linha
# ou 1. se os textos estão na mesma linha.Em seguida, caso ambos os textos estejam na mesma linha, deve-se criar
# outra função que diga qual dos dois textos vem primeiro. Como entrada da função, deve digitar o valor Xleft e
# Xright do primeiro e também do segundo texto. Realize um processamento que como resposta da função, retorne o
# valor inteiro 0. se ambos os textos estão sobrepostos, 1. se o primeiro texto está a esquerda do segundo ou 2.
# se o primeiro texto está a direita do segundo.

def texto_primeiro(xleft1,xleft2,xrigh1,xright2):
    if xleft1 == xleft2 and xrigh1 == xright2:
        print(0)
    elif xleft1 == xleft2 and xrigh1 < xright2:
        print(1)
    elif xleft1 == xleft2 and xrigh1 > xright2:
        print(2)


def comprimento_e_altura_de_dois_textos(alt_pad,comp_pad,posx1,posy1,posx2,posy2):

    n = 0

    if posy1 >= posy2 and posy2 <= posy1 + alt_pad:
        print(n)
        if n == 0:
            xleft1 = float(input('Digite a posição da esquerda do primeiro texto:\n'))
            xleft2 = float(input('Digite a posição da esquerda do segundo texto:\n'))
            xright1 = float(input('Digite a posição da direita do primeiro texto:\n'))
            xright2 = float(input('Digite a posição da direita do primeiro texto:\n'))

            posicao_referencial = texto_primeiro(xleft1,xleft2,xright1,xright2)
            print(posicao_referencial)

    else:
        print(n + 1)



alt_pad = float(input('Digite a altura padão do texto:\n'))
comp_pad = float(input('Digite o comprimento padão do texto:\n'))

posx1 = float(input('Digite a posição x do primeiro texto:\n'))
posy1 = float(input('Digite a posição y do primeiro texto:\n'))
posx2 = float(input('Digite a posição x do segundo texto:\n'))
posy2 = float(input('Digite a posição y do segundo texto:\n'))

estaosobrepostos = comprimento_e_altura_de_dois_textos(alt_pad,comp_pad,posx1,posy1,posx2,posy2)

