class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(u)

    def get_adjacent_nodes(self, u):
        return self.graph.get(u, [])

    def get_all_nodes(self):
        return list(self.graph.keys())

    def is_edge(self, u, v):
        return u in self.graph and v in self.graph[u]

    def remove_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
            self.graph[v].remove(u)

    def remove_node(self, u):
        if u in self.graph:
            adjacent_nodes = self.graph[u]
            del self.graph[u]
            for node in adjacent_nodes:
                self.graph[node].remove(u)

    def print_graph(self):
        for node in self.graph:
            print(node, "->", " -> ".join(map(str, self.graph[node])))

def main():
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    print("----------------")
    g.print_graph()
    print("----------------")
    print()
    print("ADJACENT NODES OF NODE 0:", g.get_adjacent_nodes(0))
    print("=========================")
    print("ALL NODES IN THE GRAPH:", g.get_all_nodes())
    print("=======================")
    print()
    print("--------------------------------------")
    print("IS THERE AN EDGE BETWEEN 1 and 2?", g.is_edge(1, 2))
    print("--------------------------------------")
    print()
    g.remove_edge(1, 2)
    print("AFTER REMOVING EDGE BETWEEN 1 and 2:")
    print("====================================")
    g.print_graph()
    print()
    g.remove_node(1)
    print("AFTER REMOVING NODE 1:")
    print("======================")
    g.print_graph()

main()
