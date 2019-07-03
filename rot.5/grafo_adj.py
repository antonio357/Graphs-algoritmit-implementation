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
        if self.aresta_valida(a):
            self.M[self.indice_primeiro_vertice_aresta(a)][self.indice_segundo_vertice_aresta(a)] += 1
        else:
            ArestaInvalidaException('A aresta ' + self.A[a] + ' é inválida')

    # FUNÇÕES
    # retira arestas paralelas considerando que o grafo nao é ponderado, e tambem retira lacos
    def define_matrix(self):
        E = deepcopy(self.M)
        for l in range(len(self.N)):
            for c in range(len(self.N)):
                elm = E[l][c]
                if elm > 1:  # remove paralelas
                    E[l][c] = 1
                if l == c:  # remove lacos
                    E[l][c] = 0
        return E

    # retorna uma lista com todos os vertices que da pra chegar com um aresta apartir do vertice dado
    def vertices_seguintes_possiveis(self, vertice, matrix):
        lis = []
        l = self.N.index(vertice)
        for c in range(len(self.N)):
            elm = matrix[l][c]
            if elm >= 1:
                lis.append(self.N[c])
        return lis

    """
    def DijkstraDrone(self, inicial_drone_load=5, max_drone_load=5, load_places=[], vertice_inicial=None, vertice_final=None):
        # setUp drone, dicionario dos vertices
            load = inicial_drone_load  # currenty drone load
            dit_v_at = {}
            for v in self.N:
                dit_v_at[v] = {}
                dit_v_at[v]["beta"] = inf
                dit_v_at[v]["fi"] = 0
                dit_v_at[v]["pi"] = 0 
        # setUp drone, dicionario dos vertices
        # primeiro e segundo passos

        # primeiro e segundo passos
        # recarrega drone se possivel
        if vertice_atual in load_places:
            load = max_drone_load
        # recarrega drone se possivel
        for l in
    """

    # def Dijkstra(self, vertice_inicial, vertice_final):
    #     # setUp, levando em consideração o segundo passo
    #     dit_v_at = {} # dicionario dos vertices
    #     for v in self.N:
    #         dit_v_at[v] = {}
    #         dit_v_at[v]["beta"] = inf
    #         dit_v_at[v]["fi"] = 0
    #         dit_v_at[v]["pi"] = "-"
    #     matrix_at = self.define_matrix()  # definindo matrix sem lacos e sem paralelas
    #     # setUp, levando em consideração o segundo passo
    #     # primeiro passo
    #     dit_v_at[vertice_inicial]["beta"] = 0
    #     dit_v_at[vertice_inicial]["fi"] = 1
    #     # primeiro passo
    #     w = vertice_inicial
    #     while True:
    #         # tracaback and return smallest path
    #         if w == vertice_final:
    #             traceback = []
    #             wi = w
    #             traceback.append(wi)
    #             while wi != vertice_inicial:
    #                 traceback.append(dit_v_at[wi]["pi"])
    #                 wi = dit_v_at[wi]["pi"]
    #             traceback.reverse()
    #             return traceback
    #         # tracaback and return smallest path
    #         b_lis = []
    #         for r in self.vertices_seguintes_possiveis(w, matrix_at):
    #             if dit_v_at[r]["fi"] == 0 and dit_v_at[r]["beta"] > dit_v_at[w]["beta"] + 1:
    #                 dit_v_at[r]["beta"] = dit_v_at[w]["beta"] + 1
    #                 dit_v_at[r]["pi"] = w
    #
    #             b = dit_v_at[r]["beta"]
    #             if b > 0:
    #                 b_lis.append(b)
    #         # b_lis = []
    #         # for v in self.N:
    #         #     b = dit_v_at[v]["beta"]
    #         #     if b > 0:
    #         #         b_lis.append(b)
    #         r_existe = False
    #         for r_ in self.N:
    #             if dit_v_at[r_]["fi"] == 0 and dit_v_at[r_]["beta"] < inf and len(b_lis) > 0 and dit_v_at[r_]["beta"] == min(b_lis):
    #                 r_existe = True
    #                 dit_v_at[r_]["fi"] = 1
    #                 w = r_
    #             if w == vertice_final:
    #                 break
    #         if r_existe is False:
    #             # print("W = {}".format(w))
    #             return "Não existe caminho entre os vertices"

    def Dijkstra(self, vertice_inicial, vertice_final):
        # setUp, levando em consideração o segundo passo
        dit_v_at = {} # dicionario dos vertices
        for v in self.N:
            dit_v_at[v] = {}
            dit_v_at[v]["beta"] = inf
            dit_v_at[v]["fi"] = 0
            dit_v_at[v]["pi"] = "-"
        matrix_at = self.define_matrix()  # definindo matrix sem lacos e sem paralelas
        # setUp, levando em consideração o segundo passo
        # primeiro passo
        dit_v_at[vertice_inicial]["beta"] = 0
        dit_v_at[vertice_inicial]["fi"] = 1
        # primeiro passo
        w = vertice_inicial
        while True:
            # tracaback and return smallest path
            if w == vertice_final:
                traceback = []
                wi = w
                traceback.append(wi)
                while wi != vertice_inicial:
                    traceback.append(dit_v_at[wi]["pi"])
                    wi = dit_v_at[wi]["pi"]
                traceback.reverse()
                # SESSAO DE PRINTS
                # for v in self.N:
                #     print("vertice = {}, beta = {}, fi = {}, pi = {}". format(v, dit_v_at[v]["beta"], dit_v_at[v]["fi"], dit_v_at[v]["pi"]))
                # SESSAO DE PRINTS
                return traceback
            # tracaback and return smallest path
            # b_lis = []
            for r in self.vertices_seguintes_possiveis(w, matrix_at):
                if dit_v_at[r]["fi"] == 0 and dit_v_at[r]["beta"] > dit_v_at[w]["beta"] + 1:
                    dit_v_at[r]["beta"] = dit_v_at[w]["beta"] + 1
                    dit_v_at[r]["pi"] = w

                    # b_lis.append(dit_v_at[r]["beta"])

            r_existe = False
            # pegando todos os betas com fi == 0
            b_lis = []
            for v in self.N:
                if dit_v_at[v]["fi"] == 0:
                    b_lis.append(dit_v_at[v]["beta"])
            # pegando todos os betas com fi == 0
            for r_ in self.N:
                # try:
                if dit_v_at[r_]["fi"] == 0 and dit_v_at[r_]["beta"] < inf and dit_v_at[r_]["beta"] == min(b_lis):
                    r_existe = True
                    dit_v_at[r_]["fi"] = 1
                    w = r_
                    break
                # except ValueError:
                #     # print("w = {}".format(w))
                #     # print("nao conseguiu, vertice = {}, beta = {}, fi = {}, b_lis = {}".format(r_,dit_v_at[r_]["beta"], dit_v_at[r_]["fi"], b_lis))
                #     r_existe = True
                #     dit_v_at[r_]["fi"] = 1
                #     w = r_
                #     break
            if r_existe is False:
                # print("W = {}".format(w))
                return "Não existe caminho entre os vertices"

    def ist_possible(self, vertice_futuru, vertice_inicial, dit_v_at, load_places, inicial_drone_load, max_drone_load):
        dit_v_at = dit_v_at.deepycopy()
        dit_v_at[vertice_futuru]["fi"] = 1
        wi = vertice_futuru
        traceback = []
        drone_load = inicial_drone_load
        traceback.append(wi)
        while wi != vertice_inicial:
            traceback.append(dit_v_at[wi]["pi"])
            wi = dit_v_at[wi]["pi"]
        traceback.reverse()
        print("antes tracaback = {}". format(traceback))
        for v in traceback:
            if v != traceback[0]:
                drone_load -= 1
            if v in load_places:
                drone_load = max_drone_load
            if drone_load < 0:
                print("dorne_load < 0 tracaback = {}".format(traceback))
                return False
        print(" retornou True tracaback = {}".format(traceback))
        return True

    def recargas(self, vertice_futuru, vertice_inicial, dit_v_at, load_places, max_drone_load, inicial_drone_load, vertice_atual):
        dit_v_at__ = deepcopy(dit_v_at)
        wi = vertice_atual
        traceback = []
        # traceback.append(vertice_futuru)
        traceback.append(wi)
        while wi != vertice_inicial:
            traceback.append(dit_v_at__[wi]["pi"])
            wi = dit_v_at__[wi]["pi"]
        traceback.reverse()
        drone_load = 0
        for v in traceback:
            if drone_load > max_drone_load:
                drone_load = max_drone_load
            if v == vertice_inicial:
                drone_load = inicial_drone_load
            if v in load_places:
                drone_load = max_drone_load
            if v != vertice_inicial and v not in load_places:
                drone_load -= 1
            if drone_load < 0:
                break
        print("actual traceback = {}".format(traceback))
        print("drone_load = {}".format(drone_load))
        # if drone_load < 0:
        #     for i in range(20):
        #         print("doesn't works")
        return drone_load


    def Dijkstra_with_drone(self, vertice_inicial, vertice_final, inicial_drone_load=3, max_drone_load=5, load_places=[]):
        # setUp, levando em consideração o segundo passo
        dit_v_at = {}  # dicionario dos vertices
        for v in self.N:
            dit_v_at[v] = {}
            dit_v_at[v]["beta"] = inf
            dit_v_at[v]["fi"] = 0
            dit_v_at[v]["pi"] = "-"
        matrix_at = self.define_matrix()  # definindo matrix sem lacos e sem paralelas
        # setUp, levando em consideração o segundo passo
        # primeiro passo
        dit_v_at[vertice_inicial]["beta"] = 0
        dit_v_at[vertice_inicial]["fi"] = 1
        # primeiro passo
        w = vertice_inicial
        lis = []
        b_lis = []
        b_lis1 = []
        lis_n_tem_carga_o_bastante = []
        while True:
            # tracaback and return smallest path
            if w == vertice_final:
                traceback = []
                wi = w
                traceback.append(wi)
                while wi != vertice_inicial:
                    traceback.append(dit_v_at[wi]["pi"])
                    wi = dit_v_at[wi]["pi"]
                traceback.reverse()
                for v in traceback:
                    print("\nv = {}: \nbeta = {}, \nfi={}\n".format(v, dit_v_at[v]["beta"], dit_v_at[v]["fi"]))
                return traceback
            # tracaback and return smallest path
            for r in self.vertices_seguintes_possiveis(w, matrix_at):
                if dit_v_at[r]["fi"] == 0 and dit_v_at[r]["beta"] > dit_v_at[w]["beta"] + 1:
                    if r not in lis_n_tem_carga_o_bastante:
                        dit_v_at[r]["beta"] = dit_v_at[w]["beta"] + 1
                        dit_v_at[r]["pi"] = w
                    else:
                        dit_v_at[r]["beta"] = inf
                        dit_v_at[r]["pi"] = '-'

            r_existe = False
            # pegando todos os betas com fi == 0
            b_lis.clear()
            b_lis1.clear()
            for v in self.N:
                b_lis1.append(dit_v_at[v]["beta"])
                if dit_v_at[v]["fi"] == 0:
                    if v not in lis_n_tem_carga_o_bastante:  # para garantir que o drone não tente ir para locais onde a carga nao vai ser o bastante
                        b_lis.append(dit_v_at[v]["beta"])
            # pegando todos os betas com fi == 0
            print(b_lis)
            lis.clear()
            for p in range(len(b_lis1)):
                if p == len(b_lis1) - 1:
                    lis.append("{}: {}".format(self.N[p], b_lis1[p]))
                else:
                    lis.append("{}: {}, ".format(self.N[p], b_lis1[p]))
            print(lis)
            for r_ in self.N:
                # try:
                future_load = self.recargas(vertice_futuru=r_, vertice_inicial=vertice_inicial, dit_v_at=dit_v_at,
                                            max_drone_load=max_drone_load, load_places=load_places,
                                            inicial_drone_load=inicial_drone_load, vertice_atual=w)
                # future_load = inf
                if dit_v_at[r_]["fi"] == 0 and dit_v_at[r_]["beta"] < inf and dit_v_at[r_]["beta"] == min(b_lis):
                    # if r_existe is False:
                    #     r_existe = True
                    if future_load >= 1 or future_load == 0 and r_ == vertice_final:  # se apos a simulação de viajem vai ter energia
                        r_existe = True
                        dit_v_at[r_]["fi"] = 1
                        w = r_
                        break
                    else:
                        r_existe = True
                        w = dit_v_at[w]["pi"]
                        lis_n_tem_carga_o_bastante.append(r_)
                        break

            if r_existe is False:
                # print("W = {}".format(w))
                return "Não existe caminho entre os vertices"

    def define_dit_arestas(self):
        E = deepcopy(self.M)
        dit_arestas = {}
        for l in range(len(self.N)):
            for c in range(len(self.N)):
                elm = E[l][c]
                if elm > 1:  # remove paralelas
                    E[l][c] = 1
                if l == c:  # remove lacos
                    E[l][c] = 0
        for l in range(len(E)):
            dit_arestas[self.N[l]] = {}
            for c in range(len(E)):
                if E[l][c] == 1:
                    dit_arestas[self.N[l]][self.N[c]] = 1
                else:
                    dit_arestas[self.N[l]][self.N[c]] = 0
        return dit_arestas

    def Dijkstra_indian(self, vertice_inicial, vertice_final):
        map_heap = {}
        v_dist = {}
        v_parent = {}
        dit_arestas = self.define_dit_arestas()
        for v in self.N:
            map_heap[v] = inf
        v_parent[vertice_inicial] = None
        map_heap[vertice_inicial] = 0
        # setando todos os predecessores e os pesos de cada vertice em relassao ao vertice_inicial
        while True:
            vertice_atual = None

            # procurando vertice com menor beta para determinar o vertice_atual
            if len(map_heap) > 0:
                menor_beta = min(map_heap.values())
                for v in map_heap.keys():
                    if map_heap[v] == menor_beta:
                        vertice_atual = v
                        v_dist[vertice_atual] = map_heap[vertice_atual]  # adicionando o vertice_atual no v_dist com seu  repectivo peso
                        map_heap.pop(vertice_atual)  # retirando o vertice atual dos vertices a serem analisados
                        break

            # determinando os vartices_de_analise visinhos ao vertice atual
            if vertice_atual is not None:
                vertices_de_analise = []
                for v in map_heap.keys():
                    if dit_arestas[vertice_atual][v]:  # se a aresta realmente existe
                        vertices_de_analise.append(v)

                for v in vertices_de_analise:
                    if v_dist[vertice_atual] + 1 < map_heap[v]:  # se encontra um peso menor do que o atual para aquele vertice em analise
                        map_heap[v] = v_dist[vertice_atual] + 1
                        v_parent[v] = vertice_atual

            else:
                break

        # print("map_heap = {}".format(map_heap))
        # print("v_dist = {}".format(v_dist))
        # print("v_parent = {}".format(v_parent))
        # retornar o menor caminho se ele exixtir
        traceback = []
        wi = vertice_final
        while wi is not None:
            traceback.append(wi)
            try:
                wi = v_parent[wi]
            except:
                return False
        traceback.reverse()
        return traceback

    def print_das_estruturas(self, map_heap, v_dist, v_parent):
        print("\n  | v_parent | v_dist | map_heap |")
        for v in self.N:
            a = ""
            b = ""
            c = ""
            try:
                c = map_heap[v]
            except:
                pass
            try:
                a = v_parent[v]
            except:
                pass
            try:
                b = v_dist[v]
            except:
                pass
            print("{} |    {}    |   {}   |    {}    |".format(v, a, b, c))
        print("\n")

    def Min2(self, map_heap, recharge_points, drone_load):
        # tem_vertice_de_recarga = False
        # for k in map_heap.keys():
        #     if map_heap[k] != inf and k in recharge_points:
        #         tem_vertice_de_recarga = True
        #         break
        # if drone_load == 0 and tem_vertice_de_recarga:
        #     vertice_desejado = None
        #     Min = inf
        #     for k in map_heap.keys():
        #         if map_heap[k] < Min and k in recharge_points:
        #             Min = map_heap[k]
        #             vertice_desejado = k
        #     return [vertice_desejado, True, Min]
        # else:
        #     vertice_desejado = None
        #     Min = inf
        #     for k in map_heap.keys():
        #         if map_heap[k] < Min:
        #             Min = map_heap[k]
        #             vertice_desejado = k
        #     return [vertice_desejado, False, Min]

        vertice_desejado = None
        Min = inf
        for k in map_heap.keys():
            if map_heap[k] < Min:
                Min = map_heap[k]
                vertice_desejado = k
        return [vertice_desejado, False]



    def Dijkstra_indian_with_drone_2(self, vertice_inicial, vertice_final, recharge_points, initial_charge, recharge_value):
        map_heap = {}
        v_dist = {}
        v_parent = {}
        dit_arestas = self.define_dit_arestas()
        for v in self.N:
            map_heap[v] = inf
        v_parent[vertice_inicial] = None
        map_heap[vertice_inicial] = 0
        pseudo_vertice_atual = vertice_inicial
        drone_load = initial_charge
        # setando todos os predecessores e os pesos de cada vertice em relassao ao vertice_inicial
        while True:
            vertice_atual = None
            # print("vertice_atual = {}".format(pseudo_vertice_atual))
            # self.print_das_estruturas(map_heap, v_dist, v_parent)
            # procurando vertice com menor beta para determinar o vertice_atual
            if len(map_heap) > 0:
                menor_beta = self.Min2(map_heap, recharge_points, drone_load)
                # print("menor_beta = {}".format(menor_beta))
                # if menor_beta[1] is True:
                #     print("limpando os bagui com peso = {}, que não são pontos de recarga".format(menor_beta[-1]))
                #     keys = list(map_heap.keys())
                #     for ex in keys:
                #         if map_heap[ex] != inf:
                #             print("vertice {} com peso {}".format(ex, map_heap[ex]))
                #             if map_heap[ex] == menor_beta[-1] and ex != menor_beta[0]:
                #                 print("este foi removido")
                #                 v_dist[ex] = map_heap[ex]  # adicionando o vertice_atual no v_dist com seu  repectivo peso
                #                 map_heap.pop(ex)  # retirando o vertice atual dos vertices a serem analisados
                #             else:
                #                 print("este não foi removido")
                for v in map_heap.keys():
                    if v == menor_beta[0]:
                        vertice_atual = v
                        v_dist[vertice_atual] = map_heap[vertice_atual]  # adicionando o vertice_atual no v_dist com seu  repectivo peso
                        map_heap.pop(vertice_atual)  # retirando o vertice atual dos vertices a serem analisados
                        break

            # determinando os vartices_de_analise visinhos ao vertice atual
            if vertice_atual is not None:
                pseudo_vertice_atual = vertice_atual
                # print("Drone_load = {}".format(self.carga_atual(vertice_atual, vertice_inicial, recharge_points,
                #                                                 initial_charge, recharge_value, v_parent)))
                vertices_de_analise = []
                for v in map_heap.keys():
                    if dit_arestas[vertice_atual][v]:  # se a aresta realmente existe
                        future_drone_load = self.carga_atual(vertice_atual=pseudo_vertice_atual,
                                                              recharge_points=recharge_points,
                                                              initial_charge=initial_charge,
                                                              recharge_value=recharge_value, v_parent=v_parent, next=v)
                        # print("DRONE LOAD = {} SE TENTAR IR PELO VERTICE {}".format(future_drone_load, v))
                        if future_drone_load >= 1 or (future_drone_load == 0 and v == vertice_final):
                            # print("CONSIDEROU QUE PODIA")
                            vertices_de_analise.append(v)
                        # else:
                            # print("NÃO CONSIDEROU QUE PODIA")

                drone_load = self.carga_atual(vertice_atual=pseudo_vertice_atual, recharge_points=recharge_points,
                                              initial_charge=initial_charge, recharge_value=recharge_value,
                                              v_parent=v_parent)
                # print("ETAPA DE CALCULO DE PESO DOS OUTROS VERTICES COM VERTICE_ATUAL = {}, e DRONE_LOAD = {}".format(vertice_atual, drone_load))
                for v in vertices_de_analise:
                    if v_dist[vertice_atual] + 1 < map_heap[v]:  # se encontra um peso menor do que o atual para aquele vertice em analise
                        map_heap[v] = v_dist[vertice_atual] + 1
                        v_parent[v] = vertice_atual


            else:
                break

        # print("map_heap = {}".format(map_heap))
        # print("v_dist = {}".format(v_dist))
        # print("v_parent = {}".format(v_parent))
        # retornar o menor caminho se ele exixtir
        traceback = []
        wi = vertice_final
        while wi is not None:
            traceback.append(wi)
            try:
                wi = v_parent[wi]
            except:
                return  False
        traceback.reverse()
        return traceback

    def carga_atual(self, vertice_atual, recharge_points, initial_charge, recharge_value, v_parent, next=None):
        v_parent = deepcopy(v_parent)
        wi = vertice_atual
        traceback = []
        if next is not None:
            traceback.append(next)
        while wi is not None:
            traceback.append(wi)
            wi = v_parent[wi]
        traceback.reverse()
        drone_load = initial_charge
        for v in traceback[1:]:
            drone_load -= 1
            if drone_load < 0:
                break
            if v in recharge_points:
                if drone_load < recharge_value:
                    drone_load = recharge_value
        # print("vertice_atual = {}".format(vertice_atual))
        # print("1. actual traceback = {}".format(traceback))
        # print("2. drone_load = {}".format(drone_load))
        return drone_load

    def recargas_indian(self, vertice_atual, vertice_inicial, recharge_points, initial_charge, recharge_value, v_parent, vertice_futuru):
        v_parent = deepcopy(v_parent)
        wi = vertice_atual
        traceback = []
        traceback.append(vertice_atual)
        traceback.append(vertice_futuru)
        while wi is not None:
            traceback.append(wi)
            wi = v_parent[wi]
        traceback.reverse()
        drone_load = 0
        for v in traceback:
            if drone_load > recharge_value:
                drone_load = recharge_value
            if v == vertice_inicial:
                drone_load = initial_charge
            if v in recharge_points:
                drone_load = recharge_value
            if v != vertice_inicial and v not in recharge_points:
                drone_load -= 1
            if drone_load < 0:
                break
        print("vertice_atual = {}".format(vertice_atual))
        print("1. actual traceback = {}".format(traceback))
        print("2. drone_load = {}".format(drone_load))
        return drone_load

    def Min(self, map_heap, recharge_points, vertice_final, vertice_atual, vertice_inicial, initial_charge, v_parent, recharge_value):
        # less = False
        # vr = None
        # for v in map_heap.keys():
        #     if v in recharge_points:
        #         if less is False:
        #             if map_heap[v] != inf:
        #                 less = map_heap[v]
        #                 vr = v
        #         else:
        #             if map_heap[v] < less:
        #                 less = map_heap[v]
        #                 vr = v
        #
        # if vr is None:
        #     vr = list(map_heap.keys())[0]
        #     less = map_heap[vr]
        #     for v in map_heap.keys():
        #         if map_heap[v] < less:
        #             less = map_heap[v]
        #             vr = v
        #
        # return vr
        map_heap = deepcopy(map_heap)
        if vertice_atual is None:
            vertice_atual = vertice_inicial
        while True:
            less = min(map_heap.values())
            for v in map_heap.keys():
                if map_heap[v] == less:
                    if self.recargas_indian(vertice_atual=vertice_atual, vertice_inicial=vertice_inicial,
                                            recharge_points=recharge_points, initial_charge=initial_charge,
                                            recharge_value=recharge_value, v_parent=v_parent, vertice_futuru=v) >= 1:
                        return v
                    elif self.recargas_indian(vertice_atual=vertice_atual, vertice_inicial=vertice_inicial,
                                            recharge_points=recharge_points, initial_charge=initial_charge,
                                            recharge_value=recharge_value, v_parent=v_parent, vertice_futuru=v) == 0 and \
                                            v in recharge_points or v == vertice_final:
                        return v
                    else:
                        map_heap.pop(v)
                        break

    def Dijkstra_indian_drone(self, vertice_inicial, vertice_final, recharge_points, initial_charge, recharge_value):
        map_heap = {}
        v_dist = {}
        v_parent = {}
        dit_arestas = self.define_dit_arestas()
        for v in self.N:
            map_heap[v] = inf
        v_parent[vertice_inicial] = None
        map_heap[vertice_inicial] = 0
        # setando todos os predecessores e os pesos de cada vertice em relassao ao vertice_inicial
        while True:
            vertice_atual = None

            # procurando vertice com menor beta para determinar o vertice_atual
            if len(map_heap) > 0:
                menor_beta = self.Min(map_heap=map_heap,recharge_points=recharge_points,vertice_final=vertice_final,
                                      vertice_atual=vertice_atual, vertice_inicial=vertice_inicial,
                                      initial_charge=initial_charge, v_parent=v_parent, recharge_value=recharge_value)
                for v in map_heap.keys():
                    if map_heap[v] == menor_beta:
                        vertice_atual = v
                        v_dist[vertice_atual] = map_heap[
                            vertice_atual]  # adicionando o vertice_atual no v_dist com seu  repectivo peso
                        map_heap.pop(vertice_atual)  # retirando o vertice atual dos vertices a serem analisados
                        break

            # determinando os vartices_de_analise visinhos ao vertice atual
            if vertice_atual is not None:
                vertices_de_analise = []
                for v in map_heap.keys():
                    if dit_arestas[vertice_atual][v]:  # se a aresta realmente existe
                        vertices_de_analise.append(v)

                for v in vertices_de_analise:
                    if v_dist[vertice_atual] + 1 < map_heap[
                        v]:  # se encontra um peso menor do que o atual para aquele vertice em analise
                        map_heap[v] = v_dist[vertice_atual] + 1
                        v_parent[v] = vertice_atual

            else:
                break

        print("map_heap = {}".format(map_heap))
        print("v_dist = {}".format(v_dist))
        print("v_parent = {}".format(v_parent))
        # retornar o menor caminho se ele exixtir
        traceback = []
        wi = vertice_final
        while wi is not None:
            traceback.append(wi)
            wi = v_parent[wi]
        traceback.reverse()
        return traceback

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
