import unittest
from grafo_adj_nao_dir import Grafo


class TestEuler(unittest.TestCase):

    def setUp(self):

        # Pontes de Konigsberg
        self.konigsberg = Grafo([], [])
        for i in ['M', 'T', 'B', 'R']:
            self.konigsberg.adiciona_vertice(i)
        for i in ['M-T', 'M-T', 'M-B', 'M-B', 'M-R', 'B-R', 'T-R']:
            self.konigsberg.adiciona_aresta(i)


        # Grafos com caminho euleriano
        self.konigsberg_mod = Grafo([], [])
        for i in ['M', 'T', 'B', 'R']:
            self.konigsberg_mod.adiciona_vertice(i)
        for i in ['M-T', 'M-T', 'M-B', 'M-B', 'M-R', 'M-R', 'B-R', 'T-R']:
            self.konigsberg_mod.adiciona_aresta(i)

        self.g_c_e = Grafo([], [])
        for i in ['A', 'B', 'C']:
            self.g_c_e.adiciona_vertice(i)
        for i in ['A-B', 'B-C']:
            self.g_c_e.adiciona_aresta(i)


        # Grafo da Paraíba
        self.g_p = Grafo([], [])
        for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
            self.g_p.adiciona_vertice(i)
        for i in ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
            self.g_p.adiciona_aresta(i)

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = Grafo([], [])
        for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
            self.g_p_sem_paralelas.adiciona_vertice(i)
        for i in ['J-C', 'C-E', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
            self.g_p_sem_paralelas.adiciona_aresta(i)

        # Grafos completos
        self.g_c = Grafo([], [])
        for i in ['J', 'C', 'E', 'P']:
            self.g_c.adiciona_vertice(i)
        for i in ['J-C', 'J-E', 'J-P', 'C-E', 'C-P', 'E-P']:
            self.g_c.adiciona_aresta(i)

        self.g_c2 = Grafo([], [])
        for i in ['J', 'C', 'E', 'P']:
            self.g_c2.adiciona_vertice(i)
        for i in ['J-C', 'E-J', 'J-P', 'E-C', 'C-P', 'P-E']:
            self.g_c2.adiciona_aresta(i)

        self.g_c3 = Grafo([], [])
        self.g_c3.adiciona_vertice('J')

        # Grafos com laco
        self.g_l1 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D']:
            self.g_l1.adiciona_vertice(i)
        for i in ['A-A', 'B-A', 'A-A']:
            self.g_l1.adiciona_aresta(i)

        self.g_l2 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D']:
            self.g_l2.adiciona_vertice(i)
        for i in ['A-B', 'B-B', 'B-A']:
            self.g_l2.adiciona_aresta(i)

        self.g_l3 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D']:
            self.g_l3.adiciona_vertice(i)
        for i in ['C-A', 'C-C', 'D-D']:
            self.g_l3.adiciona_aresta(i)

        self.g_l4 = Grafo([], [])
        self.g_l4.adiciona_vertice('D')
        self.g_l4.adiciona_aresta('D-D')

        self.g_l5 = Grafo([], [])
        for i in ['C', 'D']:
            self.g_l5.adiciona_vertice(i)
        for i in ['D-C', 'C-C']:
            self.g_l5.adiciona_aresta(i)

        self.judA = Grafo([], [])  # grafo com caminho euleriano, com vertices de grau ímpar no começo.
        for i in ['T', 'B', 'M', 'R']:
            self.judA.adiciona_vertice(i)
        for i in ['M-T', 'M-T', 'M-B', 'M-B', 'M-R', 'M-R', 'B-R', 'T-R']:
            self.judA.adiciona_aresta(i)

        self.judB = Grafo([], [])  # grafo com caminho euleriano, com vertices apenas de grau par.
        for i in ['T', 'B', 'M', 'R']:
            self.judB.adiciona_vertice(i)
        for i in ['M-T', 'M-T', 'M-B', 'M-B', 'M-R', 'M-R']:
            self.judB.adiciona_aresta(i)

    # def test_caminho_euleriano(self):
    #     self.assertTrue(self.konigsberg_mod.caminho_euleriano())
    #     self.assertTrue(self.g_c_e.caminho_euleriano())
    #     self.assertTrue(self.g_c_e.caminho_euleriano())
    #     self.assertFalse(self.konigsberg.caminho_euleriano())
    #     self.assertFalse(self.g_p.caminho_euleriano())
    #     self.assertFalse(self.g_p_sem_paralelas.caminho_euleriano())
    #     self.assertFalse(self.g_c.caminho_euleriano())

    # def test_caminho_euleriano_explicito(self):
    #     self.assertEquals(self.konigsberg_mod.caminho_euleriano_explicito(), "T-R, R-M, M-T, T-M, M-B, B-R, R-M, M-B")
    #     self.assertEquals(self.g_c_e.caminho_euleriano_explicito(), "A-B, B-C")
    #     self.assertEquals(self.judA.caminho_euleriano_explicito(), "T-M, M-R, R-T, T-M, M-R, R-B, B-M, M-B")
    #     self.assertEquals(self.judB.caminho_euleriano_explicito(), "T-M, M-R, R-M, M-B, B-M, M-T")
    #     self.assertFalse(self.g_l4.caminho_euleriano_explicito())
    #     self.assertFalse(self.g_p.caminho_euleriano_explicito())
    #     self.assertFalse(self.g_p_sem_paralelas.caminho_euleriano_explicito())
    #     self.assertFalse(self.g_l1.caminho_euleriano_explicito())
    #     self.assertFalse(self.g_l2.caminho_euleriano_explicito())
    #     self.assertFalse(self.g_l4.caminho_euleriano_explicito())

    def test_caminho_euleriano_path(self):
        self.assertEquals(self.konigsberg_mod.caminho_euleriano(), ['T', 'a7', 'R', 'a5', 'M', 'a1', 'T', 'a2', 'M', 'a3', 'B', 'a8', 'R', 'a6', 'M', 'a4', 'B'])
        # self.assertEquals(self.g_c_e.caminho_euleriano_path(), ['A', 'a1', 'B', 'a2', 'C'])
        # self.assertTrue(self.g_c_e.caminho_euleriano_path())

        self.assertFalse(self.konigsberg.caminho_euleriano_path())
        self.assertFalse(self.g_p.caminho_euleriano_path())
        self.assertFalse(self.g_p_sem_paralelas.caminho_euleriano_path())
        self.assertFalse(self.g_c.caminho_euleriano_path())