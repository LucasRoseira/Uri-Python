##O split()método divide uma string em uma lista.
# Você pode especificar o separador, o separador padrão é qualquer espaço em branco.
linha = input().split(" ")
linha1 = input().split(" ")
cod, qtd, valor = linha
cod1, qtd1, valor1 = linha1
valorPagar = (int(qtd) * float(valor)) + (int(qtd1) * float(valor1))
print("VALOR A PAGAR: R$ {0:.2f}".format(valorPagar))
