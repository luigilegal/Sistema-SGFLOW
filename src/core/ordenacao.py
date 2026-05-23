def bubble_sort_rotas_crescente(rotas):
    """Ordena por menor KM usando Bubble Sort manual."""
    ordenadas = rotas.copy()

    for i in range(len(ordenadas)):
        houve_troca = False

        for j in range(0, len(ordenadas) - i - 1):
            if float(ordenadas[j]["distancia"]) > float(ordenadas[j + 1]["distancia"]):
                ordenadas[j], ordenadas[j + 1] = ordenadas[j + 1], ordenadas[j]
                houve_troca = True

        if not houve_troca:
            break

    return ordenadas


def insertion_sort_rotas_decrescente(rotas):
    """Ordena por maior KM usando Insertion Sort manual."""
    ordenadas = rotas.copy()

    for i in range(1, len(ordenadas)):
        chave = ordenadas[i]
        j = i - 1

        while j >= 0 and float(ordenadas[j]["distancia"]) < float(chave["distancia"]):
            ordenadas[j + 1] = ordenadas[j]
            j -= 1

        ordenadas[j + 1] = chave

    return ordenadas


def ordenar_rotas_por_distancia(rotas, ordem="crescente"):
    if ordem == "decrescente":
        return insertion_sort_rotas_decrescente(rotas)

    return bubble_sort_rotas_crescente(rotas)
