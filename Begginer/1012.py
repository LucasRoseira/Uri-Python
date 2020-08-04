#Definição e atribuição de váriaveis
areas = input().split(" ")
a, b, c = areas

#Cálculos
trianguloRetangulo = ((float(a) * float(c))/2)
circulo = 3.14159 * (float(c) ** 2)
trapezio = (((float(a) + float(b)) / 2) * float(c))
quadrado = float(b) ** 2
retangulo = float(a) * float(b)
#prints
print("TRIANGULO: {0:.3f}".format(trianguloRetangulo))
print("CIRCULO: {0:.3f}".format(circulo))
print("TRAPEZIO: {0:.3f}".format(trapezio))
print("QUADRADO: {0:.3f}".format(quadrado))
print("RETANGULO: {0:.3f}".format(retangulo))
