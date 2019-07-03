import unittest
from grafo_adj import Grafo
#from Roteiro2.grafo_adj_nao_dir import *
#from Roteiro2.grafo_adj_nao_dir2 import *


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = Grafo([], [])
        for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
            self.g_p.adicionaVertice(i)
        for i in ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
            self.g_p.adicionaAresta(i)

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = Grafo([], [])
        for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
            self.g_p_sem_paralelas.adicionaVertice(i)
        for i in ['J-C', 'C-E', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
            self.g_p_sem_paralelas.adicionaAresta(i)

        # Grafos completos
        self.g_c = Grafo([], [])
        for i in ['J', 'C', 'E', 'P']:
            self.g_c.adicionaVertice(i)
        for i in ['J-C', 'J-E', 'J-P', 'C-J', 'C-E', 'C-P', 'E-J', 'E-C', 'E-P', 'P-J', 'P-C', 'P-E']:
            self.g_c.adicionaAresta(i)


        self.g_c3 = Grafo([], [])
        self.g_c3.adicionaVertice('J')

        # Grafos com laco
        self.g_l1 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D']:
            self.g_l1.adicionaVertice(i)
        for i in ['A-A', 'B-A', 'A-A']:
            self.g_l1.adicionaAresta(i)

        self.g_l2 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D']:
            self.g_l2.adicionaVertice(i)
        for i in ['A-B', 'B-B', 'B-A']:
            self.g_l2.adicionaAresta(i)

        self.g_l3 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D']:
            self.g_l3.adicionaVertice(i)
        for i in ['C-A', 'C-C', 'D-D']:
            self.g_l3.adicionaAresta(i)

        self.g_l4 = Grafo([], [])
        self.g_l4.adicionaVertice('D')
        self.g_l4.adicionaAresta('D-D')

        self.g_l5 = Grafo([], [])
        for i in ['C', 'D']:
            self.g_l5.adicionaVertice(i)
        for i in ['D-C', 'C-C']:
            self.g_l5.adicionaAresta(i)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(set(self.g_p.vertices_nao_adjacentes()), set(['C-C', 'C-Z', 'E-E', 'E-M', 'E-P', 'E-T', 'E-Z',
                                                                       'J-E',
                                                                       'J-J', 'J-M', 'J-P', 'J-T', 'J-Z', 'M-M', 'M-Z',
                                                                       'P-M',
                                                                       'P-P', 'P-T', 'P-Z', 'T-T', 'Z-Z']))

        self.assertEqual(self.g_c.vertices_nao_adjacentes(), ['J-J', 'C-C', 'E-E', 'P-P'])

        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), ['J-J'])

    # def test_ha_laco(self):
    #     self.assertFalse(self.g_p.ha_laco_rot4())
    #     self.assertFalse(self.g_p_sem_paralelas.ha_laco_rot4())
    #     self.assertTrue(self.g_l1.ha_laco_rot4())
    #     self.assertTrue(self.g_l2.ha_laco_rot4())
    #     self.assertTrue(self.g_l3.ha_laco_rot4())
    #     self.assertTrue(self.g_l4.ha_laco_rot4())
    #     self.assertTrue(self.g_l5.ha_laco_rot4())
    #
    # def test_grau(self):
    #     # Paraíba
    #     self.assertEqual(self.grau_rot4('J'), 1)
    #     self.assertEqual(self.grau_rot4('C'), 7)
    #     self.assertEqual(self.grau_rot4('E'), 2)
    #     self.assertEqual(self.grau_rot4('P'), 2)
    #     self.assertEqual(self.grau_rot4('M'), 2)
    #     self.assertEqual(self.grau_rot4('T'), 3)
    #     self.assertEqual(self.grau_rot4('Z'), 1)
    #
    #     # Completos
    #     self.assertEqual(self.grau_rot4('J'), 6)
    #     self.assertEqual(self.grau_rot4('C'), 6)
    #     self.assertEqual(self.grau_rot4('E'), 6)
    #     self.assertEqual(self.grau_rot4('P'), 6)
    #
    #     # Com laço. Lembrando que cada laço conta uma única vez por vértice para cálculo do grau
    #     self.assertEqual(self.grau_rot4('A'), 3)
    #     self.assertEqual(self.grau_rot4('B'), 3)
    #     self.assertEqual(self.grau_rot4('D'), 1)
    #
    # def test_arestas_ha_paralelas(self):
    #     self.assertTrue(ha_paralelas(self.g_p))
    #     self.assertFalse(ha_paralelas(self.g_p_sem_paralelas))
    #     self.assertFalse(ha_paralelas(self.g_c))
    #     self.assertFalse(ha_paralelas(self.g_c3))
    #     self.assertTrue(ha_paralelas(self.g_l1))
    #
    # def test_arestas_sobre_vertice(self):
    #     self.assertEqual(arestas_sobre_vertice(self.g_p, 'J'), ['J-C'])
    #     self.assertEqual(arestas_sobre_vertice(self.g_p, 'C'), ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T'])
    #     self.assertEqual(arestas_sobre_vertice(self.g_p, 'M'), ['C-M', 'M-T'])
    #
    # def test_eh_completo(self):
    #     self.assertFalse(eh_completo(self.g_p))
    #     self.assertFalse(eh_completo(self.g_p_sem_paralelas))
    #     self.assertTrue(eh_completo(self.g_c))
    #     self.assertTrue(eh_completo(self.g_c3))
    #     self.assertFalse(eh_completo(self.g_l1))
    #     self.assertFalse(eh_completo(self.g_l2))
    #     self.assertFalse(eh_completo(self.g_l3))
    #     self.assertTrue(eh_completo(self.g_l4))
    #     self.assertFalse(eh_completo(self.g_l5))