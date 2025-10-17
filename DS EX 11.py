from collections import deque

def create_adjacency_matrix(n, connections):
    matrix = [[0] * n for _ in range(n)]
    for u, v in connections:
        matrix[u][v] = 1
        matrix[v][u] = 1  # Undirected friendship
    return matrix

def create_adjacency_list(n, connections):
    adj_list = {i: [] for i in range(n)}
    for u, v in connections:
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list

def display_matrix(matrix):
    print("\nAdjacency Matrix Representation:")
    print(" ", end=" ")
    for i in range(len(matrix)):
        print(i, end=" ")
    print("\n" + "-" * (3 + 2 * len(matrix)))
    for i, row in enumerate(matrix):
        print(i, "|", " ".join(map(str, row)))

def display_list(adj_list):
    print("\nAdjacency List Representation:")
    for user, friends in adj_list.items():
        print(f"{user}: {friends}")

def check_connection_matrix(matrix, user1, user2):
    return matrix[user1][user2] == 1

def check_connection_list(adj_list, user1, user2):
    return user2 in adj_list[user1]

print("=== Social Network Representation ===")
n = int(input("Enter total number of users: "))
connections = []
m = int(input("Enter number of connections (friendships): "))
for _ in range(m):
    u, v = map(int, input("Enter connection (u v): ").split())
    connections.append((u, v))

adj_matrix = create_adjacency_matrix(n, connections)
adj_list = create_adjacency_list(n, connections)

display_matrix(adj_matrix)
display_list(adj_list)

print("\n=== Check if two users are directly connected ===")
user1, user2 = map(int, input("Enter two user IDs: ").split())
if check_connection_matrix(adj_matrix, user1, user2):
    print(f"Users {user1} and {user2} are directly connected (Matrix).")
else:
    print(f"Users {user1} and {user2} are NOT directly connected (Matrix).")

if check_connection_list(adj_list, user1, user2):
    print(f"Users {user1} and {user2} are directly connected (List).")
else:
    print(f"Users {user1} and {user2} are NOT directly connected (List).")


# BFS and DFS implementations

def bfs(graph, start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
    return visited

def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)
    return visited

print("\n=== GRAPH TRAVERSAL USING BFS AND DFS ===")
n = int(input("Enter number of vertices: "))
graph = {}
print("Enter adjacency list (space-separated neighbors):")
for i in range(1, n + 1):
    neighbors = list(map(int, input(f"Neighbors of vertex {i}: ").split()))
    graph[i] = neighbors

start_node = int(input("Enter the starting vertex: "))

bfs_result = bfs(graph, start_node)
dfs_result = dfs(graph, start_node)

print("\nBreadth-First Traversal:", bfs_result)
print("Depth-First Traversal:", dfs_result)
