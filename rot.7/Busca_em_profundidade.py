import unittest
from grafo_adj import *


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # exemplos
        self.exemplo1 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']:
            self.exemplo1.adiciona_vertice(i)
        for i in [['A-B', 1], ['A-C', 1], ['A-D', 1], ['B-K', 1], ['B-I', 1], ['B-J', 1], ['B-H', 1], ['B-C', 1],
                   ['K-I', 1], ['I-J', 1], ['H-G', 1], ['C-G', 1], ['C-F', 1], ['C-D', 1], ['C-E', 1], ['D-E', 1],
                  ['D-F', 1]]:
            self.exemplo1.adiciona_aresta(i)

        self.exemplo1_answer = Grafo([], [])
        for i in self.exemplo1.N:
            self.exemplo1_answer.adiciona_vertice(i)
        for i in [['A-B', 1], ['B-K', 1], ['K-I', 1], ['I-J', 1], ['B-H', 1], ['H-G', 1], ['C-G', 1], ['C-F', 1],
                  ['D-F', 1], ['D-E', 1]]:
            self.exemplo1_answer.adiciona_aresta(i)

        self.exemplo1D_answer = Grafo([], [])
        for i in self.exemplo1.N:
            self.exemplo1D_answer.adiciona_vertice(i)
        for i in [['A-B', 1], ['B-K', 1], ['K-I', 1], ['I-J', 1], ['B-H', 1], ['H-G', 1], ['B-C', 1], ['C-F', 1],
                  ['C-D', 1], ['D-E', 1]]:
            self.exemplo1D_answer.adiciona_aresta(i)

        self.exemplo2 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']:
            self.exemplo2.adiciona_vertice(i)
        for i in [['A-B', 1], ['A-C', 1], ['A-D', 1], ['C-E', 1], ['C-G', 1], ['C-G', 1], ['E-B', 1], ['E-F', 1],
                  ['F-C', 1], ['G-B', 1], ['G-D', 1], ['H-G', 1], ['H-J', 1], ['J-I', 1], ['I-H', 1], ['I-L', 1],
                  ['J-L', 1], ['M-J', 1], ['K-M', 1], ['K-L', 1], ['K-J', 1]]:
            self.exemplo2.adiciona_aresta(i)

        self.exemplo2_answer = Grafo([], [])
        for i in self.exemplo2.N:
            self.exemplo2_answer.adiciona_vertice(i)
        for i in [['A-B', 1], ['E-B', 1], ['C-E', 1], ['C-G', 1], ['G-D', 1], ['H-G', 1], ['H-J', 1], ['J-I', 1],
                  ['I-L', 1], ['K-L', 1], ['K-M', 1], ['F-C', 1]]:
            self.exemplo2_answer.adiciona_aresta(i)

        self.exemplo2D_answer = Grafo([], [])
        for i in self.exemplo2.N:
            self.exemplo2D_answer.adiciona_vertice(i)
        for i in [['A-B', 1], ['A-C', 1], ['C-E', 1], ['E-F', 1], ['C-G', 1], ['G-D', 1], ['H-J', 1], ['J-I', 1],
                  ['I-L', 1], ['K-M', 1]]:
            self.exemplo2D_answer.adiciona_aresta(i)

        # Grafos de teste
        self.t = Grafo([], [])
        for i in ['A', 'B', 'C', 'D']:
            self.t.adiciona_vertice(i)
        for i in [['A-B', 1], ['B-C', 1], ['C-D', 1], ['D-A', 1], ['A-C', 1], ['B-D', 1]]:
            self.t.adiciona_aresta(i)

        self.t_answer = Grafo([], [])
        for i in self.t.N:
            self.t_answer.adiciona_vertice(i)
        for i in [['A-B', 1], ['B-C', 1], ['C-D', 1]]:
            self.t_answer.adiciona_aresta(i)

        # Grafo da Paraíba
        self.g_p = Grafo([], [])
        for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
            self.g_p.adiciona_vertice(i)
        for i in [['J-C', 3], ['C-E', 7], ['C-E', 2], ['C-P', 6], ['C-P', 2], ['C-M', 5], ['C-T', 9], ['M-T', 7], ['T-Z', 4]]:
            self.g_p.adiciona_aresta(i)

        self.g_p_answer = Grafo([], [])
        for i in self.g_p.N:
            self.g_p_answer.adiciona_vertice(i)
        for i in [['J-C', 3], ['C-E', 7], ['C-P', 6], ['C-M', 5], ['M-T', 7], ['T-Z', 4]]:
            self.g_p_answer.adiciona_aresta(i)

        # Grafos completos
        self.g_c = Grafo([], [])
        for i in ['J', 'C', 'E', 'P']:
            self.g_c.adiciona_vertice(i)
        for i in [['J-C', 5], ['J-E', 10], ['J-P', 8], ['C-J', 9], ['C-E', 7], ['C-P', 1], ['E-J', 7], ['E-C', 4],
                  ['E-P', 6], ['P-J', 3], ['P-C', 9], ['P-E', 2]]:
            self.g_c.adiciona_aresta(i)

        self.g_c_answer = Grafo([], [])
        for i in self.g_c.N:
            self.g_c_answer.adiciona_vertice(i)
        for i in [['J-C', 5], ['C-E', 7], ['E-P', 6]]:
            self.g_c_answer.adiciona_aresta(i)

        self.g_c3 = Grafo([], [])
        self.g_c3.adiciona_vertice('J')

        self.g_c3_answer = Grafo([], [])
        for i in self.g_c3.N:
            self.g_c3_answer.adiciona_vertice(i)

        # Grafos com laco
        self.g_l1 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D']:
            self.g_l1.adiciona_vertice(i)
        for i in [['A-A', 7], ['B-A', 8], ['A-A', 10]]:
            self.g_l1.adiciona_aresta(i)

        self.g_l4 = Grafo([], [])
        self.g_l4.adiciona_vertice('D')
        self.g_l4.adiciona_aresta(['D-D', 1])

        self.g_l4_answer = Grafo([], [])
        for i in self.g_l4.N:
            self.g_l4_answer.adiciona_vertice(i)

        self.g_l5 = Grafo([], [])
        for i in ['C', 'D']:
            self.g_l5.adiciona_vertice(i)
        for i in [['D-C', 5], ['C-C', 1]]:
            self.g_l5.adiciona_aresta(i)

        self.g_l5_answer = Grafo([], [])
        for i in self.g_l5.N:
            self.g_l5_answer.adiciona_vertice(i)
        for i in [['D-C', 5]]:
            self.g_l5_answer.adiciona_aresta(i)

        self.g_l5D_answer = Grafo([], [])
        for i in self.g_l5.N:
            self.g_l5D_answer.adiciona_vertice(i)

    def test_busca_em_profundidadeNaoDirecionados(self):
        self.assertEqual(self.exemplo2.BuscaEmProfundidadeGrafos(), self.exemplo2_answer)
        self.assertEqual(self.exemplo1.BuscaEmProfundidadeGrafos(), self.exemplo1_answer)
        self.assertEqual(self.t.BuscaEmProfundidadeGrafos(), self.t_answer)
        self.assertEqual(self.g_p.BuscaEmProfundidadeGrafos(), self.g_p_answer)
        self.assertEqual(self.g_c.BuscaEmProfundidadeGrafos(), self.g_c_answer)
        self.assertEqual(self.g_c3.BuscaEmProfundidadeGrafos(), self.g_c3_answer)
        self.assertEqual(self.g_l1.BuscaEmProfundidadeGrafos(), "Não é conexo")
        self.assertEqual(self.g_l4.BuscaEmProfundidadeGrafos(), self.g_l4_answer)
        self.assertEqual(self.g_l5.BuscaEmProfundidadeGrafos(), self.g_l5_answer)


    def test_busca_em_profundidadeDirecionados(self):
        self.assertEqual(self.exemplo2.BuscaEmProfundidadeGrafos(True), self.exemplo2D_answer)
        self.assertEqual(self.exemplo1.BuscaEmProfundidadeGrafos(True), self.exemplo1D_answer)
        self.assertEqual(self.t.BuscaEmProfundidadeGrafos(True), self.t_answer)
        self.assertEqual(self.g_p.BuscaEmProfundidadeGrafos(True), self.g_p_answer)
        self.assertEqual(self.g_c.BuscaEmProfundidadeGrafos(True), self.g_c_answer)
        self.assertEqual(self.g_c3.BuscaEmProfundidadeGrafos(True), self.g_c3_answer)
        self.assertEqual(self.g_l4.BuscaEmProfundidadeGrafos(True), self.g_l4_answer)
        self.assertEqual(self.g_l5.BuscaEmProfundidadeGrafos(True), self.g_l5D_answer)
