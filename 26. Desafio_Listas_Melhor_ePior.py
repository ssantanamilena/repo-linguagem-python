#1. Faturamento do Melhor e do Pior Mês do Ano
# Qual foi o valor de vendas do melhor mês do Ano?
# E valor do pior mês do ano?
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]
vendas_1sem.extend(vendas_2sem)
print (vendas_1sem)

#a. Melhor faturamento
melhor_faturamento = max(vendas_1sem)
print(melhor_faturamento)

#b.saber posição do melhor faturamento do melhor mês
melhor_faturamento_produto = vendas_1sem.index (melhor_faturamento)
print(melhor_faturamento_produto)

#c.saber qual foi o mais vendido e em qual mês apartir do index do codigo acima
i = vendas_1sem.index (melhor_faturamento)
melhor_faturamento_produto = meses[10]
print(melhor_faturamento_produto)
print(f'O valor de venda do melhor mês foi de {melhor_faturamento} no mês de {melhor_faturamento_produto}')

#d.E valor do pior mês do ano?
pior_faturamento = min(vendas_1sem)
print(pior_faturamento)

pior_faturamento_produto = vendas_1sem.index (pior_faturamento)
print(pior_faturamento_produto)

i = vendas_1sem.index (pior_faturamento)
pior_faturamento_produto = meses[11]
print(pior_faturamento_produto)
print(f'O valor de venda do pior mês foi de {pior_faturamento} no mês de {pior_faturamento_produto}')

# Calcule também o faturamento total do Ano e quanto que o melhor mês representou do faturamento total.
Faturamento_total =sum(vendas_1sem)
print(f'O faturamneto total do ano foi {Faturamento_total:.2f}')
valor_formatado = f"{Faturamento_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
print(f'O valor formatado: {valor_formatado}')
percentual = melhor_faturamento / Faturamento_total
print(f'O melhor mês representou {percentual:.1%} das vendas do ano todo')
