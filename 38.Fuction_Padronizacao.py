def pradronizar_codigos(lista_codigos, padrao = 'm'):
    for i, item in enumerate(lista_codigos):
        item = item.replace('  ',' ') # transformar 2 espaços por 1 espaço
        item = item.strip()
        if padrao == 'm':
            item = item.casefold()
        elif padrao == 'M':
            item = item.upper()
        lista_codigos[i] = item
    return lista_codigos

cod_produtos = ['ABC12', 'abc123', 'Ab37']
print(pradronizar_codigos(cod_produtos, 'm'))