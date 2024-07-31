"""
    # Funzione per controllare se due sottoalberi sono speculari
def is_mirror(left_index, right_index):
        # Se entrambi gli indici sono fuori bounds, è simmetrico
    if left_index >= len(tree) and right_index >= len(tree):
        return True
        # Se solo uno dei due è fuori bounds, non è simmetrico
    if left_index >= len(tree) or right_index >= len(tree):
        return False
        # Se i valori dei nodi sono diversi, non è simmetrico
    if tree[left_index] != tree[right_index]:
        return False
        # Confronta i sottoalberi in modo speculare
    return (is_mirror(2 * left_index + 1, 2 * right_index + 2) and
            is_mirror(2 * left_index + 2, 2 * right_index + 1))
    
    # Un albero vuoto è considerato simmetrico

"""
def symmetric(tree: list[int]) -> bool:
    # scrivere qui la vostra funzione
    lista_specchio:list=[]
    lista2:list=[]
    v:int=0
    for i in tree[1:]:
        if v % 2 ==0:
            lista_specchio.append(i)
        else:
            lista2.append(i)
        v+=1
    for v in lista_specchio[:]:
        if v in lista2[:]:
            lista2.remove(v)
            lista_specchio.remove(v)
    if len(lista_specchio)==0 and len(lista2)==0:
        return True
    else:
        return False

        





print(symmetric([1,2,2,3,4,4,3]))

""""
Data una lista di interi, chiamata tree, che rappresenta un albero binario, restituire True se l'albero è simmetrico; False altrimenti.

La lista di interi è formata così:

    L'elemento in posizione 0 corrisponde alla radice
    Dato un nodo in posizione i, il suo figlio sinistro si trova in posizione 2*i + 1
    Dato un nodo in posizione i, il suo figlio destro si trova in posizione 2*(i+1)
    Se, dato un indice i si va fuori bound facendo almeno uno dei calcoli dei punti precedenti, significa che il nodo che corrisponde a quell'indice è una foglia.

"""
def symmetric(tree: list[int]) -> bool:
    # scrivere qui la vostra funzione
    pass