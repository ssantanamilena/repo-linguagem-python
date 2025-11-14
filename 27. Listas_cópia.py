#1º maneira de modificar lista
lista = ['ipad', 'iphone x', 'apple tv']
lista[2] = 'iphone11'
print(lista)
#2º maneira de modificar lista
lista = ['ipad', 'iphone x', 'apple tv']
lista2 = lista[:]
lista[2] = 'iphone11'
print(lista)
print(lista2)