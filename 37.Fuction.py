# Crie uma função que calcule qual o % da carga tributária que está sendo aplicado sobre um determinado produto, dado o preço de venda, o "lucro" e os custos (com exceção do imposto) dele. 
preco = 1500
custo = 400
lucro = 800
def carga_tributario(preco, custo ,lucro):
    imposto = preco - custo - lucro
    carga = imposto / preco
    return imposto / preco
print(carga_tributario(preco, lucro, custo))
