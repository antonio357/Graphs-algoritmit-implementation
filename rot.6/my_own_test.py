from grafo_adj import Grafo

g_p = Grafo([], [])
for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
    g_p.adiciona_vertice(i)
for i in [['J-C', 3], ['C-E', 7], ['C-E', 2], ['C-P', 6], ['C-P', 2], ['C-M', 5], ['C-T', 9], ['M-T', 7], ['T-Z', 4]]:
    g_p.adiciona_aresta(i)

# Grafos completos
g_c = Grafo([], [])
for i in ['J', 'C', 'E', 'P']:
    g_c.adiciona_vertice(i)
for i in [['J-C', 5], ['J-E', 10], ['J-P', 8], ['C-J', 9], ['C-E', 7], ['C-P', 1], ['E-J', 7], ['E-C', 4],
          ['E-P', 6], ['P-J', 3], ['P-C', 9], ['P-E', 2]]:
    g_c.adiciona_aresta(i)

g_c3 = Grafo([], [])
g_c3.adiciona_vertice('J')

# Grafos com laco
g_l1 = Grafo([], [])
for i in ['A', 'B', 'C', 'D']:
    g_l1.adiciona_vertice(i)
for i in [['A-A', 7], ['B-A', 8], ['A-A', 10]]:
    g_l1.adiciona_aresta(i)

g_l4 = Grafo([], [])
g_l4.adiciona_vertice('D')
g_l4.adiciona_aresta(['D-D', 1])

g_l5 = Grafo([], [])
for i in ['C', 'D']:
    g_l5.adiciona_vertice(i)
for i in [['D-C', 5], ['C-C', 1]]:
    g_l5.adiciona_aresta(i)

g_challenger = Grafo([], [])
for i in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
          "U", "V", "X", "Y", "W", "Z", "1", "2", "3", "4", "5", "6", "7"]:
    g_challenger.adiciona_vertice(i)
for i in [['A-B', 5], ['A-C', 3], ['A-D', 10], ['B-H', 2], ['B-I', 8], ['C-F', 9], ['D-C', 3], ['D-E', 7],
          ['E-F', 1], ['E-L', 3], ['F-G', 3], ['F-J', 4], ['F-K', 5], ['G-B', 3], ['G-J', 6], ['H-G', 4],
          ['I-P', 8], ['J-I', 5], ['J-O', 6], ['K-N', 9], ['L-M', 4], ['M-Q', 8], ['N-R', 7], ['O-5', 7], ['O-R', 6],
          ['O-Q', 9], ['P-R', 10], ['P-T', 2], ['Q-R', 9], ['R-5', 6],['R-Y', 10],['T-U', 6], ['U-7', 8], ['U-W', 10],
          ['V-2', 5], ['V-W', 8], ['V-X', 1], ['X-R', 6], ['Y-Z', 1], ['Y-1', 2], ['1-3', 1], ['1-X', 9], ['3-4', 3],
          ['3-S', 4], ['5-T', 3], ['5-V', 6], ['6-3', 8], ['7-6', 9]]:
    g_challenger.adiciona_aresta(i)

print(g_p.Prim_indian())
print(g_c.Prim_indian())
print(g_l1.Prim_indian())
print(g_l4.Prim_indian())
print(g_l5.Prim_indian())
print(g_challenger.Prim_indian())