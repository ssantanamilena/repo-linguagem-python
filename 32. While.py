venda = input('registre um produto')
vendas  = []
while venda != '':
    vendas.append(venda)
    venda = input('registre um produto')
print(f'as vendas cadastradas fora {vendas}')