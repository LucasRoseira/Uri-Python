#import de bibliotecas
import math
#Definição e atribuição de váriaveis
linha = input().split(" ")
linha1 = input().split(" ")
x1, y1 = linha
x2, y2 = linha1

#Cálculos
distancia = ((float(x2) - float(x1)) ** 2) + ((float(y2) - float(y1)) ** 2)
distancia = math.sqrt(distancia)
#prints
print("{0:.4f}".format(distancia))
