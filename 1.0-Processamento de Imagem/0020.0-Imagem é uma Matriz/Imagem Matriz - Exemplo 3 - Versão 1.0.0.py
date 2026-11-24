# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import os
import matplotlib.pyplot as plt
from pathlib import Path
import seaborn as sns
import pandas as pd
import numpy as np

########################################################################
# Definições Gerais
########################################################################
#
NomeOutput1 = "AdicaoOutMatplotlib01.png"
NomeOutput2 = "AdicaoOutMatplotlib02.png"
dirOutput  = "Output"
NomeImagem = "Adicao.png"
dirAula = "1.0-Processamento de Imagem/0020.0-Imagem é uma Matriz"
dirCaminhoImagem = f"./Imagens/{NomeImagem}"
dirCaminhoOutput1 = f"./{dirAula}/{dirOutput}/{NomeOutput1}"
dirCaminhoOutput2 = f"./{dirAula}/{dirOutput}/{NomeOutput2}"
# 
########################################################################
# Lendo e Reduzindo a Imagem
########################################################################
#
imgBase = cv.imread ( dirCaminhoImagem, cv.IMREAD_GRAYSCALE)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if imgBase is None:
   print( "Não Foi Localizada a Imagem : ", NomeImagem)
   exit ()

# 
########################################################################
# Analisando as Dimensões da Imagem
########################################################################
#
# Pega o número de linhas (altura) e colunas (largura) da imagem,
# necessários para percorrer todos os pixels nos laços abaixo.
# Como a imagem foi lida em escala de cinza, o shape tem só 2 dimensões (linhas, colunas)
iLinhas = imgBase.shape[0]
iColunas = imgBase.shape[1]


Figura = plt.figure(figsize=(14,14))
# Binarizando: o que não é preto (0) vira branco (255) pois a imagem tem tom de cinza, não é totalmente branca o fundo
for iAux in range(iLinhas):
    for jAux in range(iColunas):
        if imgBase[iAux, jAux] > 0:
            imgBase[iAux, jAux] = 255

# 
########################################################################
# Apresentando a Matriz, Montando na mão.
########################################################################
#

# Percorre a imagem pixel a pixel (linha por linha, coluna por coluna) e escreve,
# em vermelho(r) e centralizado sobre cada pixel, o seu valor de intensidade (0–255).
# Obs.: no text() a ordem é (x, y) = (coluna, linha), por isso jAux vem antes de iAux.
# zfill(3) completa com zeros à esquerda: 7 → "007"
Grafico = Figura.add_subplot(1, 1, 1)
Grafico.imshow(imgBase, cmap='gray',vmin =0, vmax=255)
for iAux in range(iLinhas):
    for jAux in range(iColunas):
        Grafico.text(jAux, iAux, str(imgBase[iAux, jAux]).zfill(3), color='r', ha="center", va="center",fontsize=7 )

# Grafico.set_axis_off()
Figura.tight_layout()
Figura.savefig(dirCaminhoOutput1)
plt.show()

# 
########################################################################
# Invertendo a cor da Matriz
########################################################################
#

imgInvertida = imgBase.copy() # Pra não alterar a original

for iAux in range(iLinhas):
    for jAux in range(iColunas):
        imgInvertida[iAux, jAux] = 255 - imgBase[iAux, jAux]  #255 - valor, 255 vira 0 e 0 vira 255

Figura2 = plt.figure(figsize=(14,14))
Grafico2 = Figura2.add_subplot(1, 1, 1)
Grafico2.imshow(imgInvertida, cmap='gray', vmin=0, vmax=255)
for iAux in range(iLinhas): # Só escrevendo os valores dos pixel na imagem tal como o primeiro exemplo.
    for jAux in range(iColunas):
        Grafico2.text(jAux, iAux, str(imgInvertida[iAux, jAux]).zfill(3), color='r', ha="center", va="center",fontsize=7)

# Grafico.set_axis_off()
Figura2.tight_layout()
Figura2.savefig(dirCaminhoOutput2)
plt.savefig("1.0-Processamento de Imagem/0020.0-Imagem é uma Matriz/Output/saida_Imagem_Matriz.png")  

########################################################################
# FIM DO PROGRAMA
########################################################################
