import unittest
from grafo import Grafo

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T', 'a8':'M-T', 'a9':'T-Z'})

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {'a1': 'J-C', 'a3': 'C-E', 'a4': 'C-P', 'a6': 'C-M', 'a7': 'C-T', 'a8': 'M-T', 'a9': 'T-Z'})

        # Grafos completos
        self.g_c = Grafo(['J', 'C', 'E', 'P'], {'a1':'J-C', 'a3':'J-E', 'a4':'J-P', 'a6':'C-E', 'a7':'C-P', 'a8':'E-P'})
        self.g_c2 = Grafo(['J', 'C', 'E', 'P'], {'a1':'J-C', 'a3':'E-J', 'a4':'J-P', 'a6':'E-C', 'a7':'C-P', 'a8':'P-E'})
        self.g_c3 = Grafo(['J'])

        # Grafos com laco
        self.g_l1 = Grafo(['A', 'B', 'C', 'D'], {'a1':'A-A', 'a2':'B-A', 'a3':'A-A'})
        self.g_l2 = Grafo(['A', 'B', 'C', 'D'], {'a1':'A-B', 'a2':'B-B', 'a3':'B-A'})
        self.g_l3 = Grafo(['A', 'B', 'C', 'D'], {'a1':'C-A', 'a2':'C-C', 'a3':'D-D'})
        self.g_l4 = Grafo(['D'], {'a2':'D-D'})
        self.g_l5 = Grafo(['C', 'D'], {'a2':'D-C', 'a3':'C-C'})

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(), ['J-J', 'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-C', 'C-Z', 'E-J', 'E-E', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-J', 'P-E', 'P-P', 'P-M', 'P-T', 'P-Z', 'M-J', 'M-E', 'M-P', 'M-M', 'M-Z', 'T-J', 'T-E', 'T-P', 'T-T', 'Z-J', 'Z-C', 'Z-E', 'Z-P', 'Z-M', 'Z-Z'])

        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         ['J-J', 'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-C', 'C-Z', 'E-J', 'E-E', 'E-P', 'E-M', 'E-T',
                          'E-Z', 'P-J', 'P-E',
                          'P-P', 'P-M', 'P-T', 'P-Z', 'M-J', 'M-E', 'M-P', 'M-M', 'M-Z', 'T-J', 'T-E', 'T-P', 'T-T',
                          'Z-J', 'Z-C', 'Z-E',
                          'Z-P', 'Z-M', 'Z-Z'])

        self.assertEqual(self.g_c.vertices_nao_adjacentes(), ['J-J', 'C-C', 'E-E', 'P-P'])

        self.assertEqual(self.g_c2.vertices_nao_adjacentes(), ['J-J', 'C-C', 'E-E', 'P-P'])

        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), ['J-J'])

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta uma única vez por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 3)
        self.assertEqual(self.g_l2.grau('B'), 3)
        self.assertEqual(self.g_l4.grau('D'), 1)

    def test_arestas_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('J')), set(['a1']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('C')), set(['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('M')), set(['a6', 'a8']))

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertTrue((self.g_l4.eh_completo()))
        self.assertTrue((self.g_l5.eh_completo()))

    # DESAFIOS
    def test_comprimento_de_tamanho_n(self):
        self.assertTrue(self.g_p.comprimento_de_tamanho_n(1))
        self.assertTrue((self.g_p_sem_paralelas.comprimento_de_tamanho_n(2)))
        self.assertTrue((self.g_c.comprimento_de_tamanho_n(3)))
        self.assertFalse((self.g_c2.comprimento_de_tamanho_n(4)))
        self.assertFalse((self.g_c3.comprimento_de_tamanho_n(5)))
        self.assertFalse((self.g_l1.comprimento_de_tamanho_n(6)))
        self.assertFalse((self.g_l2.comprimento_de_tamanho_n(7)))
        self.assertFalse((self.g_l3.comprimento_de_tamanho_n(8)))
        self.assertFalse((self.g_l4.comprimento_de_tamanho_n(9)))
        self.assertFalse((self.g_l5.comprimento_de_tamanho_n(10)))

    def test_ha_ciclo(self):
        self.assertEqual(self.g_p.ha_ciclo(), ["C", "a2", "E", "a3", "C"])
        self.assertEqual(self.g_p_sem_paralelas.ha_ciclo(), ["C", "a6", "M", "a8", "T", "a7", "C"])
        self.assertEqual(self.g_c.ha_ciclo(), ["J", "a1", "C", "a6", "E", "a3", "J"])
        self.assertEqual(self.g_c2.ha_ciclo(), ["J", "a1", "C", "a6", "E", "a3", "J"])
        self.assertFalse(self.g_c3.ha_ciclo())
        self.assertEqual(self.g_l1.ha_ciclo(), ["A", "a1", "A"])
        self.assertEqual(self.g_l2.ha_ciclo(), ["A", "a1", "B", "a3", "A"])
        self.assertEqual(self.g_l3.ha_ciclo(), ["C", "a2", "C"])
        self.assertEqual(self.g_l4.ha_ciclo(), ["D", "a2", "D"])
        self.assertEqual(self.g_l5.ha_ciclo(), ["C", "a3", "C"])

    def test_eh_conexo(self):
        self.assertTrue(self.g_p.eh_conexo())
        self.assertTrue(self.g_p_sem_paralelas.eh_conexo())
        self.assertTrue(self.g_c.eh_conexo())
        self.assertTrue(self.g_c2.eh_conexo())
        self.assertTrue(self.g_c3.eh_conexo())
        self.assertFalse(self.g_l1.eh_conexo())
        self.assertFalse(self.g_l2.eh_conexo())
        self.assertFalse(self.g_l3.eh_conexo())
        self.assertTrue(self.g_l4.eh_conexo())
        self.assertTrue(self.g_l5.eh_conexo())
    # DESAFIOS

