# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

########################################################################
# Definições Gerais
########################################################################

NomeImagem = "Adicao.png"
NomeOutput = "AdicaoOut.txt"
dirImagem = "Imagens"  
dirOutput = "Output"
dirAula = "1.0-Processamento de Imagem/0020.0-Imagem é uma Matriz"
dirCaminhoImagem = f"./Imagens/{NomeImagem}"
dirCaminhoOutput = f"./{dirAula}/{NomeOutput}"

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

########################################################################
# Apresentando a Matriz
########################################################################

fleOut = open(dirCaminhoOutput, 'w')
# Como o cv.imread devolve a imagem como uma matriz NumPy 2D (em escala de cinza),
# o for percorre essa matriz linha por linha: cada "row" é um vetor com as
# intensidades (0–255) dos pixels daquela linha, que é gravado no arquivo de saída
for row in imgBase: 
    print('|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|'.format(*row),  file=fleOut)

########################################################################
# FIM DO PROGRAMA
########################################################################
