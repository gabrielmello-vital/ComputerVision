########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
import cv2 as cv #opencv
import os
########################################################################
# Definições Gerais
########################################################################


def listar_imagens(pasta_relativa ="../../Imagens"):
      pasta_atual = os.path.dirname(os.path.abspath(__file__))
      pasta_alvo = os.path.abspath(os.path.join(pasta_atual, pasta_relativa))
      with os.scandir(pasta_alvo) as entradas:
        for entrada in entradas:
            if entrada.is_file() and entrada.name.lower().endswith((".jpg", ".png")):
                print(entrada.name)

def main():
   
   print("########################### Lista de Imagens Disponíveis #############################")
   listar_imagens()

   variavelImagem = input("Digite o Nome da Imagem desejada com extensão: ").strip()
   print ("")
   NomeImagem = "../../Imagens/" + variavelImagem
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

if __name__ == "__main__":
   main()

