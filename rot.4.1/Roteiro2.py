# -*- coding: utf-8 -*-


# FUNCOES IMPLEMANTADAS
def ha_laco(C):
    # percorre a diagonal principal
    # contador para pegar apenas os elementos da diagonal principal
    el = -1
    # cada linha
    for l in range(len(C.N)):
        el += 1
        # quadrado da diagonal principal
        elm = C.M[l][el]
        # lasso
        if elm >= 1:
            return True
# nao encontrou laco na diagonal principal
    return False

def vertices_nao_adjacentes(C):
    # varavel de retorno
    lis_vertices_nao_adjacentes = []
    # percorre a matirz
    c_el = -1
    adj = ""
    for l in range(len(C.N)):
        c_el += 1
        for e in range(c_el, len(C.M[l])):
            elm = C.M[l][e]
            if elm == 0:
                adj = "{}-{}".format(C.N[l], C.N[e])
                lis_vertices_nao_adjacentes.append(adj)
    return lis_vertices_nao_adjacentes

def ha_paralelas(C):
    # percorre a matirz
    c_el = -1
    for l in range(len(C.N)):
        c_el += 1
        for e in range(c_el, len(C.M[l])):
            elm = C.M[l][e]
            if elm > 1:
                return True
    return False

# def grau(C, vertice):
#     # percorre a matirz
#     c_el = -1
#     counter = 0
#     adj = ""
#     for l in range(len(C.N)):
#         c_el += 1
#         for e in range(c_el, len(C.M[l])):
#             adj = "{}{}".format(C.N[l], C.N[e])
#             if vertice in adj:
#                 elm = C.M[l][e]
#                 if elm > 0:
#                     counter += elm
#     return counter

def grau(C, vertice):
    # percorre a matirz
    counter = 0
    for l in range(len(C.N)):
        for e in range(len(C.M[l])):
            adj = "{}{}".format(C.N[l], C.N[e])
            if vertice in adj:
                elm = C.M[l][e]
                if elm > 0:
                    counter += elm
    return counter

def arestas_sobre_vertice(C, vertice):
    # percorre a matirz
    ver = vertice
    lis = []
    c_el = -1
    adj = ""
    elm = 0
    for l in range(len(C.N)):
        c_el += 1
        for e in range(c_el, len(C.M[l])):
            if C.N[l] != C.N[e]:
                adj = "{}-{}".format(C.N[l], C.N[e])
                elm = C.M[l][e]
                if vertice in adj and elm >= 1:
                    for ap in range(elm):
                        lis.append(adj)
    return lis

def eh_completo(C):
    # percorre a matirz
    c_el = -1
    for l in range(len(C.N)):
        c_el += 1
        for e in range(c_el, len(C.M[l])):
            if C.N[l] != C.N[e]:
                elm = C.M[l][e]
                if elm == 0:
                    return False
    return True
# FUNCOES IMPLEMENTADAS

# DESAFIOS
def comprimento_de_tamanho_n(C, lenght_arg, l_arg=None, trld_edgs_quant_arg=0):
    if trld_edgs_quant_arg == lenght_arg:  # gets the objective
        C.return_var = True
    if l_arg is None:
        C.return_var = False  # declarating local static variable
        c_el = 0  # excludes main diagonal
        for l in range(len(C.N)):
            c_el += 1
            for c in range(c_el, len(C.M[l])):
                elm = C.M[l][c]  # element of the position of the matrix
                if elm >= 1:
                    # calls the recursion whereas each vertex as the beginnig of a path
                    trld_edgs_quant_arg += 1
                    C.comprimento_de_tamanho_n(lenght_arg=lenght_arg, l_arg=c, trld_edgs_quant_arg=trld_edgs_quant_arg)
                    trld_edgs_quant_arg -= 1
    else:
        for c in range(l_arg + 1, len(C.M[l_arg])):
            elm = C.M[l_arg][c]  # element of the position of the matrix
            if elm >= 1:
                # calls the recursion to jump to another line of the matrix
                trld_edgs_quant_arg += 1
                C.comprimento_de_tamanho_n(lenght_arg=lenght_arg, l_arg=c, trld_edgs_quant_arg=trld_edgs_quant_arg)
                trld_edgs_quant_arg -= 1
    return C.return_var

