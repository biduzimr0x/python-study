'''Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'''
n = int(input('Digite quantos metrôs você quer converter: '))
cm = n * 100
mm = n * 1000
print('Você escolheu o número {} em centímetro é {} e em milímetro é {}'.format(n, cm, mm))
