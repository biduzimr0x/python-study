'''Escreva um programa que converta uma temperatura digita em °C e converta para °F'''
graus = float(input('Quantos graus °C está em sua cidade? '))
converter = (graus * 1.8) + 32
print('Em sua cidade está {}°C e convertido fica {}°F.'.format(graus, converter))
