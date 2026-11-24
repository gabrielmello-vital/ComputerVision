########################################################################
# Importação das Bibliotecas Necessárias
########################################################################

import numpy as np
from skimage import data
import matplotlib.pyplot as plt
from pathlib import Path

########################################################################
# Definições Gerais
########################################################################

dirAula = "./1.0-Processamento de Imagem/0021.0-Operações Usando NumPy/"
NomeOutput = "Operações Usando Numpy - Exemplo 1.png"
dirCaminhoOutput = dirAula + "Output/" + NomeOutput


Limiar = 87          # pixels com valor abaixo disso viram brancos
PassoDiagonal = 4    # quantas colunas a linha anda a cada linha que desce

########################################################################
# Recupera a Imagem da Base de Dados
########################################################################

# data.camera() é uma foto de exemplo que já vem dentro do scikit-image:
# tons de cinza, matriz 512 x 512, tipo uint8 (valores de 0 a 255).
imgCamera = data.camera()

# .copy() faz uma cópia independente. Sem ela, imgOriginal seria só outro
# nome para a mesma matriz e também sofreria as alterações abaixo.
imgOriginal = imgCamera.copy()

iLinhas = imgCamera.shape[0]    # altura da imagem
iColunas = imgCamera.shape[1]   # largura da imagem

########################################################################
# Preenche de Branco o Que Estiver Dentro da Regra (pixels escuros)
########################################################################

# Máscara booleana: a comparação é feita em todos os pixels de uma vez e
# gera uma matriz de True/False do mesmo tamanho da imagem.
#   pixel 40  -> True  (vai virar branco)
#   pixel 150 -> False (não muda)
# Em seguida, só as posições True recebem 255, sem precisar de laço.
Mascara = imgCamera < Limiar
imgCamera[Mascara] = 255
imgMascara = imgCamera.copy ()

########################################################################
# Inserindo Linhas
########################################################################

# IndiceX = [0, 1, 2, ..., 511]               -> número da linha
# IndiceY = [0, 4, 8, ..., 508, 0, 4, ...]    -> número da coluna
# O % (resto da divisão) faz a coluna "dar a volta" ao chegar no fim.
# O NumPy junta os dois vetores em pares (linha, coluna) e pinta de preto
# os pixels (0,0), (1,4), (2,8)... formando 4 linhas pontilhadas.
IndiceX = np.arange(iLinhas)
IndiceY = (PassoDiagonal * IndiceX) % iColunas
imgCamera[IndiceX, IndiceY] = 0
imgLinhas = imgCamera.copy()

########################################################################
# Desenha o Círculo e Preenche de Preto o Externo
########################################################################

# np.ogrid devolve dois vetores com a posição de cada pixel:
#  X -> número da linha,  formato (512, 1)  (vetor "em pé")
#  Y -> número da coluna, formato (1, 512)  (vetor "deitado")
# Ao fazer contas entre os dois, o NumPy completa sozinho a tabela 512 x 512
# (broadcasting), sem montar duas matrizes inteiras na memória.
X, Y = np.ogrid[:iLinhas, :iColunas]

CentroX = iLinhas / 2
CentroY = iColunas / 2
Raio = min(iLinhas, iColunas) / 2   # min() também funciona em imagem retangular

# Equação do círculo: (x - cx)² + (y - cy)² > r²  ->  pixel FORA do círculo
MascaraForaCirculo = (X - CentroX)**2 + (Y - CentroY)**2 > Raio**2
imgCamera[MascaraForaCirculo] = 0 # pinta tudo que está fora de preto


########################################################################
# Apresentação dos Resultados
########################################################################

# As imagens são em tons de cinza (1 canal), então não é preciso converter
# BGR -> RGB com o OpenCV: basta usar cmap="gray" no imshow.
# vmin=0 e vmax=255 fixam a escala. Sem eles, o Matplotlib ajusta o
# contraste de cada imagem sozinho (na imgMascara o menor valor é 87,
# que seria desenhado como preto).
Grafico = plt.figure(figsize=(11,10))

Grafico.add_subplot(2,2,1)
plt.imshow(imgOriginal, cmap="gray", vmin=0, vmax=255)
plt.title("Imagem Original", fontweight="bold", fontsize=10)

Grafico.add_subplot(2,2,2)
plt.imshow(imgMascara, cmap="gray", vmin=0, vmax=255)
plt.title(f"Pixels Menores que {Limiar} Viram Brancos", fontweight="bold", fontsize=10)

Grafico.add_subplot(2,2,3)
plt.imshow(imgLinhas, cmap="gray", vmin=0, vmax=255)
plt.title("Imagem com Linhas", fontweight="bold", fontsize=10)

Grafico.add_subplot(2,2,4)
plt.imshow(imgCamera, cmap="gray", vmin=0, vmax=255)
plt.title("Imagem Resultado", fontweight="bold", fontsize=10)

plt.tight_layout()
plt.savefig(dirCaminhoOutput)   # salvar ANTES do show (depois dele a figura fica vazia)
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################

##Como rodar o arquivo - instalações necessárias
#Requirements
#numpy
#matplotlib
#scikit-image
#opencv-pytohn

##Comandos para dowload
""" >> LINUX (Ubuntu)
 
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
 
  Se o primeiro comando der erro de "ensurepip" ou "venv", instale o
  pacote que falta e repita os comandos:
 
    sudo apt install python3-venv
 
>> WINDOWS (PowerShell)
 
    py -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt
 
  Se aparecer erro dizendo que a execução de scripts está desabilitada,
  rode o comando abaixo uma vez e tente ativar de novo:
 
    Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
 
Quando o ambiente está ativo, aparece (.venv) no começo da linha do
terminal. """

##Selecionar como usar
##Ctrl+Shift+P > "Python: Select Interpreter" > escolha o que tem
## .venv no caminho.