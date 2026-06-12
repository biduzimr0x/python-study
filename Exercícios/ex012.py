'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''
preço = float(input('Digite o preço do produto: '))
#Outro forma de fazer
'''desconto = preço * 5 / 100 
novo_preço = preço - desconto'''
novo_preço = preço * 0.95
print('O preço do produto é R${:.2f} e com o desconto de 5% fica R${:.2f}'.format(preço, novo_preço))
