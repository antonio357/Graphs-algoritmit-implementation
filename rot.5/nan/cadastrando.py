def conferi_cadastro():
    for v in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "W", "Z", "1", "2", "3", "4", "5", "6", "7"]:
        lis_vertices_ligados = []
        for aresta in ['A-B', 'A-C', 'A-D', 'B-H', 'B-I', 'C-F', 'D-C', 'D-E', 'E-F', 'E-L', 'F-G', 'F-J', 'F-K', 'G-B', 'G-J', 'H-G',
          'I-P', 'J-I', 'J-O', 'K-N', 'L-M', 'M-Q', 'N-R', 'O-5', 'O-R', 'O-Q', 'P-R', 'P-T', 'R-5', 'R-Y',
          'T-U', 'U-7', 'U-W', 'V-2', 'V-W', 'V-X', 'X-R', 'Y-Z', 'Y-1', '1-3', '1-X', '3-4', '3-S',
          '5-T', '5-V', '6-3', '7-6']:
            if aresta[0] == v:
                lis_vertices_ligados.append(aresta[-1])
        print("o vertice {} vai para as seguintes arestas = {}".format(v, lis_vertices_ligados))

conferi_cadastro()