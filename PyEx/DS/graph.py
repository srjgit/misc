class Graph:
    def __init__(self):
        self.Nodes = {}
    
    def add_node(self, node):
        if not self.Nodes.has_key(node):
            self.Nodes[node] = []

    def add_node(self, node, edges):
        if not self.Nodes.has_key(node):
            self.Nodes[node] = edges

    def find_path(self, start, end, path=[]):
        path.append(start)
        if start == end:
            return path
        if not self.Nodes.has_key(start):
            return None
        for node in self.Nodes[start]:
            if node not in path:
                newpath = self.find_path(node, end, path)
                if newpath: return newpath

        return None

    def show_graph(self):
        return self.Nodes

if __name__ == '__main__':
    g = Graph()
    g.add_node('A', ['B', 'C'])
    g.add_node('B', ['C', 'D'])
    g.add_node('C', ['D'])
    g.add_node('D', ['C'])
    g.add_node('E', ['F'])
    g.add_node('F', ['C'])

    print g.show_graph()

    print g.find_path('C', 'F')
