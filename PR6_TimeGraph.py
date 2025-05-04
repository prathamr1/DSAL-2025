import time

def graph_info_adj_list(adj_list):
    start_time = time.time()
    num_vertices = len(adj_list)
    num_edges = sum(len(neighbors) for neighbors in adj_list.values()) // 2
    end_time = time.time()
    runtime = end_time - start_time
    return num_vertices, num_edges, runtime


def graph_info_adj_matrix(adj_matrix):
    start_time = time.time()
    num_vertices = len(adj_matrix)
    num_edges = sum(sum(row) for row in adj_matrix) // 2
    end_time = time.time()
    runtime = end_time - start_time
    return num_vertices, num_edges, runtime


# Example usage for adjacency list
graph_list = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}
vertices_list, edges_list, runtime_list = graph_info_adj_list(graph_list)
print(f"Adjacency List: Vertices = {vertices_list}, Edges = {edges_list}, Runtime = {runtime_list:.6f} seconds")


# Example usage for adjacency matrix
graph_matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]
vertices_matrix, edges_matrix, runtime_matrix = graph_info_adj_matrix(graph_matrix)
print(f"Adjacency Matrix: Vertices = {vertices_matrix}, Edges = {edges_matrix}, Runtime = {runtime_matrix:.6f} seconds")
