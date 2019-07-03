from grafo_adj_nao_dir import Grafo

# grafo_1 = Grafo([], [])
# for i in ['A', 'B', 'C', 'D']:
#     grafo_1.adiciona_vertice(i)
# for i in ['A-B', 'A-C', 'B-D', 'D-C']:
#     grafo_1.adiciona_aresta(i)
#
# print("grafo_1")
# print(grafo_1)
# print(grafo_1.caminho_euleriano_path())
#
# grafo_2 = Grafo([], [])
# for i in ['A', 'B', 'C', 'D', 'E']:
#     grafo_2.adiciona_vertice(i)
# for i in ['A-B', 'A-E', 'B-C', 'C-D', 'D-E']:
#     grafo_2.adiciona_aresta(i)
#
# print("grafo_2")
# print(grafo_2)
# print(grafo_2.caminho_euleriano_path())
#
# VERIFICAR ESTE CASO DE TESTE COM HENRIQUE
# grafo_3 = Grafo([], [])
# for i in ['A', 'B', 'C', 'D']:
#     grafo_3.adiciona_vertice(i)
# for i in ['A-B', 'A-C', 'B-D', 'D-D', 'C-C']:
#     grafo_3.adiciona_aresta(i)
#
# print(grafo_3)
# print(grafo_3.caminho_euleriano_path())

# grafo_4 = Grafo([], [])
# for i in ['A', 'B', 'C', 'D']:
#     grafo_4.adiciona_vertice(i)
# for i in ['A-B', 'A-C', 'B-D', 'B-C', 'D-C']:
#     grafo_4.adiciona_aresta(i)
#
# print("grafo_4")
# print(grafo_4)
# print(grafo_4.caminho_euleriano_path())
#
# grafo_5 = Grafo([], [])
# for i in ['A', 'B', 'C', 'D']:
#     grafo_5.adiciona_vertice(i)
# for i in ['A-B', 'A-C', 'A-D', 'B-D', 'B-C', 'D-C']:
#     grafo_5.adiciona_aresta(i)
#
# print("grafo_5")
# print(grafo_5)
# print(grafo_5.caminho_euleriano_path())
#
# konigsberg = Grafo([], [])
# for i in ['M', 'T', 'B', 'R']:
#     konigsberg.adiciona_vertice(i)
# for i in ['M-T', 'M-T', 'M-B', 'M-B', 'M-R', 'B-R', 'T-R']:
#     konigsberg.adiciona_aresta(i)
#
# print("konigsberg")
# print(konigsberg)
# print(konigsberg.caminho_euleriano_path())
#
# # Grafos com caminho euleriano
# konigsberg_mod = Grafo([], [])
# for i in ['M', 'T', 'B', 'R']:
#     konigsberg_mod.adiciona_vertice(i)
# for i in ['M-T', 'M-T', 'M-B', 'M-B', 'M-R', 'M-R', 'B-R', 'T-R']:
#     konigsberg_mod.adiciona_aresta(i)
#
# print("konigsberg_mod")
# print(konigsberg_mod)
# print(konigsberg_mod.caminho_euleriano_path())

# g_c_e = Grafo([], [])
# for i in ['A', 'B', 'C']:
#     g_c_e.adiciona_vertice(i)
# for i in ['A-B', 'B-C']:
#     g_c_e.adiciona_aresta(i)
#
# print("g_c_e")
# print(g_c_e)
# print(g_c_e.caminho_euleriano_path())

