# Busqueda en Amplitud 
from Nodos import Nodo

def busqueda_BPA_solucion(estado_inicial, solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []

    nodo_raiz = Nodo(estado_inicial)
    nodos_frontera.append(nodo_raiz)
    while (not resuelto) and len(nodos_frontera) != 0:
        nodo_actual = nodos_frontera.pop(0)
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_estado() == solucion:
            # solucion encontrada
            resuelto = True
            return nodo_actual
        else:
            # expandir nodos hijo
            estado_nodo = nodo_actual.get_estado()

            # operador izquierdo
            hijo = [estado_nodo[0], estado_nodo[2], estado_nodo[1], estado_nodo[3], estado_nodo[4]]
            hijo_izquierda = Nodo(hijo)
            if not hijo_izquierda.en_lista(nodos_visitados) and not hijo_izquierda.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izquierda)

            # operador central
            hijo = [estado_nodo[1], estado_nodo[0], estado_nodo[2], estado_nodo[3], estado_nodo[4]]
            hijo_centro = Nodo(hijo)
            if not hijo_centro.en_lista(nodos_visitados) and not hijo_centro.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_centro)

            # operador derecho
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[2], estado_nodo[4], estado_nodo[3]]
            hijo_derecha = Nodo(hijo)
            if not hijo_derecha.en_lista(nodos_visitados) and not hijo_derecha.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_derecha)

            #operador auxiliar
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[3], estado_nodo[2], estado_nodo[4]]
            hijo_aux = Nodo(hijo)
            if not hijo_aux.en_lista(nodos_visitados) and not hijo_aux.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_aux)

            nodo_actual.set_hijo([hijo_izquierda, hijo_centro, hijo_derecha, hijo_aux ])


if __name__ == "__main__":
    estado_inicial = ['C', 'A', 'E', 'D', 'B']
    solucion = ['A', 'B', 'C', 'D', 'E']
    nodo_solucion = busqueda_BPA_solucion(estado_inicial, solucion)
    # mostrar resultado
    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_estado())
        nodo_actual = nodo_actual.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
