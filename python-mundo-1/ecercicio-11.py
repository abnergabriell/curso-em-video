# Exercício Python 011 -Faça um programa que leia largura e a altura de uma paraede em metros,calcule a sua área e a quantidade de tinta  necessária para pintá-la,sabendo que cada litro de tinta,pinta uma área de 2m².
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2
print(f'Sua parede tem dimensão de {largura}x{altura} e sua área é de {area}m².\n Para pintar esta parede, você precisará de {tinta} de tinta')