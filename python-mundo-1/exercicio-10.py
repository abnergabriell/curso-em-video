# Exercício Python 010- Crie um programa que leia  quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
real =  float(input('Quanto de dinheiro você tem na carteira? '))
dolar = real / 5.22
print ('Com r${} você  pode comprar  US${}' .format(real,dolar))0