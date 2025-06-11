import pytest
import networkx as nx


# NOTE: explicit set construction in benchmarks is required for meaningful
# comparisons due to change in return type from generator -> set. See gh-7244.
class TestNonNeighbors:
    params = [10, 100, 1000]

    def setup_method(self):
        pass

    @pytest.mark.parametrize("num_nodes", [10, 100, 1000])
    def test_star_center(self, num_nodes):
        star_graph = nx.star_graph(num_nodes)
        set(nx.non_neighbors(star_graph, 0))

    @pytest.mark.parametrize("num_nodes", [10, 100, 1000])
    def test_star_rim(self, num_nodes):
        star_graph = nx.star_graph(num_nodes)
        set(nx.non_neighbors(star_graph, 5))

    @pytest.mark.parametrize("num_nodes", [10, 100, 1000])
    def test_complete(self, num_nodes):
        complete_graph = nx.complete_graph(num_nodes)
        set(nx.non_neighbors(complete_graph, 0))

    @pytest.mark.parametrize("num_nodes", [10, 100, 1000])
    def test_path_first(self, num_nodes):
        path_graph = nx.path_graph(num_nodes)
        set(nx.non_neighbors(path_graph, 0))

    @pytest.mark.parametrize("num_nodes", [10, 100, 1000])
    def test_path_last(self, num_nodes):
        path_graph = nx.path_graph(num_nodes)
        set(nx.non_neighbors(path_graph, num_nodes - 1))

    @pytest.mark.parametrize("num_nodes", [10, 100, 1000])
    def test_path_center(self, num_nodes):
        path_graph = nx.path_graph(num_nodes)
        set(nx.non_neighbors(path_graph, num_nodes // 2))


# NOTE: explicit set construction in benchmarks is required for meaningful
# comparisons due to change in return type from generator -> set. See gh-7244.
class TestCommonNeighbors:
    params = [10, 100, 1000]

    def setup_method(self):
        pass

    @pytest.mark.parametrize("num_nodes", [10, 100, 1000])
    def test_star_center_rim(self, num_nodes):
        star_graph = nx.star_graph(num_nodes)
        set(nx.common_neighbors(star_graph, 0, num_nodes // 2))

    @pytest.mark.parametrize("num_nodes", [10, 100, 1000])
    def test_star_rim_rim(self, num_nodes):
        star_graph = nx.star_graph(num_nodes)
        set(nx.common_neighbors(star_graph, 4, 5))

    @pytest.mark.parametrize("num_nodes", [10, 100, 1000])
    def test_complete(self, num_nodes):
        complete_graph = nx.complete_graph(num_nodes)
        set(nx.common_neighbors(complete_graph, 0, num_nodes // 2))
