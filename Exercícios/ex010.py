'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considere
$1,00 = 3,27'''
valor = float(input('Quanto você quer converter para dólar? '))
dólar = 3.27
valor_corridigo = valor / dólar
print('{} convertido para dolar é {:.2f}'.format(valor, valor_corridigo))
