# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt
from pathlib import Path
import seaborn as sns 

# 
########################################################################
# Funções de Apoio
########################################################################
#
def LimpaTerminal ():
    if os.name == "nt":
       _ = os.system( "cls" )
    else:
      _ = os.system( "clear ")
    return ()

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeImagem = "Adicao.png" 
dirCaminhoImagem = "../../Imagens/" + NomeImagem

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
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagem)
   exit ()

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgColorida = cv.cvtColor(imgBase, cv.COLOR_BGR2RGB)


def desenhar_imagem(espaco,imagem):
    espaco.imshow( imgColorida ) # Pega a matriz numpy e renderiza os numeros como pixel visuais que formam a imagem
    espaco.set_title("Original", fontsize=11, weight='bold' ) #sempre sabe qual foi o ultimo grafico gerado e atribui o titulo


def desenhar_mapa_de_calor(espaco,imagem):
    heatmap=sns.heatmap (  
                           imgBase, 
                           annot=True, #valor numerico exato de cada pixel de 0 a 255
                           fmt="d",    #formato decimal
                           linewidth=1, #espessura da linha que separa cada pixel
                           cbar=True, #não exibe ou exibe a barra de cores
                           annot_kws={"size": 8}, #um dicionario de configuracoes extras para o texto, nesse caso o tamanho da fonte passa a ser 8
                           #cmap="blue", #paleta de cores, nesse caso está comentada, então o padrão
                           square=True, #força cada celula da matriz ser um quadrado 1x1
                           linecolor="k", #cor da linha que separa cada pixel, nesse caso preto blac(K)
                           ax=espaco,
                        ) # basicamente fazendo o mapa de calor d
    
    espaco.set_title("Visão Matricial da Imagem", fontsize=11, weight='bold' )
    


Grafico = plt.figure() #Abriu uma figura(quadro em branco) para colocar os graficos

espaco1 = Grafico.add_subplot(1,2,1) #Recorta a figura em 1 linha e 2 colunas, e seleciona o primeiro quadrante para colocar o grafico
espaco2 = Grafico.add_subplot(1,2,2)
desenhar_imagem(espaco1,imgColorida)
desenhar_mapa_de_calor(espaco2,imgBase)

plt.show()
exit()

########################################################################
# FIM DO PROGRAMA
########################################################################
