# faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

n1 = float(input('digite o preço'))
desconto = n1 - (n1*5/100)
#preco = n1-desconto
#print('O preço de R$ {} com desconto de 5% resulta em R$ {:.2f}'.format(n1,preco))
print ('O produto que custava R${} com 5% de desconto custará R${:.2f}'.format(n1, desconto))
