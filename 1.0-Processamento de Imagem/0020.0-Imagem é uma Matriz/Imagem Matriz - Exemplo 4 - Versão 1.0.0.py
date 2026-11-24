#
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
# Para rodar:  pip install -r requirements.txt  (ver COMO RODAR.txt)
#
import cv2 as cv
import matplotlib.pyplot as plt

########################################################################
# Definições Gerais
########################################################################

NomeImagem = "Adicao.png"
dirCaminhoImagem = "./Imagens/" + NomeImagem

dirAula = "./1.0-Processamento de Imagem/0021.0-Operações Usando NumPy/"
NomeOutput = "Imagem Matriz - Exemplo 3.png"
dirCaminhoOutput = dirAula + "Output/" + NomeOutput


########################################################################
# Lendo a Imagem em Tons de Cinza
########################################################################
# cv.IMREAD_GRAYSCALE lê a imagem com 1 canal só (cinza): cada pixel
# vira um único número de 0 (preto) a 255 (branco).
# O resultado é uma matriz NumPy 2D (linhas x colunas).
imgBase = cv.imread(dirCaminhoImagem, cv.IMREAD_GRAYSCALE)

########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
# Se o caminho estiver errado, o OpenCV não dá erro: só devolve None.
# Por isso é preciso conferir antes de usar a imagem.
if imgBase is None:
   print("Não Foi Localizada a Imagem : ", dirCaminhoImagem)
   exit()

#
########################################################################
# Recuperando as Dimensões da Imagem
########################################################################
#
# shape devolve (linhas, colunas). Ex.: (28, 28) para Adicao.png.
iLinhas = imgBase.shape[0]    # altura da imagem
iColunas = imgBase.shape[1]   # largura da imagem

#
########################################################################
# Apresentando a Matriz
########################################################################
#
# Desenha a imagem e escreve, em cima de cada pixel, o seu valor (0 a 255).
# figsize grande e fontsize pequeno para os números caberem sem se encostar.
fig = plt.figure(figsize=(14, 14))

ax = fig.add_subplot(1, 1, 1)

# cmap="Oranges": 0 fica branco e 255 fica laranja escuro.
# vmin=0 e vmax=255 fixam a escala (sem eles o Matplotlib ajusta o
# contraste sozinho com base no menor e no maior valor da imagem).
ax.imshow(imgBase, cmap="Oranges", vmin=0, vmax=255)

# Percorre a matriz pixel a pixel. Aqui o laço é necessário: o objetivo
# é escrever um texto para cada pixel, e isso não dá para vetorizar.
# No text() a ordem é (x, y) = (coluna, linha), por isso j vem antes de i.
# zfill(3) completa com zeros à esquerda: 7 -> "007", 45 -> "045".
# Fundo escuro (valor > 128) recebe número branco; fundo claro, número preto.
for i in range(iLinhas):
    for j in range(iColunas):
        if imgBase[i, j] > 128:
            CorTexto = "white"
        else:
            CorTexto = "black"
        ax.text(j, i, str(imgBase[i, j]).zfill(3), color=CorTexto, ha="center", va="center", fontsize=7)

ax.set_axis_off()

fig.tight_layout()
fig.savefig(dirCaminhoOutput)   # salvar ANTES do show (depois dele a figura fica vazia)
plt.show()

########################################################################
# FIM DO PROGRAMA
########################################################################