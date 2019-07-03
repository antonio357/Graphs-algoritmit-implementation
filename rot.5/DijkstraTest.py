import unittest
from grafo_adj import *


class TestGrafo(unittest.TestCase):

    def setUp(self):
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
        for i in ['J-C', 'J-E', 'J-P', 'C-J', 'C-E', 'C-P', 'E-J', 'E-C', 'E-P', 'P-J', 'P-C', 'P-E']:
            self.g_c.adiciona_aresta(i)

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

        self.g_challenger = Grafo([], [])
        for i in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "X", "Y", "W", "Z", "1", "2", "3", "4", "5", "6", "7"]:
            self.g_challenger.adiciona_vertice(i)
        for i in ['A-B', 'A-C', 'A-D', 'B-H', 'B-I', 'C-F', 'D-C', 'D-E', 'E-F', 'E-L', 'F-G', 'F-J', 'F-K', 'G-B',
                  'G-J', 'H-G',
                  'I-P', 'J-I', 'J-O', 'K-N', 'L-M', 'M-Q', 'N-R', 'O-5', 'O-R', 'O-Q', 'P-R', 'P-T', 'Q-R', 'R-5',
                  'R-Y',
                  'T-U', 'U-7', 'U-W', 'V-2', 'V-W', 'V-X', 'X-R', 'Y-Z', 'Y-1', '1-3', '1-X', '3-4', '3-S',
                  '5-T', '5-V', '6-3', '7-6']:
            self.g_challenger.adiciona_aresta(i)


    def test_Dijstra(self):
        self.assertEqual(self.g_p.Dijkstra_indian("J", "Z"), ['J', 'C', 'T', 'Z'])
        self.assertEqual(self.g_challenger.Dijkstra_indian("A", "S"), ['A', 'B', 'I', 'P', 'R', 'Y', '1', '3', 'S'])

    def test_Dijsktra_Drone(self):
        """ Estes são os 2  casos de teste proposto do roteiro {
        """
        self.assertEqual(
            self.g_challenger.Dijkstra_indian_with_drone_2(vertice_inicial="A", vertice_final="S", initial_charge=5,
                                                           recharge_value=5, recharge_points=["L", "R", "U", "6"]),
            ['A', 'B', 'I', 'P', 'R', 'Y', '1', '3', 'S'])
        self.assertEqual(
            self.g_challenger.Dijkstra_indian_with_drone_2(vertice_inicial="A", vertice_final="S", initial_charge=3,
                                                           recharge_value=5, recharge_points=["L", "R", "U", "6"]),
            ['A', 'D', 'E', 'L', 'M', 'Q', 'R', 'Y', '1', '3', 'S'])
        """
        }
        """
        self.assertEqual(self.g_challenger.Dijkstra_indian_with_drone_2(vertice_inicial="A", vertice_final="S", initial_charge=3,
                                                  recharge_value=3, recharge_points=["L", "R", "U", "6"]),
                         ['A', 'D', 'E', 'L', 'M', 'Q', 'R', '5', 'T', 'U', '7', '6', '3', 'S'])
        self.assertFalse(
            self.g_challenger.Dijkstra_indian_with_drone_2(vertice_inicial="A", vertice_final="S", initial_charge=3,
                                                           recharge_value=2, recharge_points=["L", "R", "U", "6"]))
        self.assertEqual(
            self.g_challenger.Dijkstra_indian_with_drone_2(vertice_inicial="A", vertice_final="S", initial_charge=3,
                                                           recharge_value=4, recharge_points=["L", "R", "U", "6"]),
            ['A', 'D', 'E', 'L', 'M', 'Q', 'R', 'Y', '1', '3', 'S'])
        self.assertFalse(
            self.g_challenger.Dijkstra_indian_with_drone_2(vertice_inicial="A", vertice_final="S", initial_charge=2,
                                                           recharge_value=3, recharge_points=["L", "R", "U", "6"]))
        self.assertEqual(
            self.g_challenger.Dijkstra_indian_with_drone_2(vertice_inicial="A", vertice_final="S", initial_charge=4,
                                                           recharge_value=4, recharge_points=["L", "R", "U", "6"]),
            ['A', 'B', 'I', 'P', 'R', 'Y', '1', '3', 'S'])
        self.assertFalse(
            self.g_challenger.Dijkstra_indian_with_drone_2(vertice_inicial="A", vertice_final="S", initial_charge=0,
                                                           recharge_value=3, recharge_points=["L", "R", "U", "6"]))
        self.assertFalse(
            self.g_challenger.Dijkstra_indian_with_drone_2(vertice_inicial="A", vertice_final="S", initial_charge=3,
                                                           recharge_value=0, recharge_points=["L", "R", "U", "6"]))
        self.assertEqual(
            self.g_challenger.Dijkstra_indian_with_drone_2(vertice_inicial="A", vertice_final="S", initial_charge=8,
                                                           recharge_value=0, recharge_points=["L", "R", "U", "6"]),
            ['A', 'B', 'I', 'P', 'R', 'Y', '1', '3', 'S'])
        self.assertEqual(
            self.g_challenger.Dijkstra_indian_with_drone_2(vertice_inicial="A", vertice_final="S", initial_charge=4,
                                                           recharge_value=3, recharge_points=["L", "R", "U", "6"]),
            ['A', 'B', 'I', 'P', 'R', '5', 'T', 'U', '7', '6', '3', 'S'])
        self.assertEqual(
            self.g_challenger.Dijkstra_indian_with_drone_2(vertice_inicial="A", vertice_final="S", initial_charge=5,
                                                           recharge_value=2, recharge_points=["L", "R", "U", "6"]),
            ['A', 'B', 'I', 'P', 'T', 'U', '7', '6', '3', 'S'])
        self.assertFalse(
            self.g_challenger.Dijkstra_indian_with_drone_2(vertice_inicial="A", vertice_final="S", initial_charge=3,
                                                           recharge_value=3, recharge_points=["L", "R", "U"]))
        self.assertFalse(
            self.g_challenger.Dijkstra_indian_with_drone_2(vertice_inicial="A", vertice_final="R", initial_charge=2,
                                                           recharge_value=3, recharge_points=["L", "R", "U", "6"]))
        self.assertEqual(
            self.g_challenger.Dijkstra_indian_with_drone_2(vertice_inicial="A", vertice_final="R", initial_charge=3,
                                                           recharge_value=3, recharge_points=["L", "R", "U", "6"]),
                                                           ['A', 'D', 'E', 'L', 'M', 'Q', 'R'])
