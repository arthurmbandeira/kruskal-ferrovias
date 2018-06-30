from Vertice import Vertice
from collections import OrderedDict

class Grafo:
    """docstring for Grafo"""
    def __init__(self):
        self.lista_vertices = OrderedDict()
        self.num_vertices = 0
        self.topological_sort = []
        self.arestas = {}

    def add_vertice(self, chave):
        self.num_vertices += 1
        novo_vertice = Vertice(chave)
        self.lista_vertices[chave] = novo_vertice
        return novo_vertice

    def get_vertice(self, v):
        if v in self.lista_vertices:
            return self.lista_vertices[v]
        else:
            return None

    def add_aresta(self, atual, vizinho, peso = 0):
        if atual not in self.lista_vertices:
            nv = self.add_vertice(atual)
        if vizinho not in self.lista_vertices:
            nv = self.add_vertice(vizinho)
        self.lista_vertices[atual].add_vizinho(self.lista_vertices[vizinho], peso)
        self.arestas[(atual, vizinho)] = peso

    def get_vertices(self):
        return self.lista_vertices.keys()

    def get_arestas(self):
        return self.arestas.keys()

    def get_itens(self):
        return self.arestas.items()

    def __iter__(self):
        return iter(self.lista_vertices.values())
