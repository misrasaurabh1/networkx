import pytest
import networkx as nx


class TestToNetworkXGraphBenchmark:
    params = [nx.Graph, nx.DiGraph]

    def setup_method(self):
        self.edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]

    @pytest.mark.parametrize("graph_type", [nx.Graph, nx.DiGraph])
    def test_to_networkx_graph_direct(self, graph_type):
        _ = nx.to_networkx_graph(self.edges, create_using=graph_type)

    @pytest.mark.parametrize("graph_type", [nx.Graph, nx.DiGraph])
    def test_to_networkx_graph_via_constructor(self, graph_type):
        _ = graph_type(self.edges)

    ### NOTE: Multi-instance checks are explicitly included to cover the case
    # where many graph instances are created, which is not uncommon in graph
    # analysis. The reason why multi-instance is explicitly probed (rather than
    # relying solely on the number of repeats/runs from `timeit` in the benchmark
    # suite) is to capture/amplify any distinctions from potential import
    # caching of the try-excepts in the *same* run

    @pytest.mark.parametrize("graph_type", [nx.Graph, nx.DiGraph])
    def test_to_networkx_graph_direct_multi_instance(self, graph_type):
        for _ in range(500):  # Creating many graph instances
            _ = nx.to_networkx_graph(self.edges, create_using=graph_type)

    @pytest.mark.parametrize("graph_type", [nx.Graph, nx.DiGraph])
    def test_to_networkx_graph_via_constructor_multi_instance(self, graph_type):
        for _ in range(500):  # Creating many graph instances
            _ = graph_type(self.edges)
