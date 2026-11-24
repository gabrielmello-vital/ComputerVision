#
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################

# Para rodar:  pip install numpy matplotlib scikit-image opencv-python  (ver COMO_RODAR.txt)

import matplotlib.pyplot as plt

# Funções do scikit-image que criam "elementos estruturantes": matrizes
# pequenas de 0 e 1 com um formato (losango, disco, estrela...).
# square, rectangle e cube foram substituídas por footprint_rectangle,
# porque as antigas serão removidas do scikit-image na versão 0.27.
from skimage.morphology import (footprint_rectangle, diamond, disk,octagon, star, octahedron, ball)

########################################################################
# Definições Gerais
########################################################################

dirAula = "./1.0-Processamento de Imagem/0021.0-Operações Usando NumPy/"
NomeOutput = "Operações Usando Numpy - Exemplo 2.png"
dirCaminhoOutput = dirAula + "Output/" + NomeOutput

########################################################################
# Criando os Elementos Estruturantes 2D
########################################################################

# Dicionário no formato  "título": matriz.
# Cada função devolve uma matriz NumPy (uint8) com 1 onde está a forma
# e 0 fora dela. Ex.: diamond(1) ->  0 1 0
#                                    1 1 1
#                                    0 1 0
# diamond(7) tem raio 7, então a matriz é 15 x 15 (7 + 1 + 7).
# Para ver outras formas, é só tirar o # da linha correspondente.
Elementos2D = {
    "Quadrado 15x15":   footprint_rectangle((15, 15)),
    "Retângulo 15x10":  footprint_rectangle((15, 10)),
    "diamond(7)":       diamond(7),
    "disk(7)":          disk(7),
    "octagon(7, 4)":    octagon(7, 4),
    "star(5)":          star(5),
}

########################################################################
# Criando os Elementos Estruturantes 3D
########################################################################

# Mesma ideia, mas em 3 dimensões (matriz 11 x 11 x 11 de 0 e 1).

Elementos3D = {
    "Cubo 11x11x11":  footprint_rectangle((11, 11, 11)),
    "octahedron(5)":  octahedron(5),
    "ball(5)":        ball(5),
}

########################################################################
# Apresentação dos Resultados
########################################################################
# A folha é dividida numa grade 3 x 3 (cabem 9 elementos: 6 em 2D e
# 3 em 3D). Posicao indica em qual quadrinho o próximo será desenhado.
Grafico = plt.figure(figsize=(8, 8))

Posicao = 1
for Titulo, Elemento in Elementos2D.items():

    # Mostra no terminal a matriz de 0 e 1 (prova de que é só uma matriz)
    print(Titulo)
    print(Elemento)

    Eixo = Grafico.add_subplot(3, 3, Posicao)

    # Pinta a matriz: 0 e 1 recebem cores diferentes da paleta "Paired".
    # vmin=0 e vmax=12 fixam a escala da paleta (ela tem 12 cores).
    Eixo.imshow(Elemento, cmap="Paired", vmin=0, vmax=12)

    # Escreve o valor (0 ou 1) no centro de cada célula.
    # No text() a ordem é (x, y) = (coluna, linha), por isso j vem antes de i.
    for i in range(Elemento.shape[0]):
        for j in range(Elemento.shape[1]):
            Eixo.text(j, i, Elemento[i, j], ha="center", va="center", color="w")

    Eixo.set_axis_off()
    Eixo.set_title(Titulo)
    Posicao += 1

# Para mostrar os elementos 3D

for Titulo, Elemento in Elementos3D.items():
    Eixo = Grafico.add_subplot(3, 3, Posicao, projection="3d")
    Eixo.voxels(Elemento)   # desenha um cubinho para cada 1 da matriz
    Eixo.set_title(Titulo)
    Posicao += 1

plt.tight_layout()
plt.savefig(dirCaminhoOutput)   # salvar ANTES do show (depois dele a figura fica vazia)
plt.show()

########################################################################
# FIM DO PROGRAMA
########################################################################