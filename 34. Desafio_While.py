# While - continua rodando até produto ser fazio.
vendas = []
while True:
    produto = input('Qual seu produto?')
    if not produto:
        break
    qtd = int(input('Qual a quantidade?'))
    vendas.append([produto,qtd])
print(vendas)