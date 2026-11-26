#
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
# Para rodar: pip install numpy matplotlib scikit-image opencv-python
import cv2 as cv

########################################################################
# Definições Gerais
########################################################################
NomeImagem = "Girassol.png"
NomeJanela = "Imagem Base"   
dirCaminhoImagem = "./Imagens/" + NomeImagem

########################################################################
# Lendo a Imagem
########################################################################
# cv.IMREAD_COLOR lê a imagem colorida com 3 canais na ordem B, G, R
# (azul, verde, vermelho), com valores inteiros de 0 a 255 (uint8).
imgBase = cv.imread(dirCaminhoImagem, cv.IMREAD_COLOR)

########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
# O cv.imread NÃO dá erro quando não acha o arquivo: só devolve None.
if imgBase is None:
   print("Não Foi Localizada a Imagem : ", dirCaminhoImagem)
   exit()


########################################################################
# Apresentando a Imagem
########################################################################
# A imagem foi lida pelo OpenCV (BGR) e vai ser mostrada pelo OpenCV (BGR),
# então não precisa de cvtColor: as cores já estão na ordem certa.
# imshow abre a janela com o título NomeJanela.
# waitKey(0) deixa o programa parado até alguma tecla ser apertada
# (com a janela selecionada). Sem ele, a janela abre e fecha na hora.
# destroyAllWindows fecha todas as janelas abertas pelo OpenCV.
cv.imshow(NomeJanela, imgBase)
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################