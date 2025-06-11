from itertools import permutations

import pytest
import networkx as nx


class TestGraphBenchmark:
    params = ["Graph", "DiGraph", "MultiGraph", "MultiDiGraph"]

    def setup_method(self):
        self.nodes = list(range(1, 1000))
        self.edges = []
        self.subgraph_nodes = list(range(1, 100))
        self.subgraph_nodes_large = list(range(1, 900))

    @pytest.mark.parametrize("graph_type", ["Graph", "DiGraph", "MultiGraph", "MultiDiGraph"])
    def test_graph_create(self, graph_type):
        _ = getattr(nx, graph_type)()

    @pytest.mark.parametrize("graph_type", ["Graph", "DiGraph", "MultiGraph", "MultiDiGraph"])
    def test_add_nodes_from(self, graph_type):
        self.G = getattr(nx, graph_type)()
        self.G.add_nodes_from(self.nodes)

    @pytest.mark.parametrize("graph_type", ["Graph", "DiGraph", "MultiGraph", "MultiDiGraph"])
    def test_add_edges_from(self, graph_type):
        self.G = getattr(nx, graph_type)()
        self.G.add_edges_from(self.edges)

    @pytest.mark.parametrize("graph_type", ["Graph", "DiGraph", "MultiGraph", "MultiDiGraph"])
    def test_remove_nodes_from(self, graph_type):
        self.G = getattr(nx, graph_type)()
        self.G.add_nodes_from(self.nodes)
        self.G.remove_nodes_from(self.nodes)

    @pytest.mark.parametrize("graph_type", ["Graph", "DiGraph", "MultiGraph", "MultiDiGraph"])
    def test_remove_edges_from(self, graph_type):
        self.G = getattr(nx, graph_type)()
        self.G.add_edges_from(self.edges)
        self.G.remove_edges_from(self.edges)

    @pytest.mark.parametrize("graph_type", ["Graph", "DiGraph", "MultiGraph", "MultiDiGraph"])
    def test_copy(self, graph_type):
        self.G = getattr(nx, graph_type)()
        _ = self.G.copy()

    @pytest.mark.parametrize("graph_type", ["Graph", "DiGraph", "MultiGraph", "MultiDiGraph"])
    def test_to_directed(self, graph_type):
        self.G = getattr(nx, graph_type)()
        _ = self.G.to_directed()

    @pytest.mark.parametrize("graph_type", ["Graph", "DiGraph", "MultiGraph", "MultiDiGraph"])
    def test_to_undirected(self, graph_type):
        self.G = getattr(nx, graph_type)()
        _ = self.G.to_undirected()

    @pytest.mark.parametrize("graph_type", ["Graph", "DiGraph", "MultiGraph", "MultiDiGraph"])
    def test_subgraph(self, graph_type):
        self.G = getattr(nx, graph_type)()
        _ = self.G.subgraph(self.subgraph_nodes).copy()

    @pytest.mark.parametrize("graph_type", ["Graph", "DiGraph", "MultiGraph", "MultiDiGraph"])
    def test_subgraph_large(self, graph_type):
        self.G = getattr(nx, graph_type)()
        _ = self.G.subgraph(self.subgraph_nodes_large).copy()
