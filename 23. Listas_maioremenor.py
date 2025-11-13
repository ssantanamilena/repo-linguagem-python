# Saber quantos produtos tem em um lista
produtos = ['apple tv', 'mac', 'iphone x', 'ipad', 'apple watch', 'mac book', 'airpods']
tamanho= len(produtos)
print(f'temos {tamanho} produtos')

#Saber qual produto foi o mais vendido
vendas = [4000,5000,2000,4000,1000,9000,200]
mais_vendido = max(vendas)
menos_vendido = min(vendas)
print(f'O produto mais vendido teve {mais_vendido} unidas vendidas e o menos vendido teve {menos_vendido}')

#saber a posição do mais vendido
produto_mais_vendido = vendas.index(mais_vendido)
print(produto_mais_vendido)
# saber qual foi o mais vendido apartir do index do codigo acima
i = vendas.index(mais_vendido)
produto_mais_vendido  = produtos [5]
print(produto_mais_vendido)
#saber a posição do menos vendido
produto_menos_vendido = vendas.index(menos_vendido)
print(produto_menos_vendido)
#saber qual foi o menos vendido apartir do index do codigo acima
i = vendas.index(mais_vendido)
produto_mais_vendido  = produtos [6]
print(produto_mais_vendido)

