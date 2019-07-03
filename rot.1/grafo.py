class VerticeInvalidoException(Exception):
    pass

class ArestaInvalidaException(Exception):
    pass

class Grafo:

    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'

    def __init__(self, N=[], A={}):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param N: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma dicionário que guarda as arestas do grafo. A chave representa o nome da aresta e o valor é uma string que contém dois vértices separados por um traço.
        '''
        for v in N:
            if not(Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

        self.N = N

        for a in A:
            if not(self.arestaValida(A[a])):
                raise ArestaInvalidaException('A aresta ' + A[a] + ' é inválida')

        self.A = A

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

        # Verifica se as arestas antes de depois do elemento separador existem no Grafo
        if not(self.existeVertice(aresta[:i_traco])) or not(self.existeVertice(aresta[i_traco+1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def existeAresta(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, aresta):
            for k in self.A:
                if aresta == self.A[k]:
                    existe = True

        return existe

    def adicionaVertice(self, v):
        '''
        Adiciona um vértice no Grafo caso o vértice seja válido e não exista outro vértice com o mesmo nome
        :param v: O vértice a ser adicionado
        :raises: VerticeInvalidoException se o vértice passado como parâmetro não puder ser adicionado
        '''
        if self.verticeValido(v) and not self.existeVertice(v):
            self.N.append(v)
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, nome, a):
        '''
        Adiciona uma aresta no Grafo caso a aresta seja válida e não exista outra aresta com o mesmo nome
        :param v: A aresta a ser adicionada
        :raises: ArestaInvalidaException se a aresta passada como parâmetro não puder ser adicionada
        '''
        if self.arestaValida(a):
            self.A[nome] = a
        else:
            ArestaInvalidaException('A aresta ' + self.A[a] + ' é inválida')
			
    # FUNÇÕES IMPLEMENTADAS
    def vertices_nao_adjacentes(self):
        lis_pares_n_adjc = []
        lis_v = self.N
        lis_a = sorted(self.A)
        counter = 0
        for i in lis_v[:]:
            arestas_i = []
            for a in lis_a:
                ck = self.A[a]
                ck = ck.split(Grafo.SEPARADOR_ARESTA)
                if ck[0] == i or ck[1] == i:
                    arestas_i.append(a)
            for j in lis_v[counter:]:
                adjc = False
                for ar in arestas_i:
                    ck_1 = self.A[ar]
                    ck_1 = ck_1.split(Grafo.SEPARADOR_ARESTA)
                    if ck_1[0] == i and ck_1[1] == j or ck_1[0] == j and ck_1[1] == i:
                        adjc = True
                        break
                if adjc == False:
                    lis_pares_n_adjc.append("{}-{}".format(i, j))
            # counter += 1 isso previnia por exemplo J-E e E-P de ocorrer mas ai a resposta saia diferente da esperada
        return lis_pares_n_adjc

    def ha_laco(self):
        lis = sorted(self.A)
        for i in lis:
            check = self.A[i]
            check = check.split(Grafo.SEPARADOR_ARESTA)
            if check[0] == check[1]:
                return True
        return False

    def ha_paralelas(self):
        lis = sorted(self.A)
        counter = 0
        for i in lis[:-1]:
            counter += 1
            for j in lis[counter:]:
                ci = self.A[i]
                cj = self.A[j]
                ci = ci.split(Grafo.SEPARADOR_ARESTA)
                cj = cj.split(Grafo.SEPARADOR_ARESTA)
                if ci[0] == cj[0] and ci[1] == cj[1]:
                    return True
                elif ci[0] == cj[1] and ci[1] == cj[0]:
                    return True
        return False

    def grau(self, V):
        grau = 0
        lis_a = sorted(self.A)
        for a in lis_a:
            ck = self.A[a]
            if ck[0] == V or ck[2] == V:
                grau += 1
        return grau

    def arestas_sobre_vertice(self, V):
        lis_a = sorted(self.A)
        lis_r = []
        for a in lis_a:
            ck = self.A[a]
            ck = ck.split(Grafo.SEPARADOR_ARESTA)
            if ck[0] == V or ck[1] == V:
                lis_r.append(a)
        return lis_r

    def eh_completo(self):
        lis_v = self.N
        lis_a = sorted(self.A)
        counter = 0
        for i in lis_v[:-1]:
            arestas_i = []
            counter += 1  # isso previnia por exemplo J-E e E-P de ocorrer mas ai a resposta saia diferente da esperada
            for a in lis_a:
                ck = self.A[a]
                ck = ck.split(Grafo.SEPARADOR_ARESTA)
                if ck[0] == i or ck[1] == i:
                    arestas_i.append(a)
            for j in lis_v[counter:]:
                adjc = False
                for ar in arestas_i:
                    ck_1 = self.A[ar]
                    ck_1 = ck_1.split(Grafo.SEPARADOR_ARESTA)
                    if ck_1[0] == i and ck_1[1] == j or ck_1[0] == j and ck_1[1] == i:
                        adjc = True
                        break
                if adjc == False:
                    return False
        return True
    # FUNÇÕES IMPLEMENTADAS

    # DESAFIOS
    # h
    def comprimento_de_tamanho_n(self, lenght, counter=0, lis_path=[], v=None):
        if v == None:
            self.var_h = False
            # cria lis_v quando e a primeira chamada da func
            lis_v = self.N.copy()
            # limpando a lista retira os vertices com grau zero na primeira chamada da func
            for v1 in lis_v:
                if self.grau(v1) == 0:
                    lis_v.remove(v1)

            # percorre cada vertice possivel como comesso de caminho
            for v2 in lis_v:
                # inicializa listas que seram para o inicio do percursso
                lis_v_in = lis_v.copy()
                lis_path_in = []

                # chama a recursividade para o else
                lis_v_in.remove(v2)
                lis_path_in.append(v2)
                # print("v2 == {}".format(v2))
                # print("Vertice de chamada {}".format(v2))

                self.comprimento_de_tamanho_n(lenght=lenght, counter=0, lis_path=lis_path_in, v=v2)

        elif v != None:
            # print("chegou ao else")
            # print("lista_de vertices -> {}".format(lis_v))

            # condicionais de quebra de fluxo de recursao
            # se o tamanho foi atingindo seta a variavel de retorno em True
            if counter == lenght:
                # print("1 -- path_found -->> {}".format(lis_path))
                # print("2 -- in this case it does match the lenght")
                self.var_h = True

            # seta variaveis necessarias
            counter_in = counter
            lis_path_in = lis_path.copy()
            # cria a lista de arestas possiveis pelas quais viajar
            lis_a_in = []
            for a in sorted(self.A):
                str_ = self.A[a].split(self.SEPARADOR_ARESTA)
                if v in str_:
                    # nao permiti lasos
                    if str_[0] != str_[1]:
                        # nao permiti paralelas
                        paralela = False
                        for p in lis_a_in:
                            str_2 = self.A[p].split(self.SEPARADOR_ARESTA)
                            if (str_[0] == str_2[0] and str_[1] == str_2[1]) or (
                                    str_[0] == str_2[1] and str_[1] == str_2[0]):
                                paralela = True
                        if paralela == False:
                            lis_a_in.append(a)

            # pula(viaja) para cada aresta possivel
            for a1 in lis_a_in:
                str_1 = self.A[a1].split(self.SEPARADOR_ARESTA)
                str_1.remove(v)
                str_1 = str_1[0]

                # so viaja se nao pegar um caminho voltando para um vertice que ja foi viajado
                if str_1 not in lis_path:
                # caso seja valido ciclos comenta o if de cima e ativa o debaixo
                #if str_1 not in lis_path or str_1 == lis_path[0]:
                    # registra o caminho no path e chama a viagem
                    lis_path_in.append(a1)
                    lis_path_in.append(str_1)
                    counter_in += 1
                    self.comprimento_de_tamanho_n(lenght=lenght, counter=counter_in, lis_path=lis_path_in, v=str_1)

                    # reseta variaveis que precisam ser resetadas para novas tentativas
                    counter_in -= 1
                    lis_path_in.remove(a1)
                    lis_path_in.remove(str_1)

            # print("ou o for estava vasio ou simplesmente nao foi possivel acahar o caminho ou encontrou um vertice que nao se liga a nenhum outro")

        # utiliza variavel de retorno para resposta final
        return self.var_h

    #g
    def ha_ciclo(self, lis_path=[], v=None):
        if v == None:
            # seta algumas variaveis que sao utilizadas a penas na primeira sesao de chamada
            self.var_c = False
            # cria lis_v quando e a primeira chamada da func
            lis_v = self.N.copy()
            # limpando a lista retira os vertices com grau zero na primeira chamada da func
            for v1 in lis_v:
                if self.grau(v1) == 0:
                    lis_v.remove(v1)

            # percorre cada vertice possivel como comesso de caminho
            for v2 in lis_v:
                # inicializa listas que seram para o inicio do percursso
                lis_path_in = []

                # chama a recursividade para o else
                lis_path_in.append(v2)
                # print("v2 == {}".format(v2))
                # print("Vertice de chamada {}".format(v2))
                self.ha_ciclo(lis_path=lis_path_in.copy(), v=v2)
        elif v != None:
            # print("chegou ao else")
            # print("lista_de vertices -> {}".format(lis_v))

            # seta variaveis necessarias
            lis_path_in = lis_path.copy()
            # cria a lista de arestas possiveis pelas quais viajar
            lis_a_in = []
            for a in sorted(self.A):
                str_ = self.A[a].split(self.SEPARADOR_ARESTA)
                if v in str_:
                    lis_a_in.append(a)

            # condicionais de quebra de fluxo de recursao
            # se o tamanho foi atingindo seta a variavel de retorno em True
            #try:
            if lis_path_in[-1] == lis_path_in[0] and len(lis_path_in) > 1:
                #print("entrei no if de parada")
                #print("1 -- path_found -->> {}".format(lis_path))

                # garante que o ciclo que sera retornado sera o primeiro ciclo encontrado
                if (self.var_c == False):
                    self.lis_path_in = lis_path_in.copy()
                self.var_c = True

            #except IndexError:
            # pula(viaja) para cada aresta possivel
            for a1 in lis_a_in:
                str_1 = self.A[a1].split(self.SEPARADOR_ARESTA)
                str_1.remove(v)
                str_1 = str_1[0]

                # so viaja se nao pegar um caminho voltando para um vertice que ja foi viajado ou ja encontrou um ciclo
                if str_1 not in lis_path_in or str_1 == lis_path_in[0] and a1 not in lis_path_in:
                    #print("com o str-1 = {} consegui entrar no if".format(str_1))
                    #print("antes de add -- path_found -->> {}".format(lis_path_in))
                    # registra o caminho no path e chama a viagem
                    lis_path_in.append(a1)
                    lis_path_in.append(str_1)
                    self.ha_ciclo(lis_path=lis_path_in.copy(), v=str_1)
                    #print("depois de add -- path_found -->> {}".format(lis_path_in))
                    # reseta variaveis que precisam ser resetadas para novas tentativas
                    lis_path_in.remove(a1)
                    lis_path_in.remove(str_1)
                    #print("depois de remover -- path_found -->> {}".format(lis_path_in))

            # print("ou o for estava vasio ou simplesmente nao foi possivel acahar o caminho ou encontrou um vertice que nao se liga a nenhum outro")

        # utiliza variavel de retorno para resposta final
        if self.var_c == False:
            return False
        else:
            return self.lis_path_in

    #i
    def eh_conexo(self, v=None):
        # seta variaveis
        if v == None:
            self.lis_path = []
            self.lis_a_percoridas = []
            self.vertice = self.N[0]
            self.lis_path.append(self.vertice)
            self.eh_conexo(v=self.vertice)

        # percorre o grafo e armazena os vertices por quais passou de forma recursiva
        else:
            # conseguiu chegar neste vertice
            vertice_reccebido = v

            # seta a lista de arestas conectadas ao vertice atual
            lis_a = []
            for a in sorted(self.A):
                let = self.A[a].split(Grafo.SEPARADOR_ARESTA)
                #print("vertice_recebido = {}".format(vertice_reccebido))
                #print("let = {}".format(let))
                # na maioria das vezes e necessario para não percorrer arestas paralelas
                if vertice_reccebido in let:
                    let.remove(vertice_reccebido)
                    let = let[0]
                    # "and let != vertice_recebido" evita lassos
                    if a not in self.lis_a_percoridas and let != vertice_reccebido:
                        lis_a.append(a)
                        self.lis_a_percoridas.append(a)
            #print("\n\n\n")
            #print("self.lis_a_percorridas -->> {}".format(self.lis_a_percoridas))
            #print("lis_a -->> {}".format(lis_a))
            #print("\n\n\n")
            # chama a funcao de novo para cada vertice com tanto que nao leve a um vertice ja alcansado
            for a1 in lis_a:
                let1 = self.A[a1].split(Grafo.SEPARADOR_ARESTA)
                let1.remove(vertice_reccebido)
                let1 = let1[0]
                #print("let1 = {}".format(let1))
                # nao vai dar jump caso o vertice ja tenha sido percorrido
                # evita paralelas
                if let1 not in self.lis_path:
                    self.lis_path.append(let1)
                    self.eh_conexo(v=let1)

        # retorna
        if len(self.lis_path) == len(self.N):
            #print("final da funcao pelo True")
            #print("{} -->> self.N".format(self.N))
            #print("{} -->> self.lis_path".format(self.lis_path))
            return True
        else:
            #print("final da funcao pelo False")
            #print("{} -->> self.N".format(self.N))
            #print("{} -->> self.lis_path".format(self.lis_path))
            return False

    # DESAFIOS

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''
        grafo_str = ''

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca a vírgula se não for o último vértice
                grafo_str += ", "

        grafo_str += '\n'

        for i, a in enumerate(self.A):
            grafo_str += self.A[a]
            if not(i == len(self.A) - 1): # Só coloca a vírgula se não for a última aresta
                grafo_str += ", "

        return grafo_str































