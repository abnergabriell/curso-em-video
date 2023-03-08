# Exercício Python 013 - Faça um algoritimo que leia sálario de um funcionário e mostre seu novo sálario,com 15% de aumento.
salário = float(input('Qual o seu salário? R$'))
novosalário = salário + (salário * 0.15)
print(f' Seu salário é R${salário:.2f}, com o aumento de 15%, seu salário passará a ser R${novosalário:.2f}')