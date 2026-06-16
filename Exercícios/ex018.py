'''Faça um programa que leia um ângulo e mostre na tela o valor do seno, cosseno e tangete desse ângulo'''
import math
ângulo = int(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
cosseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno ))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente ))
