# -*- coding: utf-8 -*-

class VerticeInvalidoException(Exception):
    pass

class ArestaInvalidaException(Exception):
    pass

class MatrizInvalidaException(Exception):
    pass

class Grafo:

    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'
    __maior_vertice = 0

    def __init__(self, V=None, M=None):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param V: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma matriz de adjacência que guarda as arestas do grafo. Cada entrada da matriz tem um inteiro que indica a quantidade de arestas que ligam aqueles vértices
        '''

        if V == None:
            V = list()
        if M == None:
            M = list()

        for v in V:
            if not(Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

        self.N = list(V)

        if M == []:
            for k in range(len(V)):
                M.append(list())
                for l in range(len(V)):
                    if k>l:
                        M[k].append('-')
                    else:
                        M[k].append(0)


        if len(M) != len(V):
            raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for c in M:
            if len(c) != len(V):
                raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for i in range(len(V)):
            for j in range(len(V)):
                '''
                Verifica se os índices passados como parâmetro representam um elemento da matriz abaixo da diagonal principal.
                Além disso, verifica se o referido elemento é um traço "-". Isso indica que a matriz é não direcionada e foi construída corretamente.
                '''
                if i>j and not(M[i][j] == '-'):
                    raise MatrizInvalidaException('A matriz não representa uma matriz não direcionada')


                aresta = V[i] + Grafo.SEPARADOR_ARESTA + V[j]
                if not(self.arestaValida(aresta)):
                    raise ArestaInvalidaException('A aresta ' + aresta + ' é inválida')

        self.M = list(M)

    def arestaValida(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta é representada por um string com o formato a-b, onde:
        a é um substring de aresta que é o nome de um vértice adjacente à aresta.
        - é um caractere separador. Uma aresta só pode ter um único caractere como esse.
        b é um substring de aresta que é o nome do outro vértice adjacente à aresta.
        Além disso, uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        '''

        # Não pode haver mais de um caractere separador
        if aresta.count(Grafo.SEPARADOR_ARESTA) != Grafo.QTDE_MAX_SEPARADOR:
            return False

        # Índice do elemento separador
        i_traco = aresta.index(Grafo.SEPARADOR_ARESTA)

        # O caractere separador não pode ser o primeiro ou o último caractere da aresta
        if i_traco == 0 or aresta[-1] == Grafo.SEPARADOR_ARESTA:
            return False

        if not(self.existeVertice(aresta[:i_traco])) or not(self.existeVertice(aresta[i_traco+1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def __primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice X
        :param a: a aresta a ser analisada
        :return: O primeiro vértice da aresta
        '''
        return a[0:a.index(Grafo.SEPARADOR_ARESTA)]

    def __segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice Y
        :param a: A aresta a ser analisada
        :return: O segundo vértice da aresta
        '''
        return a[a.index(Grafo.SEPARADOR_ARESTA)+1:]

    def __indice_primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice X na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do primeiro vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__primeiro_vertice_aresta(a))

    def __indice_segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice Y na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do segundo vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__segundo_vertice_aresta(a))

    def existeAresta(self, a: str):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, a):
            for i in range(len(self.M)):
                for j in range(len(self.M)):
                    if self.M[self.__indice_primeiro_vertice_aresta(a)][self.__indice_segundo_vertice_aresta(a)]:
                        existe = True

        return existe

    def adicionaVertice(self, v):
        '''
        Inclui um vértice no grafo se ele estiver no formato correto.
        :param v: O vértice a ser incluído no grafo.
        :raises VerticeInvalidoException se o vértice já existe ou se ele não estiver no formato válido.
        '''
        if v in self.N:
            raise VerticeInvalidoException('O vértice {} já existe'.format(v))

        if self.verticeValido(v):
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

            self.N.append(v) # Adiciona vértice na lista de vértices
            self.M.append([]) # Adiciona a linha

            for k in range(len(self.N)):
                if k != len(self.N) -1:
                    self.M[k].append(0) # adiciona os elementos da coluna do vértice
                    self.M[self.N.index(v)].append('-') # adiciona os elementos da linha do vértice
                else:
                    self.M[self.N.index(v)].append(0)  # adiciona um zero no último elemento da linha
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, a):
        '''
        Adiciona uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
        if self.arestaValida(a):
            i_a1 = self.__indice_primeiro_vertice_aresta(a)
            i_a2 = self.__indice_segundo_vertice_aresta(a)
            if i_a1 < i_a2:
                self.M[i_a1][i_a2] += 1
            else:
                self.M[i_a2][i_a1] += 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def remove_aresta(self, a):
        '''
        Remove uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
        if self.arestaValida(a):
            if self.existeAresta(a):
                i_a1 = self.__indice_primeiro_vertice_aresta(a)
                i_a2 = self.__indice_segundo_vertice_aresta(a)
                if i_a1 < i_a2:
                    self.M[i_a1][i_a2] -= 1
                else:
                    self.M[i_a2][i_a1] -= 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    # FUNCOES IMPLEMANTADAS
    def ha_laco(self):
        # percorre a diagonal principal
        # contador para pegar apenas os elementos da diagonal principal
        el = -1
        # cada linha
        for l in range(len(self.N)):
            el += 1
            # quadrado da diagonal principal
            elm = self.M[l][el]
            # lasso
            if elm >= 1:
                return True
    # nao encontrou laco na diagonal principal
        return False

    def vertices_nao_adjacentes(self):
        # varavel de retorno
        lis_vertices_nao_adjacentes = []
        # percorre a matirz
        c_el = -1
        adj = ""
        for l in range(len(self.N)):
            c_el += 1
            for e in range(c_el, len(self.M[l])):
                elm = self.M[l][e]
                if elm == 0:
                    adj = "{}-{}".format(self.N[l], self.N[e])
                    lis_vertices_nao_adjacentes.append(adj)
        return lis_vertices_nao_adjacentes

    def ha_paralelas(self):
        # percorre a matirz
        c_el = -1
        for l in range(len(self.N)):
            c_el += 1
            for e in range(c_el, len(self.M[l])):
                elm = self.M[l][e]
                if elm > 1:
                    return True
        return False

    def grau(self, vertice):
        # percorre a matirz
        c_el = -1
        counter = 0
        adj = ""
        for l in range(len(self.N)):
            c_el += 1
            for e in range(c_el, len(self.M[l])):
                adj = "{}{}".format(self.N[l], self.N[e])
                if vertice in adj:
                    elm = self.M[l][e]
                    if elm > 0:
                        counter += elm
        return counter

    def arestas_sobre_vertice(self, vertice):
        # percorre a matirz
        ver = vertice
        lis = []
        c_el = -1
        adj = ""
        elm = 0
        for l in range(len(self.N)):
            c_el += 1
            for e in range(c_el, len(self.M[l])):
                if self.N[l] != self.N[e]:
                    adj = "{}-{}".format(self.N[l], self.N[e])
                    elm = self.M[l][e]
                    if vertice in adj and elm >= 1:
                        lis.append(adj)
        return lis

    def eh_completo(self):
        # percorre a matirz
        c_el = -1
        for l in range(len(self.N)):
            c_el += 1
            for e in range(c_el, len(self.M[l])):
                if self.N[l] != self.N[e]:
                    elm = self.M[l][e]
                    if elm == 0:
                        return False
        return True
    # FUNCOES IMPLEMENTADAS

    # DESAFIOS
    def comprimento_de_tamanho_n(self, lenght_arg, l_arg=None, trld_edgs_quant_arg=0):
        if trld_edgs_quant_arg == lenght_arg:  # gets the objective
            self.return_var = True
        if l_arg is None:
            self.return_var = False  # declarating local static variable
            c_el = 0  # excludes main diagonal
            for l in range(len(self.N)):
                c_el += 1
                for c in range(c_el, len(self.M[l])):
                    elm = self.M[l][c]  # element of the position of the matrix
                    if elm >= 1:
                        # calls the recursion whereas each vertex as the beginnig of a path
                        trld_edgs_quant_arg += 1
                        self.comprimento_de_tamanho_n(lenght_arg=lenght_arg, l_arg=c, trld_edgs_quant_arg=trld_edgs_quant_arg)
                        trld_edgs_quant_arg -= 1
        else:
            for c in range(l_arg + 1, len(self.M[l_arg])):
                elm = self.M[l_arg][c]  # element of the position of the matrix
                if elm >= 1:
                    # calls the recursion to jump to another line of the matrix
                    trld_edgs_quant_arg += 1
                    self.comprimento_de_tamanho_n(lenght_arg=lenght_arg, l_arg=c, trld_edgs_quant_arg=trld_edgs_quant_arg)
                    trld_edgs_quant_arg -= 1
        return self.return_var

    """
    def ha_ciclo(self, l_arg=None, c_arg=None):
        if l_arg is c_arg is None:
            self.return_var = []
            # 1__ edges translator
            self.dit_a = {}  # declarating local static variable
            a = None
            c_el = -1
            elm = None
            counter = 1
            for l in range(len(self.N)):
                c_el += 1
                for e in range(c_el, len(self.M[l])):
                    elm = self.M[l][e]
                    if elm == 1:
                        if l not in self.dit_a.keys():
                            self.dit_a[l] = {}
                        if e not in self.dit_a[l].keys():
                            self.dit_a[l][e] = []
                        a = "a{}".format(counter)
                        counter += 1
                        self.dit_a[l][e].append(a)
                    elif elm > 1:
                        if l not in self.dit_a.keys():
                            self.dit_a[l] = {}
                        if e not in self.dit_a[l].keys():
                            self.dit_a[l][e] = []
                        for i in range(elm):
                            a = "a{}".format(counter)
                            counter += 1
                            self.dit_a[l][e].append(a)
            # 1__ edges translator
            self.path = [] # declarating local static variable (return obj)
            c_el = -1  # excludes main diagonal
            for l in range(len(self.N)):
                c_el += 1
                self.path.clear()
                current_vertex = self.N[l]
                self.path.append(current_vertex)
                for c in range(c_el, len(self.M[l])):
                    elm = self.M[l][c]  # element of the position of the matrix
                    if c == l and elm > 0:
                        return [str(self.N[l]), self.dit_a[l][c][0], str(self.N[c])]
                    elif elm >= 2:
                        return [str(self.N[l]), self.dit_a[l][c][0], str(self.N[c]), self.dit_a[l][c][1], str(self.N[l])]
                    elif elm == 1:
                        self.path.append(self.dit_a[l][c][0])
                        # calls the recursion whereas each vertex as the beginnig of a path
                        self.ha_ciclo(l_arg=c, c_arg=l)
                        self.path.remove(self.N[c])
                        self.path.remove(self.dit_a[l][c][0])
        else:
            current_vertex = self.N[l_arg]
            self.path.append(current_vertex)
            # for c in range(l_arg + 1, len(self.M[l_arg])):
            #     elm = self.M[c_arg][c]
            #     if elm >= 1:
            #         self.path.append(self.dit_a[l_arg][c][0])
            #         self.path.append(self.N[c_arg])
            for c in range(l_arg + 1, len(self.M[l_arg])):
                elm = self.M[c_arg][c]
                if self.M[l_arg][c] >= 1 and elm >= 1:
                    self.path.append(self.dit_a[l_arg][c][0])
                    self.path.append(self.N[c])
                    self.path.append(self.dit_a[c_arg][c][0])
                    self.path.append(self.N[c_arg])
                    self.return_var = self.path.copy()
                elm = self.M[l_arg][c]  # element of the position of the matrix
                if elm >= 1:
                    self.path.append(self.dit_a[l_arg][c][0])
                    # calls the recursion to jump to another line of the matrix
                    self.ha_ciclo(l_arg=c, c_arg=c_arg)
                    self.path.remove(self.N[c])
                    self.path.remove(self.dit_a[l_arg][c][0])

        if len(self.return_var) > 0:
            return self.return_var
        else:
            return False
    """

    # deu certo
    def ha_ciclo(self, has_dit=False, v_partida=None, line_index=None):
        if has_dit is False and v_partida is None and line_index is None:
            self.path_ret = []
            self.path = []
            # 1__ edges translator
            self.dit_a = {}  # declarating local static variable
            a = None
            c_el = -1
            elm = None
            counter = 1
            for l in range(len(self.N)):
                c_el += 1
                for e in range(c_el, len(self.M[l])):
                    elm = self.M[l][e]
                    if elm == 1:
                        if l not in self.dit_a.keys():
                            self.dit_a[l] = {}
                        if e not in self.dit_a[l].keys():
                            self.dit_a[l][e] = []
                        a = "a{}".format(counter)
                        counter += 1
                        self.dit_a[l][e].append(a)
                    elif elm > 1:
                        if l not in self.dit_a.keys():
                            self.dit_a[l] = {}
                        if e not in self.dit_a[l].keys():
                            self.dit_a[l][e] = []
                        for i in range(elm):
                            a = "a{}".format(counter)
                            counter += 1
                            self.dit_a[l][e].append(a)
            # 1__ edges translator

            ev = -1
            for l in range(len(self.N)):
                ev += 1
                for e in range(ev, len(self.N)):
                    elm = self.M[l][e]
                    if e == l and elm >=1:
                        return [self.N[l], self.dit_a[l][e][0], self.N[l]]
                    elif e != l and elm >= 2:
                        return [self.N[l], self.dit_a[l][e][0], self.N[e], self.dit_a[l][e][1], self.N[l]]
            self.ha_ciclo(has_dit=True)


        elif has_dit is True and v_partida is None and line_index is None:
            ev = 0
            for l in range(len(self.N)):
                ev += 1
                for e in range(ev, len(self.N)):
                    elm = self.M[l][e]
                    if elm > 0:
                        vertice = self.N[l]
                        aresta = self.dit_a[l][e][0]
                        self.path.clear()
                        self.path.append(vertice)
                        self.path.append(aresta)
                        self.ha_ciclo(has_dit=True, v_partida=vertice, line_index=e)

        elif has_dit is True and v_partida is not None and line_index is not None:
            vertice_recebido = self.N[line_index]
            self.path.append(vertice_recebido)

            if self.path[0] == self.path[-1]:
                self.path_ret = self.path.copy()
                return self.path_ret

            coluna_de_retorno = line_index
            linha_de_retorno = self.N.index(self.path[0])
            elm_de_retorno = self.M[linha_de_retorno][coluna_de_retorno]
            if elm_de_retorno > 0:
                aresta_de_retorno = self.dit_a[linha_de_retorno][coluna_de_retorno][0]
                if aresta_de_retorno not in self.path: # pode retornar e feichar o ciclo
                    #self.path.append(self.N[coluna_de_retorno])
                    self.path.append(self.dit_a[linha_de_retorno][coluna_de_retorno][0])
                    self.ha_ciclo(has_dit=True, v_partida=self.path[0], line_index=linha_de_retorno)

            for e in range(line_index + 1, len(self.N)):
                elm = self.M[line_index][e]
                if elm > 0:
                    aresta = self.dit_a[line_index][e][0]
                    self.path.append(aresta)
                    self.ha_ciclo(has_dit=True, v_partida=self.path[0], line_index=e)

        return self.path_ret

    """
    # não deu certo
    def ha_ciclo(self, has_dit=False, vertice_enviado=None):
        if has_dit is False:
            self.path_ret = []
            self.path = []
            # 1__ edges translator
            self.dit_a = {}  # declarating local static variable
            a = None
            c_el = -1
            elm = None
            counter = 1
            for l in range(len(self.N)):
                c_el += 1
                for e in range(c_el, len(self.M[l])):
                    elm = self.M[l][e]
                    if elm == 1:
                        if l not in self.dit_a.keys():
                            self.dit_a[l] = {}
                        if e not in self.dit_a[l].keys():
                            self.dit_a[l][e] = []
                        a = "a{}".format(counter)
                        counter += 1
                        self.dit_a[l][e].append(a)
                    elif elm > 1:
                        if l not in self.dit_a.keys():
                            self.dit_a[l] = {}
                        if e not in self.dit_a[l].keys():
                            self.dit_a[l][e] = []
                        for i in range(elm):
                            a = "a{}".format(counter)
                            counter += 1
                            self.dit_a[l][e].append(a)
            # 1__ edges translator

            # tradutor e aresta
            self.dit_a_td = {}
            ev = -1
            for l in range(len(self.N)):
                ev += 1
                for e in range(ev, len(self.M[l])):
                    elm = self.M[l][e]
                    for i in range(elm):
                        self.dit_a_td[self.dit_a[l][e][i]] = list("{}{}".format(self.N[l], self.N[e]))


            ev = -1
            for l in range(len(self.N)):
                ev += 1
                for e in range(ev, len(self.N)):
                    elm = self.M[l][e]
                    if e == l and elm >=1:
                        return [self.N[l], self.dit_a[l][e][0], self.N[l]]
                    elif e != l and elm >= 2:
                        return [self.N[l], self.dit_a[l][e][0], self.N[e], self.dit_a[l][e][1], self.N[l]]
            self.ha_ciclo(has_dit=True)


        elif has_dit is True and vertice_enviado is None:
            ev = 0
            for v in range(len(self.N)):
                ev += 1
                vertice = self.N[v]
                lis_a = []
                for c in range(ev, len(self.N)):  # arestas na linha
                    elm = self.M[v][c]
                    if elm > 0:
                        aresta = self.dit_a[v][c][0]
                        lis_a.append(aresta)

                for l in range(0, ev):  # arestas na coluna
                    elm = self.M[l][v]
                    if l != v:
                        aresta = self.dit_a[l][v][0]
                    if elm > 0 and aresta not in lis_a:
                        lis_a.append(aresta)

                self.path.append(vertice)
                for a in lis_a:
                    self.path.append(a)
                    ck = self.dit_a_td[a].copy()
                    ck.remove(vertice)
                    ck = ck[0]
                    self.ha_ciclo(has_dit=True, vertice_enviado=ck)
                    self.path.remove(a)
                self.path.remove(vertice)

        elif has_dit is True and vertice_enviado is not None:
            self.path.append(vertice_enviado)

            if self.path[0] == self.path[-1]:
                self.path_ret = self.path.copy()
                return self.path_ret

            v = self.N.index(vertice_enviado)
            lis_a = []
            for c in range(v + 1, len(self.N)):  # arestas na linha
                elm = self.M[v][c]
                if elm > 0:
                    aresta = self.dit_a[v][c][0]
                    lis_a.append(aresta)

            for l in range(0, v):  # arestas na coluna
                elm = self.M[l][v]
                if v != l:
                    aresta = self.dit_a[l][v][0]
                if elm > 0 and aresta not in lis_a:
                    lis_a.append(aresta)

            for a in lis_a:
                if a not in self.path:
                    self.path.append(a)
                    ck = self.dit_a_td[a].copy()
                    ck.remove(vertice_enviado)
                    ck = ck[0]
                    self.ha_ciclo(has_dit=True, vertice_enviado=ck)
                    self.path.remove(ck)
                    self.path.remove(a)


        return self.path_ret
    """


    # def eh_conexo(self):
    #     # para ser conexo baste que todas as colunas do grafo tenham pelo menos um 1
    #     ct = 0
    #     elm = None
    #     it_broke = False
    #     for c in range(1, len(self.N)):
    #         it_broke = False
    #         ct += 1
    #         for l in range(0, ct):
    #             elm = self.M[l][c]
    #             if elm >= 1:
    #                 it_broke = True
    #                 ll_ = l
    #                 break
    #         if it_broke == False:
    #             ainda_continua_conexo = False
    #             # vai atras de uma outra conexão
    #             for e in range(len(self.N) - c + 1, len(self.N)):
    #                 elm1 = self.M[c][e]
    #                 if elm1 >= 1:
    #                     # verifica o elemento de cima
    #                     if self.M[c][e - 1] >= 1:
    #                         ainda_continua_conexo = True
    #             if ainda_continua_conexo == False:
    #                     return False
    #     return True

    def eh_conexo(self):
        vert = []
        ev = 0
        for l in range(len(self.N)):
            ev += 1
            count = 0
            if len(self.N) > 1:
                for e in range(ev, len(self.N)):
                    elm = self.M[l][e]
                    if elm >= 1:
                        if len(vert) == 0:
                            vert.append(self.N[l])
                        count += 1
                        if self.N[e] not in vert:
                            vert.append(self.N[e])
                if count == 0:
                    if self.N[l] in vert:
                        pass
                    else:
                        return False
            else:
                return True

        if len(vert) == len(self.N):
            return True
        return False
    # DESAFIOS

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''

        # Dá o espaçamento correto de acordo com o tamanho do string do maior vértice
        espaco = ' '*(self.__maior_vertice)

        grafo_str = espaco + ' '

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca o espaço se não for o último vértice
                grafo_str += ' '

        grafo_str += '\n'

        for l in range(len(self.M)):
            grafo_str += self.N[l] + ' '
            for c in range(len(self.M)):
                grafo_str += str(self.M[l][c]) + ' '
            grafo_str += '\n'

        return grafo_str































