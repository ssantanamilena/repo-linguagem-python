#o enumerate permite que vc percorra uma lista e ao mesmo tempo tenha uma variavel o indice daquele item.
funcionarios = ['maria','jose','heitor']
for funcionario in range(3):
    print(funcionarios)  
for i, funcionario in enumerate(funcionarios):
    print(f'{i} é o funcionario {funcionario}')

  

