from grafo_adj import Grafo

# g = Grafo([], [])
# for i in ['C', 'D']:
#     g.adiciona_vertice(i)
# for i in ['D-C', 'C-C']:
#     g.adiciona_aresta(i)
#
# print("g")
# print(g)
# print("de {} ate {}".format("D","C"))
# print(g.Dijkstra(vertice_inicial="D", vertice_final="C"))
# print("de {} ate {}".format("C","D"))
# print(g.Dijkstra(vertice_inicial="C", vertice_final="D"))
# print()
#
# g_ = Grafo([], [])
# for i in ['A', 'B', 'C', 'D']:
#     g_.adiciona_vertice(i)
# for i in ['A-B', 'B-B', 'B-A']:
#     g_.adiciona_aresta(i)
#
# print("g_")
# print(g_)
# print("de {} ate {}".format("A","B"))
# print(g_.Dijkstra(vertice_inicial="A", vertice_final="B"))
# print("de {} ate {}".format("B","A"))
# print(g_.Dijkstra(vertice_inicial="B", vertice_final="A"))
# print()
#
# g_c = Grafo([], [])
# for i in ['J', 'C', 'E', 'P']:
#     g_c.adiciona_vertice(i)
# for i in ['J-C', 'J-E', 'J-P', 'C-J', 'C-E', 'C-P', 'E-J', 'E-C', 'E-P', 'P-J', 'P-C', 'P-E']:
#     g_c.adiciona_aresta(i)
#
# print("g_c")
# print(g_c)
# print("de {} ate {}".format("J","C"))
# print(g_c.Dijkstra(vertice_inicial="J", vertice_final="C"))
# print("de {} ate {}".format("J","E"))
# print(g_c.Dijkstra(vertice_inicial="J", vertice_final="E"))
# print("de {} ate {}".format("J","P"))
# print(g_c.Dijkstra(vertice_inicial="J", vertice_final="P"))
# print()
#
# g_p = Grafo([], [])
# for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
#     g_p.adiciona_vertice(i)
# for i in ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
#     g_p.adiciona_aresta(i)
#
# print("g_p")
# print(g_p)
# for vi in g_p.N:
#     for vf in g_p.N:
#         print("de {} ate {}".format(vi, vf))
#         print(g_p.Dijkstra(vertice_inicial=vi, vertice_final=vf))
# print()
#
# g_h = Grafo([], [])
# for i in ["A", "B", "C", "D", "E", "F", "G", "H"]:
#     g_h.adiciona_vertice(i)
# for i in ["A-B", "A-C", "B-D", "B-E", "D-F", "E-G", "E-F", "C-E", "C-G", "H-B", "H-D", "H-F"]:
#     g_h.adiciona_aresta(i)
#
# print("g_h")
# print(g_h)
# print("de {} ate {}".format("H", "G"))
# print(g_h.Dijkstra(vertice_inicial="H", vertice_final="G"))
#
# g_challenger = Grafo([], [])
# counter = 0
# for i in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "W", "Z", "1", "2", "3", "4", "5", "6", "7"]:
#     g_challenger.adiciona_vertice(i)
# for i in ['A-B', 'A-C', 'A-D', 'B-H', 'B-I', 'C-F', 'D-C', 'D-E', 'E-F', 'E-L', 'F-G', 'F-J', 'F-K', 'G-B', 'G-J', 'H-G',
#           'I-P', 'J-I', 'J-O', 'K-N', 'L-M', 'M-Q', 'N-R', 'O-5', 'O-R', 'O-Q', 'P-R', 'P-T', 'Q-R', 'R-5', 'R-Y',
#           'T-U', 'U-7', 'U-W', 'V-2', 'V-W', 'V-X', 'X-R', 'Y-Z', 'Y-1', '1-3', '1-X', '3-4', '3-S',
#           '5-T', '5-V', '6-3', '7-6']:
#     print("counter = {}".format(counter))
#     counter += 1
#     g_challenger.adiciona_aresta(i)
#
# print("g_challenger")
# print(g_challenger)
# print("de {} ate {}".format("A", "S"))
# print("{} --> actual".format(g_challenger.Dijkstra(vertice_inicial="A", vertice_final="S")))
# print("{} --> expected".format(["A", "B", "I", "P", "R", "Y", "1", "3", "S"]))

# g_challenger = Grafo([], [])
# for i in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "W", "Z", "1", "2", "3", "4", "5", "6", "7"]:
#     g_challenger.adiciona_vertice(i)
# for i in ['A-B', 'A-C', 'A-D', 'B-H', 'B-I', 'C-F', 'D-C', 'D-E', 'E-F', 'E-L', 'F-G', 'F-J', 'F-K', 'G-B', 'G-J', 'H-G',
#           'I-P', 'J-I', 'J-O', 'K-N', 'L-M', 'M-Q', 'N-R', 'O-5', 'O-R', 'O-Q', 'P-R', 'P-T', 'Q-R', 'R-5', 'R-Y',
#           'T-U', 'U-7', 'U-W', 'V-2', 'V-W', 'V-X', 'X-R', 'Y-Z', 'Y-1', '1-3', '1-X', '3-4', '3-S',
#           '5-T', '5-V', '6-3', '7-6']:
#     g_challenger.adiciona_aresta(i)
#
# print("g_challenger")
# print(g_challenger)
# print("de {} ate {}".format("A", "S"))
# print("{} --> actual".format(g_challenger.Dijkstra_with_drone(vertice_inicial="A", vertice_final="S", inicial_drone_load=5, max_drone_load=5, load_places=["L", "R", "U", "6"])))
# print("{} --> expected".format(["A", "B", "I", "P", "R", "Y", "1", "3", "S"]))

# indian_graph = Grafo([], [])
# for v in ["A", "B", "C", "D", "E", "F"]:
#     indian_graph.adiciona_vertice(v)
# for a in ["A-B", "A-D", "A-E", "B-C", "C-D", "E-F", "F-D"]:
#     indian_graph.adiciona_aresta(a)
#
# print("indian_graph")
# print(indian_graph)
# print("de {} ate {}".format("A", "D"))
# print(indian_graph.Dijkstra_with_drone_indian(vertice_inicial="A", vertice_final="F"))

g_challenger = Grafo([], [])
for i in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "W", "Z", "1", "2", "3", "4", "5", "6", "7"]:
    g_challenger.adiciona_vertice(i)
for i in ['A-B', 'A-C', 'A-D', 'B-H', 'B-I', 'C-F', 'D-C', 'D-E', 'E-F', 'E-L', 'F-G', 'F-J', 'F-K', 'G-B', 'G-J', 'H-G',
          'I-P', 'J-I', 'J-O', 'K-N', 'L-M', 'M-Q', 'N-R', 'O-5', 'O-R', 'O-Q', 'P-R', 'P-T', 'Q-R', 'R-5', 'R-Y',
          'T-U', 'U-7', 'U-W', 'V-2', 'V-W', 'V-X', 'X-R', 'Y-Z', 'Y-1', '1-3', '1-X', '3-4', '3-S',
          '5-T', '5-V', '6-3', '7-6']:
    g_challenger.adiciona_aresta(i)

print("g_challenger")
print(g_challenger)
print("de {} ate {}".format("A", "S"))
print("{} --> actual".format(g_challenger.Dijkstra_indian_with_drone_2(vertice_inicial="A", vertice_final="S", initial_charge=5,
                                                                recharge_value=2, recharge_points=["L", "R", "U", "6"])))
print("{} --> expected".format(["A", "B", "I", "P", "R", "Y", "1", "3", "S"]))