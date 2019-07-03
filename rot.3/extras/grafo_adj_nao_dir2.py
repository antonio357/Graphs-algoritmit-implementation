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

    def eh_conexo(self):
        '''
        Método que analisa se o grafo é conexo.
        Um grafo é dito conexo (ou conectado) quando há uma caminho entre quaisquer 2 vértices.
        :return: Se é ou não conexo, True ou False.
        '''
        copy_tmp = []
        copy = []
        for i in range(len(self.M)):    # criando uma códia da matriz
            for j in range(len(self.M)):
                copy_tmp.append(self.M[i][j])
            copy.append(copy_tmp)
            copy_tmp = []

        for i in range(len(copy)):      # por se tratar de matrizes não direcionais é necessário preenher toda a  matriz
            for j in range(len(copy)):
                if i > j:
                    copy[i][j] = copy[j][i]

        for i in range(len(copy)):      # algorítimo de Warshall
            for j in range(len(copy)):
                if copy[j][i] >= 1:
                    for k in range(len(copy)):
                        copy[j][k] = max(copy[j][k], copy[i][k])

        for i in range(len(copy)):      # verificando se alguma ligação na matriz de alcançabilidade ficou se conexão.
            for j in range(len(copy)):
                if copy[i][j] == 0:
                    return False  # não é conexo

        return True  # é conexo

    def grau(self, vertice):
        '''
        Método que analisa a quantidade de arestas que circundam um determinado vértice de um grafo.
        :param vertice: vertice tipo String q pertence a um grafo.
        :return: Número do grau de um vértice.
        '''
        count = 0
        for i in range(len(self.N)):
            if self.N[i] == vertice:
                for j in range(len(self.N)):
                    if j != i:
                        if self.M[j][i] != '-':
                            count += self.M[j][i]
                        if self.M[i][j] != '-':
                            count += self.M[i][j]
                    else:
                        count += self.M[i][j]
                return count
        return 0

    def caminho_euleriano(self):
        '''
        Caminho cujo só existem vértices de grau par ou absolutamente dois vértices grau impar.
        :return: A condição True ou False se existir ou não um caminho euleriano.
        '''

        count = 0
        if self.eh_conexo():
            for i in self.N:   # analisando o grau de todos os vértices
                grau = self.grau(i)
                if grau % 2 != 0:
                    count += 1  # caso exista grau impar será incrementado o contador.
            if count == 0:  # se não existir vértice grau impar, ou seja, todos são grau par, o grafo tem caminho Euleriano
                return True
            if count == 2:  # existe absolutamente dois vértices com grau impar. Logo, o grafo tem caminho Euleriano.
                return True
        return False

    def caminho_euleriano_explicito(self):
        '''
        O caminho Euleriano passa por todas as arestas uma única vez, em todos os vétices.
        Se possuir os dois vértices de grau impar, um deverá dar início ao caminho, e o outro deverá ser o último.
        Se possuir apenas graus pares, o vértice que deu início ao caminho deverá se o último.
        :return: Uma string contendo o caminho euleriano.
        '''
        aresta_inicial = ""
        indice = 0  # valor padrão para quando NÃO tiver vértice com grau impar
        caminho = ""
        qtd_arestas = 0
        tem_impar = False

        if self.caminho_euleriano():  # verifica se o grafo tem caminho euleriano, método já implementado.
            for i in self.N:
                if self.grau(i) % 2 != 0:  # procurar os vértices de grau impar, para começar por um deles
                    if aresta_inicial == "":
                        aresta_inicial = i
                        indice = self.N.index(aresta_inicial)
                        tem_impar = True
                        break

            aresta_inicial = self.N[indice]  # caso não tenha vértice grau impar tem q setar a aresta inicial
            indice_linha_inicial = indice
            indice_coluna_inicial = -1

            # criando uma cópia para usar na comparação com inteiros, convertendo os '-' da matriz em '0', bem como contar quantas arestas possui.
            matriz_tmp = []
            matriz = []
            for i in range(len(self.M)):
                for j in range(len(self.M)):
                    matriz_tmp.append(self.M[i][j])
                matriz.append(matriz_tmp)
                matriz_tmp = []

            for i in range(len(matriz)):
                for j in range(len(matriz)):
                    if matriz[i][j] == '-':
                        matriz[i][j] = 0
                    if i == j:
                        matriz[i][j] = 0  # desprezando os laços!!!
                    qtd_arestas += matriz[i][j]

            vertice = ""  # variável para armazenar o próximo vértice do caminho

            while qtd_arestas > 0:  # quantidade de iteração será a quantidade de arestas no grafo

                for i in range(len(self.N)):  # iterar em cada coluna ou linha de acordo com o if abaixo.

                    # Essa comparação fixa a linha e itera a coluna analisando se exite aresta
                    if matriz[indice][i] > 0:

                        if indice_coluna_inicial < 0:  # como a princípio é -1 será setado apenas na primeira vez.
                            indice_coluna_inicial = i  # definindo o índice da coluna inicial

                        # essa comparação garante o retorno do caminho para o vértice inicial quando só tem vértice grau par no grafo.
                        if not tem_impar and indice == indice_linha_inicial and qtd_arestas > 1 and matriz[indice][i] == 1:
                            pass

                        else:
                            vertice = self.N[i]         # seta o vértice encontrado para o atual
                            matriz[indice][i] -= 1      # reduz a aresta na matriz
                            indice = i                  # atualiza o número do índice
                            qtd_arestas -= 1            # diminui a quantidade de arestas a serem percorridas
                            break

                    # caso chegue na última coluna e não encontre nenhuma aresta, ele entra nesse if para iterar a
                    # coluna buscando alguma aresta.
                    elif (matriz[indice][i] == 0) and (i == (len(self.N)) - 1):
                        for j in range(len(self.N)): # funciona da mesma maneira que a iteração por coluna
                            if matriz[j][indice] > 0:
                                if not tem_impar and indice == indice_coluna_inicial and qtd_arestas > 1 and matriz[j][indice] == 1:
                                    pass
                                else:
                                    vertice = self.N[j]
                                    matriz[j][indice] -= 1
                                    indice = j
                                    qtd_arestas -= 1
                                    break

                caminho += aresta_inicial + "-" + vertice + ", "    # escrevendo a string, com o caminho
                aresta_inicial = self.N[indice]                     # atualiza a aresta inicial do caminho

            return caminho[:-2]
        else:
            return False

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