#
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import numpy as np
import matplotlib.pyplot as plt

#
########################################################################
# Construindo a Matriz
########################################################################
#
Matriz = np.zeros([256, 256], dtype=np.uint8)   # 256 x 256, tudo 0 (preto), 1 número por pixel

# Moldura 1 - intensidade 40
Matriz[0:32, :] = 40            # linha superior
MatrizLinhaSuperior1 = Matriz.copy()

Matriz[:, :32] = 40             # coluna esquerda
MatrizColunaEsquerda1 = Matriz.copy()

Matriz[:, 224:256] = 40         # coluna direita
MatrizColunaDireita1 = Matriz.copy()

Matriz[224:, :] = 40            # linha inferior
MatrizLinhaInferior1 = Matriz.copy()

# Moldura 2 - intensidade 80
Matriz[32:64, 32:224] = 80      # linha superior
MatrizLinhaSuperior2 = Matriz.copy()

Matriz[64:224, 32:64] = 80      # coluna esquerda
MatrizColunaEsquerda2 = Matriz.copy()

Matriz[64:224, 192:224] = 80    # coluna direita
MatrizColunaDireita2 = Matriz.copy()

Matriz[192:224, 32:224] = 80    # linha inferior
MatrizLinhaInferior2 = Matriz.copy()

# Moldura 3 - intensidade 160
Matriz[64:96, 64:192] = 160     # linha superior
MatrizLinhaSuperior3 = Matriz.copy()

Matriz[96:192, 64:96] = 160     # coluna esquerda
MatrizColunaEsquerda3 = Matriz.copy()

Matriz[96:192, 160:192] = 160   # coluna direita
MatrizColunaDireita3 = Matriz.copy()

Matriz[160:192, 64:192] = 160   # linha inferior
MatrizLinhaInferior3 = Matriz.copy()

# Centro - intensidade 220
Matriz[96:160, 96:160] = 220
MatrizCentro = Matriz.copy()

#
########################################################################
# Apresentação dos Resultados
# cmap='viridis'        -> pinta cada intensidade com uma cor (roxo = baixo, amarelo = alto)
# vmin=0, vmax=255      -> a escala vai sempre de 0 a 255, então cada intensidade
#                          tem a MESMA cor em todas as figuras
########################################################################
#
# Moldura 1
Grafico = plt.figure(figsize=(14, 4))

Grafico.add_subplot(1, 4, 1)
plt.imshow(MatrizLinhaSuperior1, cmap='viridis', vmin=0, vmax=255)
plt.title("Linha Superior\nMatriz[0:32, :]")

Grafico.add_subplot(1, 4, 2)
plt.imshow(MatrizColunaEsquerda1, cmap='viridis', vmin=0, vmax=255)
plt.title("Coluna Esquerda\nMatriz[:, :32]")

Grafico.add_subplot(1, 4, 3)
plt.imshow(MatrizColunaDireita1, cmap='viridis', vmin=0, vmax=255)
plt.title("Coluna Direita\nMatriz[:, 224:256]")

Grafico.add_subplot(1, 4, 4)
plt.imshow(MatrizLinhaInferior1, cmap='viridis', vmin=0, vmax=255)
plt.title("Linha Inferior\nMatriz[224:, :]")
plt.tight_layout()
plt.show()

# Moldura 2
Grafico = plt.figure(figsize=(14, 4))

Grafico.add_subplot(1, 4, 1)
plt.imshow(MatrizLinhaSuperior2, cmap='viridis', vmin=0, vmax=255)
plt.title("Linha Superior\nMatriz[32:64, 32:224]")

Grafico.add_subplot(1, 4, 2)
plt.imshow(MatrizColunaEsquerda2, cmap='viridis', vmin=0, vmax=255)
plt.title("Coluna Esquerda\nMatriz[64:224, 32:64]")

Grafico.add_subplot(1, 4, 3)
plt.imshow(MatrizColunaDireita2, cmap='viridis', vmin=0, vmax=255)
plt.title("Coluna Direita\nMatriz[64:224, 192:224]")

Grafico.add_subplot(1, 4, 4)
plt.imshow(MatrizLinhaInferior2, cmap='viridis', vmin=0, vmax=255)
plt.title("Linha Inferior\nMatriz[192:224, 32:224]")
plt.tight_layout()
plt.show()

# Moldura 3
Grafico = plt.figure(figsize=(14, 4))

Grafico.add_subplot(1, 4, 1)
plt.imshow(MatrizLinhaSuperior3, cmap='viridis', vmin=0, vmax=255)
plt.title("Linha Superior\nMatriz[64:96, 64:192]")

Grafico.add_subplot(1, 4, 2)
plt.imshow(MatrizColunaEsquerda3, cmap='viridis', vmin=0, vmax=255)
plt.title("Coluna Esquerda\nMatriz[96:192, 64:96]")

Grafico.add_subplot(1, 4, 3)
plt.imshow(MatrizColunaDireita3, cmap='viridis', vmin=0, vmax=255)
plt.title("Coluna Direita\nMatriz[96:192, 160:192]")

Grafico.add_subplot(1, 4, 4)
plt.imshow(MatrizLinhaInferior3, cmap='viridis', vmin=0, vmax=255)
plt.title("Linha Inferior\nMatriz[160:192, 64:192]")
plt.tight_layout()
plt.show()

# Centro (imagem final)
Grafico = plt.figure(figsize=(5, 5))

Grafico.add_subplot(1, 1, 1)
plt.imshow(MatrizCentro, cmap='viridis', vmin=0, vmax=255)
plt.title("Centro\nMatriz[96:160, 96:160]")
plt.tight_layout()
plt.show()
plt.savefig("1.0-Processamento de Imagem/0020.0-Imagem é uma Matriz/Output/saida_Imagem_Matriz_Intensidade.png") 
########################################################################
# FIM DO PROGRAMA
########################################################################