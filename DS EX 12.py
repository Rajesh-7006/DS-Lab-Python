import sys

def dijkstra(graph, src, dest):
    n = len(graph)
    visited = [False] * n
    distance = [sys.maxsize] * n
    parent = [-1] * n
    distance[src] = 0
    
    for _ in range(n):
        # Find the unvisited node with the smallest distance
        min_dist = sys.maxsize
        min_index = -1
        for i in range(n):
            if not visited[i] and distance[i] < min_dist:
                min_dist = distance[i]
                min_index = i
        
        if min_index == -1:
            break  # Remaining nodes are inaccessible
        
        visited[min_index] = True
        
        # Update distances of neighbors
        for j in range(n):
            if graph[min_index][j] > 0 and not visited[j]:
                new_dist = distance[min_index] + graph[min_index][j]
                if new_dist < distance[j]:
                    distance[j] = new_dist
                    parent[j] = min_index
    
    # Reconstruct the shortest path
    path = []
    current = dest
    while current != -1:
        path.insert(0, current)
        current = parent[current]
    
    return distance[dest], path

# --- Main Program ---
n = int(input("Enter number of cities: "))
print("Enter adjacency matrix (0 if no direct path):")
graph = [list(map(int, input().split())) for _ in range(n)]

src = int(input("Enter source city (0 to n-1): "))
dest = int(input("Enter destination city (0 to n-1): "))

distance, path = dijkstra(graph, src, dest)

if distance == sys.maxsize:
    print(f"No path exists from city {src} to city {dest}.")
else:
    print(f"\nShortest distance from city {src} to city {dest} is: {distance}")
    print("Shortest path:", " -> ".join(map(str, path)))
