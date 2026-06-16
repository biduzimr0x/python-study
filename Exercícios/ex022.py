""" Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúculas
O nome com todas minúsculas
Quantas letras ao todo (sem considerar espaços)
Quantas letras tem o promeiro nome. """
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letas.'.format(separa[0], len(separa[0])))
