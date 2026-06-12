'''Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.'''
n = int(input('Digite o número no qual você queira saber a tabuada: '))

for c in range(1,11):
    print('{} x {} = {}'.format(n, c, n * c))
print('Acabou!')
