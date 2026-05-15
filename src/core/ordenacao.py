def bubble_sort_rotas(rotas):
    
    ordenadas = rotas.copy()
    n = len(ordenadas)

    for i in range(n):
        houve_troca = False
        for j in range(0, n - i - 1):
            if ordenadas[j]["distancia"] > ordenadas[j + 1]["distancia"]:
                ordenadas[j], ordenadas[j + 1] = ordenadas[j + 1], ordenadas[j]
                houve_troca = True
        if not houve_troca:
            break

    return ordenadas


def insertion_sort_rotas(rotas):
   
    ordenadas = rotas.copy()

    for i in range(1, len(ordenadas)):
        chave = ordenadas[i]
        j = i - 1

        while j >= 0 and ordenadas[j]["distancia"] > chave["distancia"]:
            ordenadas[j + 1] = ordenadas[j]
            j -= 1

        ordenadas[j + 1] = chave

    return ordenadas
