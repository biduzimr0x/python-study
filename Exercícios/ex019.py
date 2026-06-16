'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido'''
import random
primeiro = (input('Primeiro estudante: '))
segundo = (input('Segundo estudante: '))
terceiro = (input('Terceiro estudante: '))
quarto = (input('Quarto estudante: '))
estudantes = [primeiro, segundo, terceiro, quarto]
sorteio = random.choice(estudantes)
print(sorteio)
