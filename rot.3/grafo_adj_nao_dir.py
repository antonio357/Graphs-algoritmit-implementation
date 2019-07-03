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

    def __init__(self, N=[], M=[]):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param N: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma matriz de adjacência que guarda as arestas do grafo. Cada entrada da matriz tem um inteiro que indica a quantidade de arestas que ligam aqueles vértices
        '''
        for v in N:
            if not(Grafo.vertice_valido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

        self.N = N

        if len(M) != len(N):
            raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for c in M:
            if len(c) != len(N):
                raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for i in range(len(N)):
            for j in range(len(N)):
                '''
                Verifica se os índices passados como parâmetro representam um elemento da matriz abaixo da diagonal principal.
                Além disso, verifica se o referido elemento é um traço "-". Isso indica que a matriz é não direcionada e foi construída corretamente.
                '''
                if i>j and not(M[i][j] == '-'):
                    raise MatrizInvalidaException('A matriz não representa uma matriz não direcionada')


                aresta = N[i] + Grafo.SEPARADOR_ARESTA + N[j]
                if not(self.aresta_valida(aresta)):
                    raise ArestaInvalidaException('A aresta ' + aresta + ' é inválida')

        self.M = M

    def aresta_valida(self, aresta=''):
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

        if not(self.existe_vertice(aresta[:i_traco])) or not(self.existe_vertice(aresta[i_traco + 1:])):
            return False

        return True

    @classmethod
    def vertice_valido(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existe_vertice(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.vertice_valido(vertice) and self.N.count(vertice) > 0

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

    def existe_aresta(self, a: str):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.aresta_valida(self, a):
            for i in range(len(self.M)):
                for j in range(len(self.M)):
                    if self.M[self.__indice_primeiro_vertice_aresta(a)][self.__indice_segundo_vertice_aresta(a)]:
                        existe = True

        return existe

    def adiciona_vertice(self, v):
        '''
        Inclui um vértice no grafo se ele estiver no formato correto.
        :param v: O vértice a ser incluído no grafo.
        :raises VerticeInvalidoException se o vértice já existe ou se ele não estiver no formato válido.
        '''
        if v in self.N:
            raise VerticeInvalidoException('O vértice {} já existe'.format(v))

        if self.vertice_valido(v):
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

    def adiciona_aresta(self, a):
        '''
        Adiciona uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
        if self.aresta_valida(a):
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
        if self.aresta_valida(a):
            i_a1 = self.__indice_primeiro_vertice_aresta(a)
            i_a2 = self.__indice_segundo_vertice_aresta(a)
            if i_a1 < i_a2:
                self.M[i_a1][i_a2] -= 1
            else:
                self.M[i_a2][i_a1] -= 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    # FUNÇÕES IMPLEMENTADAS

    # EH_CONEXO
    def arestas_associadas_possiveis_de_viajar_conexo(self, vertice):
        aresta_posiveis = []
        l = self.N.index(vertice)
        # conferi na linha
        for c in range(l + 1, len(self.N)):
            elm = self.M[l][c]
            for i in range(elm):
                a = self.dicionario_arestas_conexo[l][c][i]
                if self.aresta_ja_percorrida_conexo(a) is False:
                    aresta_posiveis.append(a)
        # conferi na coluna
        for e in range(0, l):
            elm = self.M[e][l]
            for i in range(elm):
                a = self.dicionario_arestas_conexo[e][l][i]
                if self.aresta_ja_percorrida_conexo(a) is False:
                    aresta_posiveis.append(a)
        if len(aresta_posiveis) > 0:
            return aresta_posiveis.copy()
        return []

    def aresta_ja_percorrida_conexo(self, aresta):
        for a in self.arestas_passadas_conexo:
            if aresta == a:
                return True
        return False

    def new_eh_conexo(self):
        self.dicionario_arestas_conexo = self.tradutor_de_arestas()
        self.vertices_percorridos_conexo = []
        self.arestas_passadas_conexo = []
        self.vertices_das_arestas_conexo = self.abridor_de_arestas()
        vertice_de_partida = self.N[0]
        self.vertices_percorridos_conexo.append(vertice_de_partida)
        self.path_travaler_conexo(vertice_de_partida)
        # print(self.vertices_percorridos_conexo)
        if len(self.vertices_percorridos_conexo) == len(self.N):
            return True
        return False

    def next_vertice_conexo(self, aresta, vertice_atual):
        aresta = self.vertices_das_arestas_conexo[aresta]
        if aresta[0] == vertice_atual:
            return aresta[-1]
        elif aresta[-1] == vertice_atual:
            return aresta[0]

    def path_travaler_conexo(self, vertice_atual):
        if vertice_atual not in self.vertices_percorridos_conexo:
            self.vertices_percorridos_conexo.append(vertice_atual)
        arestas = self.arestas_associadas_possiveis_de_viajar_conexo(vertice_atual)
        for a in arestas:
            self.arestas_passadas_conexo.append(a)
            self.path_travaler_conexo(self.next_vertice_conexo(a, vertice_atual))
    # EH_CONEXO


    # def eh_conexo(self):
    #     vert = []
    #     ev = 0
    #     for l in range(len(self.N)):
    #         ev += 1
    #         count = 0
    #         if len(self.N) > 1:
    #             for e in range(ev, len(self.N)):
    #                 elm = self.M[l][e]
    #                 if elm >= 1:
    #                     if len(vert) == 0:
    #                         vert.append(self.N[l])
    #                     count += 1
    #                     if self.N[e] not in vert:
    #                         vert.append(self.N[e])
    #             if count == 0:
    #                 if self.N[l] in vert:
    #                     pass
    #                 else:
    #                     return False
    #         else:
    #             return True
    #
    #     if len(vert) == len(self.N):
    #         return True
    #     return False

    def grau(self, vertice):
        # percorre a matirz
        c_el = 0
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

    def caminho_euleriano(self):
        if self.new_eh_conexo() is False: # ve se e conexo
            return False
        else: # ve os graus dos vertices
            # quantos vertices tem graus impar
            q_a_imp = 0
            dit_a_g = {} # dicionario com os vertices e seus respectivos graus
            for v in self.N:
                grau = self.grau(v)
                dit_a_g[v] = grau
                if grau % 2 != 0:
                    q_a_imp += 1

            if q_a_imp == 0:
                return True
            elif q_a_imp > 0:
                if q_a_imp != 2:
                    return False
                elif q_a_imp == 2:
                    return True

    def tradutor_de_arestas(self): # 1__ edges translator
        dit_a = {}  # declarating local static variable
        a = None
        c_el = 0
        elm = None
        counter = 1
        for l in range(len(self.N)):
            c_el += 1
            for e in range(c_el, len(self.M[l])):
                elm = self.M[l][e]
                if elm == 1:
                    if l not in dit_a.keys():
                        dit_a[l] = {}
                    if e not in dit_a[l].keys():
                        dit_a[l][e] = []
                    a = "a{}".format(counter)
                    counter += 1
                    dit_a[l][e].append(a)
                elif elm > 1:
                    if l not in dit_a.keys():
                        dit_a[l] = {}
                    if e not in dit_a[l].keys():
                        dit_a[l][e] = []
                    for i in range(elm):
                        a = "a{}".format(counter)
                        counter += 1
                        dit_a[l][e].append(a)
        return dit_a.copy()

    def abridor_de_arestas(self):
        dit_a = self.tradutor_de_arestas()
        dit_a_td = {}
        ev = 0
        for l in range(len(self.N)):
            ev += 1
            for e in range(ev, len(self.M[l])):
                elm = self.M[l][e]
                for i in range(elm):
                    dit_a_td[dit_a[l][e][i]] = list("{}{}".format(self.N[l], self.N[e]))
        return dit_a_td

    def como_deve_ser_caminho_euleriano_path(self):
        # ve os graus dos vertices
        # quantos vertices tem graus impar
        q_a_imp = 0
        dit_a_g = {} # dicionario com os vertices e seus respectivos graus
        vertice_inicial = None
        vertice_final = None
        for v in self.N:
            grau = self.grau(v)
            dit_a_g[v] = grau
            if grau % 2 != 0:
                q_a_imp += 1
                if vertice_inicial is None:
                    vertice_inicial = v
                else:
                    vertice_final = v

        if q_a_imp == 0: # deve começar e terminar no mesmo vertice
            return []
        elif q_a_imp == 2: # deve começar em um vertice e terminar em outro
            return [vertice_inicial, vertice_final]

    def caminho_euleriano_path(self, how=None): # main for caminho eureliano
        if how is None:
            if self.caminho_euleriano() is False:
                return False
            else:
                lis_vertices_inicio_fim = self.como_deve_ser_caminho_euleriano_path()
                if len(lis_vertices_inicio_fim) == 0:
                    return self.caminho_euleriano_path(lis_vertices_inicio_fim)
                elif len(lis_vertices_inicio_fim) == 2:
                    return self.caminho_euleriano_path(lis_vertices_inicio_fim)
        else:
            """ condições de caminho eureliano
                percorrer todas as arestas apenas uma vez
                1 -- no caso de não haver vertices ímpares, o caminho começa em qualquer vertice e termina neste mesmo
                2 -- no caso de haver dois vertices ímpares,  o caminho começa em um vertice vertice ímpar e termina no outro vertice ímpar
            """
            # condições de parada distintas e recursividades distintas
            self.arestas_percorridas = []
            self.dicionario_arestas = self.tradutor_de_arestas()
            self.vertices_das_arestas = self.abridor_de_arestas()
            self.quantidade_arestas = len(self.vertices_das_arestas.keys())
            self.path = False
            if len(how) == 0:
                for v in self.N:  # tenta com todos os vertices como inicio
                    self.path_traveler(vertice_inicial=v, vertice_final=v)
                    if self.path is not False:
                        break
                return self.path
            elif len(how) == 2:
                self.path_traveler(vertice_inicial=how[0], vertice_final=how[1])
                if self.path is False:
                    self.path_traveler(vertice_inicial=how[1], vertice_final=how[0])
            return self.path

    def path_traveler(self, vertice_inicial, vertice_final, vertice_atual=None):
        # condissao de parada
        if vertice_atual == vertice_final and len(self.arestas_percorridas) == self.quantidade_arestas and self.path is False:
            self.tentativa_path.append(vertice_atual)
            self.path = self.tentativa_path.copy()

        # lista de arestas de um vertice
        if vertice_atual is None:
            self.tentativa_path = [] # é inicializado apenas uma vez
            self.tentativa_path.append(vertice_inicial)
            arestas_associadas = self.arestas_associadas_possiveis_de_viajar(vertice_inicial)
            vertice_atual = vertice_inicial
        else:
            self.tentativa_path.append(vertice_atual)
            arestas_associadas = self.arestas_associadas_possiveis_de_viajar(vertice_atual)

        for a in arestas_associadas:
            self.tentativa_path.append(a)
            self.arestas_percorridas.append(a)
            self.path_traveler(vertice_inicial, vertice_final, vertice_atual=self.next_vertice(a, vertice_atual))
            del self.tentativa_path[-1]
            self.tentativa_path.remove(a)
            self.arestas_percorridas.remove(a)

    def quantas_vezes_passou_pelo_vertice(self, vertice):
        cont = 0
        for inf in self.tentativa_path:
            if inf == vertice:
                cont += 1
        return cont

    def next_vertice(self, aresta, vertice_atual):
        aresta = self.vertices_das_arestas[aresta]
        if aresta[0] == vertice_atual:
            return aresta[-1]
        elif aresta[-1] == vertice_atual:
            return aresta[0]

    def arestas_associadas_possiveis_de_viajar(self, vertice):
        aresta_posiveis = []
        l = self.N.index(vertice)
        # conferi na linha
        for c in range(l + 1, len(self.N)):
            elm = self.M[l][c]
            for i in range(elm):
                a = self.dicionario_arestas[l][c][i]
                if self.aresta_ja_percorrida(a) is False:
                    aresta_posiveis.append(a)
        # conferi na coluna
        for e in range(0, l):
            elm = self.M[e][l]
            for i in range(elm):
                a = self.dicionario_arestas[e][l][i]
                if self.aresta_ja_percorrida(a) is False:
                    aresta_posiveis.append(a)
        if len(aresta_posiveis) > 0:
            return aresta_posiveis.copy()
        return []

    def aresta_ja_percorrida(self, aresta):
        for a in self.arestas_percorridas:
            if aresta == a:
                return True
        return False

    # FUNÇÕES IMPLEMENTADAS

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