#!/usr/bin/python3

from Grafo import Grafo

G = Grafo()

def ler(G, file):
    line = file.readline()
    spt = line.split()
    x = (spt[0])
    y = (spt[1])
    z = (spt[2])
    if '.' in z:
        z = float(z)
    else:
        z = int(z)
    G.add_aresta(x, y, z)
    G.add_aresta(y, x, z)
    return G

def imprime_grafo(G):
    for v in G:
        for w in v.get_adj():
            print(v.get_ID(), w.get_ID(), v.get_peso(w))
    print('\n')

def abre_arquivo(path):
    try:
        f = open(path, 'r')
    except FileNotFoundError:
        print("Arquivo inexistente na pasta entradas, tente novamente...")
        interface_arquivo()
        return

    nro_vertices = int(f.readline())
    nro_arestas = int(f.readline())
    for i in range(nro_arestas):
        ler(G, f)

    f.close()

def interface_arquivo():
    arquivo = input("Digite o nome do arquivo de entrada (deve estar na pasta entradas): ")
    arquivo = "entradas/" + str(arquivo) + ".txt"
    abre_arquivo(arquivo)

def make_set(vertice):
    vertice.pai = vertice
    vertice.ranking = 0

def find_set(vertice):
    if (vertice.get_pai() != vertice):
        vertice.pai = find_set(vertice.get_pai())
    return vertice.get_pai()

def union(vertice1, vertice2):
    raiz1 = find_set(vertice1)
    raiz2 = find_set(vertice2)
    if raiz1 != raiz2:
        if (raiz1.get_ranking() > raiz2.get_ranking()):
            raiz2.pai = raiz1
        else:
            raiz1.pai = raiz2
            if (raiz1.get_ranking() == raiz2.get_ranking()):
                raiz2.ranking += 1

# Algoritmo de kruskal para árvore geradora mínima
def kruskal(G):
    total = 0
    mst = []
    for k in G:
        make_set(k)
    arestas = list(G.get_itens())
    arestas.sort(key=lambda x: x[1])
    for aresta in arestas:
        vertice1, vertice2 = aresta[0]
        vertice1 = G.get_vertice(vertice1)
        vertice2 = G.get_vertice(vertice2)
        if find_set(vertice1) != find_set(vertice2):
            union(vertice1, vertice2)
            mst.append(aresta[0])
            total += aresta[1]
    print("Total: " , total)
    return mst

#Menu de opções
def menu():
    print("Escolha uma das opcoes ou pressione 'q' para sair")
    print("[1] Arvore Geradora Minima - Kruskal")
    print("[2] Imprimir Grafo")
    print("[3] Trocar arquivo")
    print("[q] Sair")

#Interação com o usuário
interface_arquivo()
menu()
while True:
    teclado = input()
    if teclado == '1':
            caminho = kruskal(G)
            print("Arestas do caminho: ")
            print(caminho)
    elif teclado == '2':
        imprime_grafo(G)
    elif teclado == '3':
        del G
        G = Grafo()
        interface_arquivo()
        imprime_grafo(G)
    elif teclado == 'q':
        print("Tchau!")
        break
    else:
        menu()
