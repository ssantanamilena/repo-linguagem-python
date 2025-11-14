#for é uma estrutura de repetição
for i in range(5): #i = variavel, (5) vai executar o codigo 5 vezes
    print(i)

for i in range(5): 
    print('Milena')

#1º maneira de percorrer item
produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
for i in range(5):
    print(produtos[i])

#2º maneira de percorrer item
produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
for item in produtos:
    print(item)

produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
for produto in produtos: #troquei o nome da variável para produtos
    print(produto)

texto = 'Milena' 
for ch in texto: #ch nome da variável criada, espaço tbém conta como caracter
    print(ch)    

produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
producao = [15000, 12000, 13000, 5000,250]
tamanho = len(produtos) #calculando/automatizando tamanho da lista
for i in range(tamanho):
    print(f'{produtos[i]} unidades produtizadas de {producao[i]}')