# deu certo
def ha_ciclo(C, has_dit=False, v_partida=None, line_index=None):
    if has_dit is False and v_partida is None and line_index is None:
        C.path_ret = []
        C.path = []
        # 1__ edges translator
        C.dit_a = {}  # declarating local static variable
        a = None
        c_el = -1
        elm = None
        counter = 1
        for l in range(len(C.N)):
            c_el += 1
            for e in range(c_el, len(C.M[l])):
                elm = C.M[l][e]
                if elm == 1:
                    if l not in C.dit_a.keys():
                        C.dit_a[l] = {}
                    if e not in C.dit_a[l].keys():
                        C.dit_a[l][e] = []
                    a = "a{}".format(counter)
                    counter += 1
                    C.dit_a[l][e].append(a)
                elif elm > 1:
                    if l not in C.dit_a.keys():
                        C.dit_a[l] = {}
                    if e not in C.dit_a[l].keys():
                        C.dit_a[l][e] = []
                    for i in range(elm):
                        a = "a{}".format(counter)
                        counter += 1
                        C.dit_a[l][e].append(a)
        # 1__ edges translator

        ev = -1
        for l in range(len(C.N)):
            ev += 1
            for e in range(ev, len(C.N)):
                elm = C.M[l][e]
                if e == l and elm >=1:
                    return [C.N[l], C.dit_a[l][e][0], C.N[l]]
                elif e != l and elm >= 2:
                    return [C.N[l], C.dit_a[l][e][0], C.N[e], C.dit_a[l][e][1], C.N[l]]
        C.ha_ciclo(has_dit=True)


    elif has_dit is True and v_partida is None and line_index is None:
        ev = 0
        for l in range(len(C.N)):
            ev += 1
            for e in range(ev, len(C.N)):
                elm = C.M[l][e]
                if elm > 0:
                    vertice = C.N[l]
                    aresta = C.dit_a[l][e][0]
                    C.path.clear()
                    C.path.append(vertice)
                    C.path.append(aresta)
                    C.ha_ciclo(has_dit=True, v_partida=vertice, line_index=e)

    elif has_dit is True and v_partida is not None and line_index is not None:
        vertice_recebido = C.N[line_index]
        C.path.append(vertice_recebido)

        if C.path[0] == C.path[-1]:
            C.path_ret = C.path.copy()
            return C.path_ret

        coluna_de_retorno = line_index
        linha_de_retorno = C.N.index(C.path[0])
        elm_de_retorno = C.M[linha_de_retorno][coluna_de_retorno]
        if elm_de_retorno > 0:
            aresta_de_retorno = C.dit_a[linha_de_retorno][coluna_de_retorno][0]
            if aresta_de_retorno not in C.path: # pode retornar e feichar o ciclo
                #self.path.append(self.N[coluna_de_retorno])
                C.path.append(C.dit_a[linha_de_retorno][coluna_de_retorno][0])
                C.ha_ciclo(has_dit=True, v_partida=C.path[0], line_index=linha_de_retorno)

        for e in range(line_index + 1, len(C.N)):
            elm = C.M[line_index][e]
            if elm > 0:
                aresta = C.dit_a[line_index][e][0]
                C.path.append(aresta)
                C.ha_ciclo(has_dit=True, v_partida=C.path[0], line_index=e)

    return C.path_ret


def eh_conexo(C):
    vert = []
    ev = 0
    for l in range(len(C.N)):
        ev += 1
        count = 0
        if len(C.N) > 1:
            for e in range(ev, len(C.N)):
                elm = C.M[l][e]
                if elm >= 1:
                    if len(vert) == 0:
                        vert.append(C.N[l])
                    count += 1
                    if C.N[e] not in vert:
                        vert.append(C.N[e])
            if count == 0:
                if C.N[l] in vert:
                    pass
                else:
                    return False
        else:
            return True

    if len(vert) == len(C.N):
        return True
    return False
# DESAFIOS