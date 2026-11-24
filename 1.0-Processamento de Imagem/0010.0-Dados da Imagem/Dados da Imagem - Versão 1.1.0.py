########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
import cv2 as cv #opencv
import os
########################################################################
# Definições Gerais
########################################################################


NomeImagem = "./Imagens/" + "Girassol.png"
########################################################################
# Lendo a Imagem
########################################################################
imgBase = cv.imread(NomeImagem, cv.IMREAD_COLOR)
   
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
if imgBase is None:
   print("Não Foi Localizada a Imagem : ")
   exit()

########################################################################
# Recuperando os Dados da Imagem
########################################################################
# O .shape retorna uma tupla com as dimensoes da imagem, (altura, largura, canais(quantidade))

ImagemAltura = imgBase.shape[0]
ImagemLargura  = imgBase.shape[1]
ImagemNumCanais = imgBase.shape[2]  

# 
########################################################################
# Apresentando os Dados da Imagem
########################################################################
#
print ("")
print ("#######################################################################")
print ("# Dados da Imagem : " + NomeImagem)
print ("#######################################################################")
print ("# Largura da Imagem (pixel) ..: ", ImagemLargura )
print ("# Altura da Imagem (pixel) ...: ", ImagemAltura )
print ("# Número de Canais ...........: ", ImagemNumCanais )
print ("#######################################################################")
print ("")

########################################################################
# FIM DO PROGRAMA
########################################################################


