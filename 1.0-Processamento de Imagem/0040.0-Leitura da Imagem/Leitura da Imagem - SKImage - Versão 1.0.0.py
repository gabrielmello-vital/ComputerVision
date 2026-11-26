########################################################################
# Importação das Bibliotecas Necessárias
########################################################################

# Para rodar: pip install numpy matplotlib scikit-image opencv-python

from skimage import io
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
# O io.imread DÁ ERRO (FileNotFoundError) quando não acha o arquivo,
# por isso usamos try/except.
try:
   imgBase = io.imread(dirCaminhoImagem)
except FileNotFoundError:
   print("Não Foi Localizada a Imagem : ", dirCaminhoImagem)
   exit()

########################################################################
# Apresentando a Imagem
########################################################################
# Versões antigas deste exemplo usavam as funções de exibição do próprio
# scikit-image:
#
#     io.imshow(imgBase)
#     io.show()
#
# Elas foram DESCONTINUADAS no scikit-image 0.25 e serão REMOVIDAS na 0.27.
# Por baixo, elas já usavam o Matplotlib, então o caminho recomendado pela
# própria biblioteca é usar o Matplotlib diretamente, como abaixo.
# O Matplotlib também usa a ordem R, G, B, igual ao scikit-image:
# a imagem é mostrada direto, sem cvtColor.
# (Se a imagem tivesse sido lida com o OpenCV, que usa B, G, R,
# seria preciso converter antes, senão o vermelho e o azul trocam.)
Grafico = plt.figure()

Grafico.add_subplot(1, 1, 1)
plt.imshow(imgBase)
plt.title("Imagem Original (SkImage)")

Grafico.tight_layout()
plt.show()

########################################################################
# FIM DO PROGRAMA
########################################################################