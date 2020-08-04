nomeFuncionario = input()
salarioFixo = float(input())
totalVendas = float(input())
salarioTotal =  (totalVendas * 0.15) + salarioFixo
print("TOTAL = R$ {0:.2f}".format(salarioTotal))
