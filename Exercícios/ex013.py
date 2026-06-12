'''Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'''
salário = float(input('Quanto você recebe por mês? '))
novo_salário = salário * 0.15
print('Seu salário era R${:.2f} e com o aumento de 15% ficou {:.2f}'.format(salário, novo_salário))
