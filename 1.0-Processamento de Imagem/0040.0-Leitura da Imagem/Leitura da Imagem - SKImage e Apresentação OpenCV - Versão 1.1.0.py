#
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################

# Para rodar: pip install numpy matplotlib scikit-image opencv-python

import cv2 as cv
from skimage import io
from skimage.util import img_as_ubyte   # local oficial da função no scikit-image
import matplotlib.pyplot as plt

########################################################################
# Definições Gerais
########################################################################

NomeImagem = "Girassol.png"
dirCaminhoImagem = "./Imagens/" + NomeImagem


########################################################################
# Lendo a Imagem (scikit-image)
########################################################################

# io.imread devolve a imagem como matriz NumPy (linhas x colunas x canais),
# com as cores na ordem R, G, B (vermelho, verde, azul).
# Se o PNG tiver transparência, vem um 4º canal (alfa): R, G, B, A.
# Diferente do cv.imread (que devolve None quando não acha o arquivo),
# o io.imread DÁ ERRO (FileNotFoundError). Por isso usamos try/except.

try:
   imgBase = io.imread(dirCaminhoImagem)
except FileNotFoundError:
   print("Não Foi Localizada a Imagem : ", dirCaminhoImagem)
   exit()

########################################################################
# Convertendo de SkImage para OpenCV
########################################################################

# 1) img_as_ubyte: garante que os valores estejam no formato do OpenCV,
#    inteiros de 0 a 255 (uint8). Algumas funções do scikit-image devolvem
#    números decimais de 0.0 a 1.0; aqui eles viram 0 a 255.
#    Se a imagem já for uint8 (o normal para PNG e JPG), nada muda.
imgBaseCV = img_as_ubyte(imgBase)

# 2) cvtColor RGB -> BGR: o scikit-image guarda as cores como R, G, B,
#    mas o OpenCV espera B, G, R. Sem essa troca, o vermelho e o azul
#    aparecem trocados na janela (ex.: as pétalas amarelas ficariam azuis).
#    Se a imagem tiver canal alfa, ele é descartado nesta conversão.
imgBaseCV = cv.cvtColor(imgBaseCV, cv.COLOR_RGB2BGR)

########################################################################
# Apresentando a Imagem OpenCv
########################################################################

# imshow abre uma janela com o título "Janela Base".
# waitKey(0) deixa o programa parado até alguma tecla ser apertada
# (com a janela selecionada). Sem ele, a janela abre e fecha na hora.
# destroyAllWindows fecha todas as janelas abertas pelo OpenCV.
cv.imshow("Leitura com OpenCv", imgBaseCV)
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################