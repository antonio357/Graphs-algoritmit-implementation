from grafo_adj import *

# Grafo da Paraíba
g_p = Grafo([], [])
for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
    g_p.adiciona_vertice(i)
for i in ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
    g_p.adiciona_aresta(i)

# Grafo da Paraíba sem arestas paralelas
g_p_sem_paralelas = Grafo([], [])
for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
    g_p_sem_paralelas.adiciona_vertice(i)
for i in ['J-C', 'C-E', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
    g_p_sem_paralelas.adiciona_aresta(i)

# Grafos completos
g_c = Grafo([], [])
for i in ['J', 'C', 'E', 'P']:
    g_c.adiciona_vertice(i)
for i in ['J-C', 'J-E', 'J-P', 'C-J', 'C-E', 'C-P', 'E-J', 'E-C', 'E-P', 'P-J', 'P-C', 'P-E']:
    g_c.adiciona_aresta(i)

g_c3 = Grafo([], [])
g_c3.adiciona_vertice('J')

# Grafos com laco
g_l1 = Grafo([], [])
for i in ['A', 'B', 'C', 'D']:
    g_l1.adiciona_vertice(i)
for i in ['A-A', 'B-A', 'A-A']:
    g_l1.adiciona_aresta(i)

g_l2 = Grafo([], [])
for i in ['A', 'B', 'C', 'D']:
    g_l2.adiciona_vertice(i)
for i in ['A-B', 'B-B', 'B-A']:
    g_l2.adiciona_aresta(i)

g_l3 = Grafo([], [])
for i in ['A', 'B', 'C', 'D']:
    g_l3.adiciona_vertice(i)
for i in ['C-A', 'C-C', 'D-D']:
    g_l3.adiciona_aresta(i)

g_l4 = Grafo([], [])
g_l4.adiciona_vertice('D')
g_l4.adiciona_aresta('D-D')

g_l5 = Grafo([], [])
for i in ['C', 'D']:
    g_l5.adiciona_vertice(i)
for i in ['D-C', 'C-C']:
    g_l5.adiciona_aresta(i)

# TESTES
print("g_p")
print(g_p.warshall())
print(g_p)

# print("g_p_sem_paralelas")
# print(g_p_sem_paralelas.warshall())
# print(g_p_sem_paralelas)
#
# print("g_c")
# print(g_c.warshall())
# print(g_c)
#
# print("g_c3")
# print(g_c3.warshall())
# print(g_c3)
#
# print("g_l1")
# print(g_l1.warshall())
# print(g_l1)
#
# print("g_l2")
# print(g_l2.warshall())
# print(g_l2)

# print("g_l3")
# print(g_l3.warshall())
# print(g_l3)
#
# print("g_l4")
# print(g_l4.warshall())
# print(g_l4)
#
# print("g_l5")
# print(g_l5.warshall())
# print(g_l5)