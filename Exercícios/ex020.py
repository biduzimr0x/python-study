'''O mesmo professor do desafio anterior que sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada'''
import random
n1 = str(input('Digite o nome do primeiro estudante: '))
n2 = str(input('Digite o nome do segundo estudante: '))
n3 = str(input('Digite o nome do terceiro estudante: '))
n4 = str(input('Digite o nome do quarto estudante: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem da apresentação será: {}'.format(lista))
