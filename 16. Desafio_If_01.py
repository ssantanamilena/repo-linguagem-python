# 1. Cálculo de Bônus
# - Crie um programa que calcule e dê um print no bônus que os funcionários devem receber segundo a regra:
# A meta é 1000 vendas.
# Se o valor de vendas for maior ou igual a meta, o valor do bônus do funcionário é 10% do valor de vendas.
# Caso contrário o valor de bônus do funcionário é 0.
# Print o bônus dos 3 funcionários

meta = 1000

Venfuncionario1 = 1500
Venfuncionario2 = 1800
Venfuncionario3 = 950


if Venfuncionario1 >= meta:
    bonus = Venfuncionario1 * 0.10
    print("O bonus do 1º funcionario foi", bonus)
else:
     Venfuncionario1 * 0
     print("o 1º funcionario não obteve bonus")
if Venfuncionario2 >= meta:
    bonus = Venfuncionario1 * 0.10
    print("O bonus do 2º funcionario foi", bonus)
else:
     Venfuncionario2 * 0
     print(" O 2º funcionario não obteve bonus")

if Venfuncionario3 >= meta:
    bonus = Venfuncionario1 * 0.10
    print("O bonus do 3º funcionario foi", bonus)
else:
     Venfuncionario1 * 0
     print("O 3º funcionario não obteve bonus")