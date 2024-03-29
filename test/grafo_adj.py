from copy import copy, deepcopy
from math import inf

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

        """
        g
          C D
        C 1 0 
        D 1 0 
        """

        self.MD = {}  # g.MD = {'a2': ['D-C', 1], 'a1': ['C-C', 1]}
        self.VA = {}  # {'D': ['a2'], 'C': ['a1', 'a2']} para grafos não direcionados
        self.VAD = {}  # {'C': ['a1'], 'D': ['a2']} para grafos direcionados
        self.counter = 1  # contador para a gravação das chaves (arestas) do self.MD { "a{}".format(selfcounter) }

        if len(M) != len(N):
            raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for c in M:
            if len(c) != len(N):
                raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for i in range(len(N)):
            for j in range(len(N)):
                aresta = N[i] + Grafo.SEPARADOR_ARESTA + N[j]
                if not(self.aresta_valida(aresta)):
                    raise ArestaInvalidaException('A aresta ' + aresta + ' é inválida')

        self.M = M

    """Creates a default implementation"""
    def __eq__(self, other):
        if self.VA == other.VA and self.VAD == other.VAD and self.MD == other.MD:
            return True
        return False

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

    def primeiro_vertice_aresta(self, a: str):
        return a[0:a.index(Grafo.SEPARADOR_ARESTA)]

    def segundo_vertice_aresta(self, a: str):
        return a[a.index(Grafo.SEPARADOR_ARESTA)+1:]

    def indice_primeiro_vertice_aresta(self, a: str):
        return self.N.index(self.primeiro_vertice_aresta(a))

    def indice_segundo_vertice_aresta(self, a: str):
        return self.N.index(self.segundo_vertice_aresta(a))

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
                    if self.M[self.indice_primeiro_vertice_aresta(a)][self.indice_segundo_vertice_aresta(a)]:
                        existe = True

        return existe

    def adiciona_vertice(self, v):
        if self.vertice_valido(v):
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

            self.N.append(v)
            self.M.append([])
            for k in range(len(self.N)):
                if k != len(self.N) -1:
                    self.M[k].append(0)
                self.M[self.N.index(v)].append(0)
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adiciona_aresta(self, a):
        peso = a[-1]
        if self.aresta_valida(a[0]) and self.peso_valido(peso):
            self.M[self.indice_primeiro_vertice_aresta(a[0])][self.indice_segundo_vertice_aresta(a[0])] += 1
            aresta = "a{}".format(self.counter)
            self.counter += 1
            self.MD[aresta] = [a[0], peso]

            # para grafo não direcionado
            if a[0][0] in self.VA.keys():
                if aresta not in self.VA[a[0][0]]:
                    self.VA[a[0][0]].append(aresta)
            else:
                self.VA[a[0][0]] = [aresta]
            if a[0][-1] in self.VA.keys():
                if aresta not in self.VA[a[0][-1]]:
                    self.VA[a[0][-1]].append(aresta)
            else:
                self.VA[a[0][-1]] = [aresta]

            # para grafo direcionado
            if a[0][0] in self.VAD.keys():
                if aresta not in self.VAD[a[0][0]]:
                    self.VAD[a[0][0]].append(aresta)
            else:
                self.VAD[a[0][0]] = [aresta]

        else:
            ArestaInvalidaException('A aresta ' + self.A[a[0]] + ' é inválida')

    def peso_valido(self, p):
        if 0 < p < inf:
            return True
        return False

    # FUNÇÕES

    def fontes(self, ditD, ditND):
        """
        g
          C D
        C 1 0
        D 1 0
        1 = {'D': ['a2'], 'C': ['a1', 'a2']} para grafos não direcionados
        2 = {'C': ['a1'], 'D': ['a2']} para grafos direcionados
        :param ditD: um dicionario que representa as arestas como direcionadas como o 2
        :param ditND: um dicionario que representa as arestas como não direcionadas como o 1
        :return: todos os vertices fontes do grafo naquele momento dentro de uma lista
        """
        fontes = []
        for v in ditD.keys():
            lis1 = sorted(ditD[v])
            lis2 = sorted(ditND[v])
            if lis1 == lis2:
                fontes.append(v)
        return fontes

    def limpandoFontesDoGrafo(self, fontes, ditD, ditND):
        """
        g
          C D
        C 1 0
        D 1 0
        1 = {'D': ['a2','a3'], 'C': ['a1', 'a2', 'a3']} para grafos não direcionados
        2 = {'D': ['a2', 'a3'], 'C': ['a1']} para grafos direcionados
        :param fontes: todos os vertices fontes do grafo naquele momento
        :param ditD: um dicionario que representa as arestas como direcionadas como o 2
        :param ditND: um dicionario que representa as arestas como não direcionadas como o 1
        :result: ditD = {'C': ['a1']} para grafos não direcionados
                ditND = {'C': ['a1']} para grafos direcionados
        """
        arRem = []
        for f in fontes:
            for ed in ditND[f]:
                arRem.append(ed)
        for k in ditND.keys():
            edRem = []
            for ar in ditND[k]:
                if ar in arRem:
                    edRem.append(ar)
            for ed in edRem:
                ditND[k].remove(ed)
        for f in fontes:
            del ditND[f]
            del ditD[f]

    def Khan(self):
        """
        g
          C D
        C 1 0
        D 1 0
        :return: Lista ordenada todologicamente tipo ['D', 'C']
        """
        OrdTopo = []
        ditD = deepcopy(self.VAD)
        ditND = deepcopy(self.VA)
        while len(OrdTopo) != len(self.N):
            fontes = self.fontes(ditD, ditND)
            for f in fontes:
                OrdTopo.append(f)
            self.limpandoFontesDoGrafo(fontes, ditD, ditND)
        return OrdTopo

    # FUNÇÕES

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
