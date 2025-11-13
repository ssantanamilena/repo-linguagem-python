#add novos produtos a uma lista
produtos = ['apple tv', 'mac', 'iphone x', 'ipad', 'apple watch', 'mac book', 'airpods']
novos_produtos = ['iphone12', 'oculos']

#maneira 1º de add novos produtos
produtos.extend(novos_produtos)
print (produtos)

#segunda maneira de add novos produtos
todos_produtos = produtos + novos_produtos
print(todos_produtos)

# ordenar lista, # true ordenada no maior pro menos e #false menor para maior
produtos.sort(reverse=True)
print(produtos)
#segundo exemplo true - maior para menor
salario = [2000,300,9000,1500,2800,700,1200]
salario.sort(reverse=True)
print(salario)







