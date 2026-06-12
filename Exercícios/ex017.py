'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa'''
co = int(input('Digite o comprimento do cateto oposto: '))
ca = int(input('Digite o comprimento do cateto adjacente: '))
h = co**2 + ca**2
ch = h ** (1/2)
print('O comprimento da hipotenusa é {}'.format(ch))
