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

    """
    :argument; vertice atual -> x, vertice em analise -> y
    armazena x em self.verticesDecendencia[y] se y for descendente de x
    """
    def associatesKinchip(self, x, y):
        if y in self.verticesDescendencia.keys():
            self.verticesDescendencia[y].append(x)
        else:
            self.verticesDescendencia[y] = [x]

    """
    :argument; descendant, fatherV
    :returns boolean; True se descendanat descender de fatherV, e False caso contrario
    """
    def isDescendant(self, descendanat, fatherV):
        if descendanat == fatherV:
            return True
        if descendanat in self.verticesDescendencia.keys():
            return self.isDescendant(self.verticesDescendencia[descendanat], fatherV)
        else:
            return False

    """
    :argument; vertice atual -> actualV, vertice em analise -> proximoV
    :return; '->' = proximoV é descendente de actualV, '<-' = actualV e descendente de proximoV, '-' = não ha parentesco
    """
    def kinchipRelation(self, actualV, proximoV):
        if self.isDescendant(proximoV, actualV):
            return '->'
        elif self.isDescendant(actualV, proximoV):
            return '<-'
        else:
            return '-'


    """
    :argument; uma aresta e o vertice atual
    :return; o tipo de aresta, (aresta da arvore, aresta de retorno, laço)
    """
    def arestaType(self, E, V):
        a = self.MD[E][0]
        if a[0] == a[-1]:
            return "laço"
        if a[0] == V:
            proximoV = a[-1]
            actualV = a[0]
        else:
            proximoV = a[0]
            actualV = a[-1]

        Kinship = self.kinchipRelation(actualV, proximoV)

        if self.D is False:
            if Kinship == '<-':
                return "retorno"
            else:
                return "arvore"
        else:
            if proximoV in self.verticesNum.keys():
                # traz
                if Kinship == '<-' and self.verticesNum[actualV] > self.verticesNum[proximoV]:
                    return self.I
                # frente
                elif Kinship == '->' and self.verticesNum[proximoV] > self.verticesNum[actualV]:
                    # print("retornou para frente")
                    return self.III
                # cruzada
                elif Kinship == '-' and self.verticesNum[actualV] > self.verticesNum[proximoV]:
                    return self.II
                else:
                    print("this is not expected never hapened before")
                    return "this is not expected never hapened before"
            else:
                # print("return normal")
                return "arvore"

    """
    :argument; um grafo (leva em consideração que o grafo não é direcionado) 
    :process; uma busca em profundidade 
    :return; uma arvore em forma de grafo direcionado
    """
    def BuscaEmProfundidadeGrafos(self, D=False):
        self.D = D
        self.counter = 1
        self.raiz = self.N[0]  # verice raiz
        self.verticesDescendencia = {}  # guarda os vertices que já foram analisados e suas pais {'A': None, 'B': 'A'}
        self.verticesNum = {}  # guarda os vertices que já foram analisados e suas numerações {'A': 1, 'B': 2}
        self.arestas = {}  # guarda as arestas já analisadas e seu tipo {'a1': 'arvore', 'a2': 'retorno', 'a3': 'laço'}
        if D is False:
            self.recursion(self.raiz)  # seta os 3 dicionarios acima
            # print("Pais = {}".format(self.verticesDescendencia))
            # print("Num = {}".format(self.verticesNum))
            # print("arestas = {}".format(self.arestas))
            # l = []
            # for ed in self.arestas.keys():
            #     if self.arestas[ed] == 'arvore':
            #         l.append(self.MD[ed])
            # print("l = {}".format(l))
            if len(self.verticesNum.keys()) == len(self.N):
                return self.builderBuscaEmProfundidadeGrafosNaoDirecionados()
            return "Não é conexo"
        else:
            self.I = "traz"
            self.II = "cruzada"
            self.III = "frente"
            # constroi as arvores da floresta
            self.quantArvores = 0
            while self.raiz is not False:
                self.quantArvores += 1
                self.recursionDirecionada(self.raiz)  # seta os 3 dicionarios acima
                self.raiz = self.findAnother()
        # print("Pais = {}".format(self.verticesDescendencia))
        # print("Num = {}".format(self.verticesNum))
        # print("arestas = {}".format(self.arestas))
        # l = []
        # for ed in self.arestas.keys():
        #     if self.arestas[ed] == 'arvore':
        #         l.append(self.MD[ed])
        # print("l = {}".format(l))
        return self.builderBuscaEmProfundidadeGrafosNaoDirecionados()

    """
    apartir do rerultado de uma busca em profundiade em uma grafo direcionado
    e com a qualtidade de arestas cruzadas == quantidade de arvores - 1 da floresta resultante 
    :return; True se o grafo era conexo ou False se era desconexo antes da busca em profundidade 
    """
    # def eraConexa(self):
    #     counterCR = 0
    #     for edType in self.arestas.values():
    #         if edType == self.II:
    #             counterCR += 1
    #     if counterCR >= self.quantArvores - 1:
    #         return True
    #     return False


    """
    procura por outro vertice que ainda não foi explorado para se tornar outra raiz
    de uma outra arvore da floresta que será retornada, caso não haja como construir outro retorna False
    """
    def findAnother(self):
        for v in self.N:
            if v not in self.verticesNum.keys():
                return v
        return False

    """
    faz busca em profundidade recursivamente para grafos não direcionados
    manipulando variaveis estaticas locais da função que a precede
    """
    def recursion(self, v):
        if v == self.raiz:
            self.verticesNum[self.raiz] = self.counter
            self.counter += 1

        if v in self.VA.keys():
            for a in self.VA[v]:
                if a not in self.arestas.keys():
                    tipo = self.arestaType(a, v)
                    self.arestas[a] = tipo
                    if tipo == "arvore":
                        proximo_vertice = self.next(a, v)
                        self.verticesNum[proximo_vertice] = self.counter
                        self.counter += 1
                        self.verticesDescendencia[proximo_vertice] = v
                        self.recursion(proximo_vertice)

    """
    faz busca em profundidade recursivamente para grafos direcionados
    manipulando variaveis estaticas locais da função que a precede
    """
    def recursionDirecionada(self, v):
        # print("\nV = {}\n".format(v))
        if v == self.raiz:
            self.verticesNum[self.raiz] = self.counter
            self.counter += 1

        if v in self.VAD.keys():
            # print("\nverice_atual = {}".format(v))
            # print("suas arestas = {}\n".format(self.VAD[v]))
            for a in self.VAD[v]:
                # print("\n aresta em nalalise = {} do vertice = {}".format(a, v))
                if a not in self.arestas.keys():
                    tipo = self.arestaType(a, v)
                    self.arestas[a] = tipo
                    if tipo == "arvore":
                        proximo_vertice = self.next(a, v)
                        self.verticesNum[proximo_vertice] = self.counter
                        self.counter += 1
                        self.verticesDescendencia[proximo_vertice] = v
                        self.recursionDirecionada(proximo_vertice)

    """
    apartir do vertice e da aresta atual da recursion 
    diz qual o proximo vertice que a recursion deve viajar
    """
    def next(self, E, V):
        string = self.MD[E][0]
        if string[0] == V:
            return string[-1]
        return string[0]

    """
    constroi um grafo e retorna a referencia deste
    """
    def builderBuscaEmProfundidadeGrafosNaoDirecionados(self):
        g = Grafo([],[])
        for v in self.N:
            g.adiciona_vertice(v)
        for e in self.arestas:
            if self.arestas[e] == "arvore":
                g.adiciona_aresta(self.MD[e])
        # print(g)
        return g

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
