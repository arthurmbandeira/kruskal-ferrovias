from collections import OrderedDict

class Vertice:
    """docstring for Vertice"""
    def __init__(self, chave):
        self.id = chave
        self.cor = ""
        self.pai = None
        self.adj = OrderedDict()
        self.d = 0
        self.f = 0
        self.nivel = 0
        self.ranking = 0

    def add_vizinho(self, vizinho, peso = 0):
        self.adj[vizinho] = peso

    def get_adj(self):
        return self.adj.keys()

    def get_ID(self):
        return self.id

    def get_cor(self):
        return self.cor

    def get_pai(self):
        if (self.pai):
            return self.pai
        else:
            return None

    def get_peso(self, vizinho):
        if (self.adj[vizinho]):
            return self.adj[vizinho]
        else: return None

    def get_termino(self):
        return self.f

    def get_nivel(self):
        return self.nivel

    def get_ranking(self):
        return self.ranking

    # def __lt__(self, other):
    #     return self.nivel < other.nivel
