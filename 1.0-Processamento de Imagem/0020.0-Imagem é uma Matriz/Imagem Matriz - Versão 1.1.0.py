#
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#
########################################################################
# Construindo a Matriz
########################################################################
#
CorPreta = (0, 0, 0)
ImagemMatriz = np.full((256, 256, 3), CorPreta, dtype=np.uint8)

# Moldura 1 - vermelho
ImagemMatriz[0:32, :, :3] = (0, 0, 255)            # linha superior
MatrizLinhaSuperior1 = ImagemMatriz.copy()

ImagemMatriz[:, :32, :3] = (0, 0, 255)             # coluna esquerda
MatrizColunaEsquerda1 = ImagemMatriz.copy()

ImagemMatriz[:, 224:256, :3] = (0, 0, 255)         # coluna direita
MatrizColunaDireita1 = ImagemMatriz.copy()

ImagemMatriz[224:, :, :3] = (0, 0, 255)            # linha inferior
MatrizLinhaInferior1 = ImagemMatriz.copy()

# Moldura 2 - laranja
ImagemMatriz[32:64, 32:224, :3] = (0, 128, 255)    # linha superior
MatrizLinhaSuperior2 = ImagemMatriz.copy()

ImagemMatriz[64:224, 32:64, :3] = (0, 128, 255)    # coluna esquerda
MatrizColunaEsquerda2 = ImagemMatriz.copy()

ImagemMatriz[64:224, 192:224, :3] = (0, 128, 255)  # coluna direita
MatrizColunaDireita2 = ImagemMatriz.copy()

ImagemMatriz[192:224, 32:224, :3] = (0, 128, 255)  # linha inferior
MatrizLinhaInferior2 = ImagemMatriz.copy()

# Moldura 3 - amarelo
ImagemMatriz[64:96, 64:192, :3] = (0, 255, 255)    # linha superior
MatrizLinhaSuperior3 = ImagemMatriz.copy()

ImagemMatriz[96:192, 64:96, :3] = (0, 255, 255)    # coluna esquerda
MatrizColunaEsquerda3 = ImagemMatriz.copy()

ImagemMatriz[96:192, 160:192, :3] = (0, 255, 255)  # coluna direita
MatrizColunaDireita3 = ImagemMatriz.copy()

ImagemMatriz[160:192, 64:192, :3] = (0, 255, 255)  # linha inferior
MatrizLinhaInferior3 = ImagemMatriz.copy()

# Centro - verde-limão
ImagemMatriz[96:160, 96:160, :3] = (0, 255, 128)
MatrizCentro = ImagemMatriz.copy()

#
########################################################################
# Apresentação dos Resultados (BGR -> RGB em cada imshow)
########################################################################
#
# Moldura 1
Grafico = plt.figure(figsize=(14, 4))

Grafico.add_subplot(1, 4, 1)
plt.imshow(cv.cvtColor(MatrizLinhaSuperior1, cv.COLOR_BGR2RGB))
plt.title("Linha Superior\nImagemMatriz[0:32, :]")

Grafico.add_subplot(1, 4, 2)
plt.imshow(cv.cvtColor(MatrizColunaEsquerda1, cv.COLOR_BGR2RGB))
plt.title("Coluna Esquerda\nImagemMatriz[:, :32]")

Grafico.add_subplot(1, 4, 3)
plt.imshow(cv.cvtColor(MatrizColunaDireita1, cv.COLOR_BGR2RGB))
plt.title("Coluna Direita\nImagemMatriz[:, 224:256]")

Grafico.add_subplot(1, 4, 4)
plt.imshow(cv.cvtColor(MatrizLinhaInferior1, cv.COLOR_BGR2RGB))
plt.title("Linha Inferior\nImagemMatriz[224:, :]")
plt.tight_layout()
plt.show()

# Moldura 2
Grafico = plt.figure(figsize=(14, 4))

Grafico.add_subplot(1, 4, 1)
plt.imshow(cv.cvtColor(MatrizLinhaSuperior2, cv.COLOR_BGR2RGB))
plt.title("Linha Superior\nImagemMatriz[32:64, 32:224]")

Grafico.add_subplot(1, 4, 2)
plt.imshow(cv.cvtColor(MatrizColunaEsquerda2, cv.COLOR_BGR2RGB))
plt.title("Coluna Esquerda\nImagemMatriz[64:224, 32:64]")

Grafico.add_subplot(1, 4, 3)
plt.imshow(cv.cvtColor(MatrizColunaDireita2, cv.COLOR_BGR2RGB))
plt.title("Coluna Direita\nImagemMatriz[64:224, 192:224]")

Grafico.add_subplot(1, 4, 4)
plt.imshow(cv.cvtColor(MatrizLinhaInferior2, cv.COLOR_BGR2RGB))
plt.title("Linha Inferior\nImagemMatriz[192:224, 32:224]")
plt.tight_layout()
plt.show()

# Moldura 3
Grafico = plt.figure(figsize=(14, 4))

Grafico.add_subplot(1, 4, 1)
plt.imshow(cv.cvtColor(MatrizLinhaSuperior3, cv.COLOR_BGR2RGB))
plt.title("Linha Superior\nImagemMatriz[64:96, 64:192]")

Grafico.add_subplot(1, 4, 2)
plt.imshow(cv.cvtColor(MatrizColunaEsquerda3, cv.COLOR_BGR2RGB))
plt.title("Coluna Esquerda\nImagemMatriz[96:192, 64:96]")

Grafico.add_subplot(1, 4, 3)
plt.imshow(cv.cvtColor(MatrizColunaDireita3, cv.COLOR_BGR2RGB))
plt.title("Coluna Direita\nImagemMatriz[96:192, 160:192]")

Grafico.add_subplot(1, 4, 4)
plt.imshow(cv.cvtColor(MatrizLinhaInferior3, cv.COLOR_BGR2RGB))
plt.title("Linha Inferior\nImagemMatriz[160:192, 64:192]")
plt.tight_layout()
plt.show()

# Centro
Grafico = plt.figure()

Grafico.add_subplot(1, 1, 1)
plt.imshow(cv.cvtColor(MatrizCentro, cv.COLOR_BGR2RGB))
plt.title("Centro\nImagemMatriz[96:160, 96:160]")
plt.tight_layout()
plt.show()
plt.savefig("1.0-Processamento de Imagem/0020.0-Imagem é uma Matriz/Output/saida_Imagem_Matriz.png") 
########################################################################
# FIM DO PROGRAMA
########################################################################