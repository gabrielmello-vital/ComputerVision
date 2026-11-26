#
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
# Para rodar: pip install numpy matplotlib scikit-image opencv-python
#
import cv2 as cv
import matplotlib.pyplot as plt

########################################################################
# Definições Gerais
########################################################################
NomeImagem = "Girassol.png"
dirCaminhoImagem = "./Imagens/" + NomeImagem

########################################################################
# Lendo a Imagem (OpenCV)
########################################################################
# cv.IMREAD_COLOR lê a imagem colorida com 3 canais na ordem B, G, R
# (azul, verde, vermelho), com valores inteiros de 0 a 255 (uint8).
# Se o PNG tiver transparência, o canal alfa é descartado.
imgBase = cv.imread(dirCaminhoImagem, cv.IMREAD_COLOR)

########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
# Diferente do io.imread do scikit-image (que dá erro), o cv.imread
# NÃO dá erro quando não acha o arquivo: só devolve None.
if imgBase is None:
   print("Não Foi Localizada a Imagem : ", dirCaminhoImagem)
   exit()

########################################################################
# Convertendo de OpenCV para SkImage / Matplotlib (BGR -> RGB)
########################################################################
# O OpenCV guarda as cores como B, G, R; o scikit-image e o Matplotlib
# esperam R, G, B. Sem essa troca, o vermelho e o azul aparecem trocados
# (as pétalas amarelas do girassol ficariam azuladas).
imgBaseRGB = cv.cvtColor(imgBase, cv.COLOR_BGR2RGB)

########################################################################
# Apresentando a Imagem
########################################################################
# Versões antigas deste exemplo usavam as funções de exibição do
# scikit-image:
#
#     io.imshow(imgBaseCV)
#     io.show()
#
# Elas foram DESCONTINUADAS no scikit-image 0.25 e serão REMOVIDAS na 0.27.
# Por baixo, elas já usavam o Matplotlib, então usamos o Matplotlib direto.
Grafico = plt.figure()

Grafico.add_subplot(1, 1, 1)
plt.imshow(imgBaseRGB)
plt.title("Imagem Lida com OpenCV (convertida para RGB)")

Grafico.tight_layout()
plt.show()

########################################################################
# FIM DO PROGRAMA
########################################################################