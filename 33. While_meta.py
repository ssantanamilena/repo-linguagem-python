vendas = [1200,250,450,800,530,900]
vendedores = ['Luiza', 'João', 'Carlos', 'José', 'Renan', 'Amanda']
meta = 500

i = 0
while i < len(vendas):
    if vendas[i] > meta:
        print(f'{vendedores[i]}, bateu a meta. A venda foi igual a {vendas[i]}.')
    i = i + 1
