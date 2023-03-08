# Exercício Python 012 - Faça um algoritimo que leia o preço  de um produto e mostre seu novo preço, com 5% de desconto.
v = float(input('Qual o preço do produto? R$ '))
p = v * 0.05
np = v - p
print(f' O produto que custava R$ {v:.2f}, e com o desconto de 5% ele passa a custar R$ {np:.2f}.')

                  