# # Grafo da Paraíba
# g_p = Grafo([], [])
# for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
#     g_p.adiciona_vertice(i)
# for i in ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
#     g_p.adiciona_aresta(i)
#
# print("g_p")
# print(g_p)
# print(g_p.caminho_euleriano_path())
#
# # Grafo da Paraíba sem arestas paralelas
# g_p_sem_paralelas = Grafo([], [])
# for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
#     g_p_sem_paralelas.adiciona_vertice(i)
# for i in ['J-C', 'C-E', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
#     g_p_sem_paralelas.adiciona_aresta(i)
#
# print("g_p_sem_paralelas")
# print(g_p_sem_paralelas)
# print(g_p_sem_paralelas.caminho_euleriano_path())
#
# # Grafos completos
# g_c = Grafo([], [])
# for i in ['J', 'C', 'E', 'P']:
#     g_c.adiciona_vertice(i)
# for i in ['J-C', 'J-E', 'J-P', 'C-E', 'C-P', 'E-P']:
#     g_c.adiciona_aresta(i)
#
# print("g_c")
# print(g_c)
# print(g_c.caminho_euleriano_path())
#
# g_c2 = Grafo([], [])
# for i in ['J', 'C', 'E', 'P']:
#     g_c2.adiciona_vertice(i)
# for i in ['J-C', 'E-J', 'J-P', 'E-C', 'C-P', 'P-E']:
#     g_c2.adiciona_aresta(i)
#
# print("g_c2")
# print(g_c2)
# print(g_c2.caminho_euleriano_path())
#
# g_c3 = Grafo([], [])
# g_c3.adiciona_vertice('J')
#
# print("g_c3")
# print(g_c3)
# print(g_c3.caminho_euleriano_path())
#
# # Grafos com laco
# g_l1 = Grafo([], [])
# for i in ['A', 'B', 'C', 'D']:
#     g_l1.adiciona_vertice(i)
# for i in ['A-A', 'B-A', 'A-A']:
#     g_l1.adiciona_aresta(i)
#
# print("g_l1")
# print(g_l1)
# print(g_l1.caminho_euleriano_path())
#
# g_l2 = Grafo([], [])
# for i in ['A', 'B', 'C', 'D']:
#     g_l2.adiciona_vertice(i)
# for i in ['A-B', 'B-B', 'B-A']:
#     g_l2.adiciona_aresta(i)
#
# print("g_l2")
# print(g_l2)
# print(g_l2.caminho_euleriano_path())
#
# g_l3 = Grafo([], [])
# for i in ['A', 'B', 'C', 'D']:
#     g_l3.adiciona_vertice(i)
# for i in ['C-A', 'C-C', 'D-D']:
#     g_l3.adiciona_aresta(i)
#
# print("g_l3")
# print(g_l3)
# print(g_l3.caminho_euleriano_path())
#
# g_l4 = Grafo([], [])
# g_l4.adiciona_vertice('D')
# g_l4.adiciona_aresta('D-D')
#
# print("g_l4")
# print(g_l4)
# print(g_l4.caminho_euleriano_path())
#
# g_l5 = Grafo([], [])
# for i in ['C', 'D']:
#     g_l5.adiciona_vertice(i)
# for i in ['D-C', 'C-C']:
#     g_l5.adiciona_aresta(i)
#
# print("g_l5")
# print(g_l5)
# print(g_l5.caminho_euleriano_path())


# grafos de judenilson
judA = Grafo([], []) # grafo com caminho euleriano, com vertices de grau ímpar no começo.
for i in ['T', 'B', 'M', 'R']:
    judA.adiciona_vertice(i)
for i in ['M-T', 'M-T', 'M-B', 'M-B', 'M-R', 'M-R', 'B-R', 'T-R']:
    judA.adiciona_aresta(i)

print("judA")
print(judA)
print(judA.caminho_euleriano_path())

# print(judA.caminho_euleriano())

# print(judA.new_eh_conexo())

judB = Grafo([], []) # grafo com caminho euleriano, com vertices apenas de grau par.
for i in ['T', 'B', 'M', 'R']:
    judB.adiciona_vertice(i)
for i in ['M-T', 'M-T', 'M-B', 'M-B', 'M-R', 'M-R']:
    judB.adiciona_aresta(i)

print("judB")
print(judB)
print(judB.caminho_euleriano_path())