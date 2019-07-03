def vertices():
    lis = []
    print("Digite os vertices do grafo separados por espaço")
    inp = str(input())
    inp = inp.split(" ")
    for c in inp:
        if c not in ['', ' ']:
            lis.append(c)
    print("vertices = {}".format(lis))
    return lis

def arestas():
    lis = []
    print("Digite as arestas do grafo")
    while True:
        try:
            inp = str(input())
            lis.append(["{}-{}".format(inp[0], inp[1]), 1])
        except:
            print("arestas = {}".format(lis))
            return




vertices()
arestas()
