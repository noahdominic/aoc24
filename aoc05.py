from collections import deque

class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def __repr__(self):
        return f"Node({self.name}) with Edges: {[n.name for n in self.edges]}"

    def connect(self, node):
        self.edges.append(node)

def topological_sort(graph, nodes_to_sort):
    # Calculate in-degrees for the nodes in the subset
    in_degree = {node: 0 for node in nodes_to_sort}
    for node in nodes_to_sort:
        if node in graph:
            for neighbor in graph[node].edges:
                if neighbor.name in nodes_to_sort:
                    in_degree[neighbor.name] += 1

    # Begin BFS sorting
    queue = deque([node for node in nodes_to_sort if in_degree[node] == 0])
    sorted_nodes = []

    while queue:
        current_node = queue.popleft()
        sorted_nodes.append(current_node)

        # Decrease the in-degree of the neighbors and add those with zero in-degree
        for neighbour in graph[current_node].edges:
            if neighbour.name in nodes_to_sort:
                in_degree[neighbour.name] -= 1
                if in_degree[neighbour.name] == 0:
                    queue.append(neighbour.name)

    # If we haven't sorted all nodes in the subset, there was a cycle in the subset
    return sorted_nodes

def day05_01(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()

        midpoint = lines.index('')

        rules = lines[:midpoint]
        paths = lines[midpoint + 1:]

        node_graph = {}
        for rule in rules:
            src_node, dst_node = rule.split("|")
            if src_node not in node_graph:
                node_graph[src_node] = Node(src_node)
            if dst_node not in node_graph:
                node_graph[dst_node] = Node(dst_node)
            node_graph[src_node].connect(node_graph[dst_node])

        total = 0

        for path in paths:
            candidate_path = [node for node in path.split(",")]

            is_valid = True
            count = 0

            for i, current_node in enumerate(candidate_path):
                for prev_node in candidate_path[:i]:
                    if prev_node not in node_graph:
                        is_valid = False
                        break
                    if current_node not in [node.name for node in node_graph[prev_node].edges]:
                        is_valid = False
                        break
                if not is_valid:
                    break
                count += 1

            if is_valid:
                total += int(candidate_path[int(len(candidate_path)/2)])

        print(f"TOTAL: {total}")

def day05_02(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()

        midpoint = lines.index('')

        rules = lines[:midpoint]
        paths = lines[midpoint + 1:]

        node_graph = {}
        for rule in rules:
            src_node, dst_node = rule.split("|")
            if src_node not in node_graph:
                node_graph[src_node] = Node(src_node)
            if dst_node not in node_graph:
                node_graph[dst_node] = Node(dst_node)
            node_graph[src_node].connect(node_graph[dst_node])

        total = 0

        for path in paths:
            candidate_path = [node for node in path.split(",")]

            is_valid = True
            count = 0

            for i, current_node in enumerate(candidate_path):
                for prev_node in candidate_path[:i]:
                    if prev_node not in node_graph:
                        is_valid = False
                        break
                    if current_node not in [node.name for node in node_graph[prev_node].edges]:
                        is_valid = False
                        break
                if not is_valid:
                    break
                count += 1

            if is_valid:
                continue

            sorted_path = topological_sort(node_graph, candidate_path)
            total += int(sorted_path[int(len(candidate_path)/2)])

        print(f"TOTAL: {total}")


