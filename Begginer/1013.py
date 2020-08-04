#Definição e atribuição de váriaveis
valores = input().split(" ")
a, b, c = valores

#Cálculos
maiorAB = (int(a) + int(b)+ abs(int(a)-int(b)))/2
maiorAB = (maiorAB + int(c)+ abs(maiorAB-int(c)))/2

#prints
print("%d eh o maior" %maiorAB)
