import heapq

def dijkstra(N, edges, start, end):
    graph = {i: [] for i in range(1, N + 1)}
    for s, d, v in edges:
        graph[s].append((v, d))
        graph[d].append((v, s))
    
    pq = [(0, start, [start])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)
        
        if node in visited:
            continue

        visited.add(node)

        if node == end:
            return path

        for next_cost, neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (cost + next_cost, neighbor, path + [neighbor]))

    return []

def main():
    # Read the number of nodes and edges
    N, E = map(int, input("Enter number of nodes and edges: ").split())

    edges = []
    for _ in range(E):
        s, d, v = map(int, input("Enter edge (start, end, value): ").split())
        edges.append((s, d, v))

    start_node = int(input("Enter the start node: "))
    end_node = int(input("Enter the end node: "))

    path = dijkstra(N, edges, start_node, end_node)

    if path:
        print("Shortest path:", ' '.join(map(str, path)))
    else:
        print("No path found between nodes", start_node, "and", end_node)

if __name__ == "__main__":
    main()
