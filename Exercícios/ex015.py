'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$0,15 por Km rodado.'''
dias = int(input('Quantos dias você ficou com o carro? '))
km_percorridos = float(input('Quantos Kms você percorreu? '))
total_dia = 60 * dias
total_km =  km_percorridos * 0.15
print('O total a pagar é de R${:.2f}'.format(total_km + total_dia))
