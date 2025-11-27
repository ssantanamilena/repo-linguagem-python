# Quando você quer permitir uma quantidade indefinida de argumentos, usa o * para isso.
def minha_soma(*numeros):  # antes do nome do argumento
    soma = 0
    for numero in numeros:
        soma += numero  # soma recebe o valor do número
    return soma


print(minha_soma(10, 13, 1, 10, 0, 9, 2))
