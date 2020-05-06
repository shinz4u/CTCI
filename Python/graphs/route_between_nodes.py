from linkedlists.linkedlist import Node

#
#
#
# def route_between_nodes_BFS(a_node, b_node):
#     """Implementing BFS"""
#     start = a_node
#
#
#
#     pass
#
#
#
#
# a_node = Node()
# b_node = Node()
# route_between_nodes_BFS(a_node,b_node)

class Graph():
    def __init__(self):
        # self.node_list = []
        self.adjacency_list = {}

    def add_node(self, start_node, end_node):
        start_node = Node(start_node)
        end_node = Node(start_node)
        if start_node in self.adjacency_list:
            self.adjacency_list[start_node].append
        self.adjacency_list[start_node]

        if start_node in self.adjacency_list:
            self.adjacency_list[start_node].append(end_node)
        else:
            self.adjacency_list[start_node] = [end_node]
            # self.node_list.append(start_node, end_node)

    def something(self):
        pass

graph = Graph()
graph.add_node(5, 6)


def route_between_nodes_BFS(graph, a_node, b_node):
    """Implementing BFS"""
    if a_node == b_node:
        return True
    to_see_nodes = graph.adjacency_list[a_node]
    seen_nodes = [a_node]

    while len(to_see_nodes) > 0:
        node = to_see_nodes.pop(0)
        if node in seen_nodes:
            continue
        if node == b_node:
            return True
        else:
            seen_nodes.append(node)
            to_see_nodes.extend(graph.adjacency_list[node])




