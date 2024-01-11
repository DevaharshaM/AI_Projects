#importing library
from queue import PriorityQueue

#defining class
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor, cost):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append((neighbor, cost))

#function for UCF
def ucs(graph, start, goal):
    priority_queue = PriorityQueue()
    priority_queue.put((0, [start]))
    visited = set()

    while not priority_queue.empty():
        cost, path = priority_queue.get()
        node = path[-1]

        if node in visited:
            continue

        neighbors = graph[node]
        for neighbor, edge_cost in neighbors:
            new_cost = cost + edge_cost
            new_path = list(path)
            new_path.append(neighbor)
            priority_queue.put((new_cost, new_path))

            if neighbor == goal:
                return new_path, new_cost

        visited.add(node)

    return None, None

if __name__ == "__main__":

    graph = Graph()
    graph.add_edge("1", "2", 7)
    graph.add_edge("1", "3", 9)
    graph.add_edge("1", "6", 14)
    graph.add_edge("2", "3", 10)
    graph.add_edge("2", "4", 15)
    graph.add_edge("3", "4", 11)
    graph.add_edge("3", "6", 2)
    graph.add_edge("4", "5", 6)
    graph.add_edge("6", "5", 9)

    start_node = "1"
    goal_node = "5"

    ucs_path, ucs_cost = ucs(graph.graph, start_node, goal_node)

    print("UCS Path:", ucs_path, "UCS Cost:", ucs_cost)
