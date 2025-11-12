# # 2. Cálculo de bônus com uma nova regra
# # - Agora, crie um novo código que calcule e dê um print no bônus dos funcionários novamente. Porém há uma nova regra nesse 2º caso:
# # A meta é 1000 vendas
# # Agora, os funcionários que venderem muito acima da meta ganham mais bônus do que os outros. Então o bônus é definido da seguinte forma:
# # - Se vendas funcionário for maior ou igual a 2000, então o bônus é de 15% sobre o valor de vendas
# # - Se vendas funcionário for menor do que 2000 e maior ou igual a 1000, então o bônus é de 10% sobre o valor de vendas
# # - Se vendas funcionário for menos do que 1000 então o bônus do funcionário é de 0.
# # Use as mesmas variáveis de vendas_funcionários

meta1 = 2000
meta2 = 1000

Venfuncionario1 = 1500
Venfuncionario2 = 1800
Venfuncionario3 = 950


if Venfuncionario1 >= meta1:
    bonus = Venfuncionario1 * 0.15
    print("O bonus do 1º funcionario foi", bonus)
elif Venfuncionario1 < meta1 and Venfuncionario1 >= meta2:
    bonus = Venfuncionario1 * 0.10
    print("o bonus do 1º funcionario foi", bonus)
else:
     Venfuncionario1 < meta2
     print("o 1º funcionario não obteve bonus")

if Venfuncionario2 >= meta1:
    bonus = Venfuncionario2 * 0.15
    print("O bonus do 2º funcionario foi", bonus)
elif Venfuncionario2 < meta1 and Venfuncionario2 >= meta2:
    bonus = Venfuncionario2 * 0.10
    print("o bonus do 2º funcionario foi", bonus)
else:
     Venfuncionario2 < meta2
     print("o 2º funcionario não obteve bonus")

if Venfuncionario3 >= meta1:
    bonus = Venfuncionario3 * 0.15
    print("O bonus do 3º funcionario foi", bonus)
elif Venfuncionario3 < meta1 and Venfuncionario3 >= meta2:
    bonus = Venfuncionario3 * 0.10
    print("o bonus do 3º funcionario foi", bonus)
else:
     Venfuncionario3 < meta2
     print("o 3º funcionario não obteve bonus")
