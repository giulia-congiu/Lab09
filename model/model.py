import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = DAO.getAllNodes()
        self._idMapAO = {} #creo una mappa con i nodi aereo: chiave id, valore aereoporto
        for n in self._nodes:
            self._idMapAO[n.ID] = n

    def buildGraph(self, distanza):
        # aggiunge i nodi
        self._graph.add_nodes_from(self._nodes)

        # aggiunge gli archi
        self.addEdges(distanza)

    def getNumNodes(self):
        return len(self._graph.nodes)

    def getNumEdges(self):
        return len(self._graph.edges)

    def addEdges(self, distanza):
        allEdges = DAO.getAllEdges(distanza, self._idMapAO)
        for e in allEdges:
                self._graph.add_edge(e[0], e[1], weight=e[2])
