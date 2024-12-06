class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def __repr__(self):
        return f"Node({self.name}) with Edges: {[n.name for n in self.edges]}"

    def connect(self, node):
        self.edges.append(node)

def dfs(graph, start, end, visited=None):
    if visited is None:
        visited = set()

    # If we've already visited the current node, avoid revisiting
    if start in visited:
        return False
    visited.add(start)

    # If we reached the end node
    if start == end:
        return True

    # Traverse through all the connected nodes
    for neighbor in graph[start].edges:
        if dfs(graph, neighbor.name, end, visited):
            return True
 
    return False

def day05_01(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()

        midpoint = lines.index('')

        rules = lines[:midpoint]
        paths = lines[midpoint + 1:]

        node_graph = {}
        for rule in rules:
            src_node, dst_node = rule.split("|")
            print(src_node, '->', dst_node)
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

            print(candidate_path)

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
                print(f"Valid! This adds {int(candidate_path[int(len(candidate_path)/2)])} to the total.\n\n")
                total += int(candidate_path[int(len(candidate_path)/2)])
            else:
                print("NOT VALID!!!!\n\n")

        print(f"TOTAL: {total}\n\n")

def day05_02(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()

        midpoint = lines.index('')

        rules = lines[:midpoint]
        paths = lines[midpoint + 1:]

        node_graph = {}
        for rule in rules:
            src_node, dst_node = rule.split("|")
            print(src_node, '->', dst_node)
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

            print(candidate_path)

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
                print(f"Valid! This adds {int(candidate_path[int(len(candidate_path)/2)])} to the total.\n\n")
                total += int(candidate_path[int(len(candidate_path)/2)])
            else:
                print("NOT VALID!!!!\n\n")

        print(f"TOTAL: {total}\n\n")


