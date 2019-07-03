def ehComentario(string):
    if string[0] == "#":
        return True
    return False

def pegaNome(string):
    s = string.split(' ')
    index = s.index("Topológica")
    s1 = ""
    for string in range(index + 1, len(s)):
        s2 = s[string]
        s2 = s2.lower().capitalize()
        s1 += s2
    return s1.rstrip()

def finalArestasGrafo(apontadorLinha, lines):
    if "adiciona_aresta(i)" in lines[apontadorLinha]:
        return True
    return False

def finalVerticesGrafo(apontadorLinha, lines):
    if "adiciona_vertice(i)" in lines[apontadorLinha]:
        return True
    return False

def verticesAppend(line, vertices):
    counter = 0
    while counter < len(line):
        char = line[counter]
        counter += 1
        if char == "'":
            s = ''
            char = line[counter]
            while char != "'":
                s += char
                counter += 1
                char = line[counter]
            counter += 1
            vertices.append(s)

def arestasAppend(line, arestas):
    counter = 0
    while counter < len(line):
        char = line[counter]
        counter += 1
        if char == "'":
            s = ''
            char = line[counter]
            while char != "'":
                s += char
                counter += 1
                char = line[counter]
            counter += 1
            arestas.append(s)

def reformatandoArestas(arestas):
    ed = []
    for a in arestas:
        ed.append([a, 1])
    return ed

grafos = {}

text = open("cases.txt", "r")

lines = text.readlines()

apontadorLinha = 0
while apontadorLinha < len(lines):
    line = lines[apontadorLinha]
    apontadorLinha += 1
    if ehComentario(line):
        apontadorLinha += 1  # pulando self.edificios = Grafo([], [])
        nomeDoGrafo = pegaNome(line)
        vertices = []
        while not finalVerticesGrafo(apontadorLinha, lines):
            line = lines[apontadorLinha]
            verticesAppend(line, vertices)
            apontadorLinha += 1
        apontadorLinha += 1  # pulando a self.edificios.adiciona_vertice(i)
        arestas = []
        while not finalArestasGrafo(apontadorLinha, lines):
            line = lines[apontadorLinha]
            arestasAppend(line, arestas)
            apontadorLinha += 1
        apontadorLinha += 1  # puando self.telematica.adiciona_aresta(i)

        arestas = reformatandoArestas(arestas)
        grafos[nomeDoGrafo] = {"arestas": arestas, "vertices": vertices}

text.close()

output_file = open("casos de teste reformatados.txt", "w")

for k in grafos.keys():
    output_file.write("self.{} = Grafo([], [])\n".format(k))
    output_file.write("{}Vertices = {}\n".format(k, grafos[k]["vertices"]))
    output_file.write("{}Arestas = {}\n\n".format(k, grafos[k]["arestas"]))
    output_file.write("    for v in {}Vertices:\n".format(k))
    output_file.write("        self.{}.adiciona_vertice(v)\n".format(k))
    output_file.write("    for ed in {}Arestas:\n".format(k))
    output_file.write("        self.{}.adiciona_aresta(ed)\n\n\n".format(k))

output_file.close()

