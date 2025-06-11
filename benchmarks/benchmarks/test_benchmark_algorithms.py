"""Benchmarks for a certain set of algorithms"""

import pytest
import networkx as nx
from benchmarks.utils import fetch_drug_interaction_network
from networkx.algorithms import community


class TestAlgorithmBenchmarks:
    timeout = 120
    nodes = 100
    _graphs = [
        nx.erdos_renyi_graph(nodes, 0.1),
        nx.erdos_renyi_graph(nodes, 0.5),
        nx.erdos_renyi_graph(nodes, 0.9),
        fetch_drug_interaction_network(),
    ]
    params = [
        "Erdos Renyi (100, 0.1)",
        "Erdos Renyi (100, 0.5)",
        "Erdos Renyi (100, 0.9)",
        "Drug Interaction network",
    ]

    def setup_method(self):
        self.graphs_dict = dict(zip(self.params, self._graphs))

    @pytest.mark.parametrize("graph", [
        "Erdos Renyi (100, 0.1)",
        "Erdos Renyi (100, 0.5)",
        "Erdos Renyi (100, 0.9)",
        "Drug Interaction network",
    ])
    def test_betweenness_centrality(self, graph):
        # timing this should also give us information about
        # underlying shortest path methods
        _ = nx.betweenness_centrality(self.graphs_dict[graph])

    @pytest.mark.parametrize("graph", [
        "Erdos Renyi (100, 0.1)",
        "Erdos Renyi (100, 0.5)",
        "Erdos Renyi (100, 0.9)",
        "Drug Interaction network",
    ])
    def test_greedy_modularity_communities(self, graph):
        _ = community.greedy_modularity_communities(self.graphs_dict[graph])

    @pytest.mark.parametrize("graph", [
        "Erdos Renyi (100, 0.1)",
        "Erdos Renyi (100, 0.5)",
        "Erdos Renyi (100, 0.9)",
        "Drug Interaction network",
    ])
    def test_louvain_communities(self, graph):
        _ = community.louvain_communities(self.graphs_dict[graph])

    @pytest.mark.parametrize("graph", [
        "Erdos Renyi (100, 0.1)",
        "Erdos Renyi (100, 0.5)",
        "Erdos Renyi (100, 0.9)",
        "Drug Interaction network",
    ])
    def test_pagerank(self, graph):
        _ = nx.pagerank(self.graphs_dict[graph])

    @pytest.mark.parametrize("graph", [
        "Erdos Renyi (100, 0.1)",
        "Erdos Renyi (100, 0.5)",
        "Erdos Renyi (100, 0.9)",
        "Drug Interaction network",
    ])
    def test_connected_components(self, graph):
        _ = list(nx.connected_components(self.graphs_dict[graph]))

    @pytest.mark.parametrize("graph", [
        "Erdos Renyi (100, 0.1)",
        "Erdos Renyi (100, 0.5)",
        "Erdos Renyi (100, 0.9)",
        "Drug Interaction network",
    ])
    def test_k_core(self, graph):
        _ = nx.k_core(self.graphs_dict[graph])

    @pytest.mark.parametrize("graph", [
        "Erdos Renyi (100, 0.1)",
        "Erdos Renyi (100, 0.5)",
        "Erdos Renyi (100, 0.9)",
        "Drug Interaction network",
    ])
    def test_average_clustering(self, graph):
        _ = nx.average_clustering(self.graphs_dict[graph])


class TestAlgorithmBenchmarksConnectedGraphsOnly:
    timeout = 120
    nodes = 100
    _graphs = [
        nx.erdos_renyi_graph(nodes, 0.1),
        nx.erdos_renyi_graph(nodes, 0.5),
        nx.erdos_renyi_graph(nodes, 0.9),
    ]
    params = [
        "Erdos Renyi (100, 0.1)",
        "Erdos Renyi (100, 0.5)",
        "Erdos Renyi (100, 0.9)",
    ]

    def setup_method(self):
        self.graphs_dict = dict(zip(self.params, self._graphs))

    @pytest.mark.parametrize("graph", [
        "Erdos Renyi (100, 0.1)",
        "Erdos Renyi (100, 0.5)",
        "Erdos Renyi (100, 0.9)",
    ])
    def test_eigenvector_centrality_numpy(self, graph):
        # Added to ensure the connectivity check doesn't affect
        # performance too much (see gh-6888, gh-7549).
        _ = nx.eigenvector_centrality_numpy(self.graphs_dict[graph])

    @pytest.mark.parametrize("graph", [
        "Erdos Renyi (100, 0.1)",
        "Erdos Renyi (100, 0.5)",
        "Erdos Renyi (100, 0.9)",
    ])
    def test_square_clustering(self, graph):
        _ = nx.square_clustering(self.graphs_dict[graph])
