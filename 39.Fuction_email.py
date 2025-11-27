def filtrar_lista_texto(lista, pedaco_texto):
    lista_filtrada = []
    for item in lista:
        if pedaco_texto in item:
            lista_filtrada.append(item)
    return lista_filtrada

lista_textos = ['milena@gmail.com', 'francisca@hotmail.com', 'joão@gmail.com']
lista = filtrar_lista_texto(lista_textos, 'hotmail')
print(lista)