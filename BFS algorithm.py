from collections import deque

def bfs(graph, start, end):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current == end:
            return path + [current]

        if current in visited:
            continue
        visited.add(current)

        if isinstance(graph, dict):
            neighbors = graph.get(current, set())
        elif isinstance(graph, list):
            row, col = current
            neighbors = []
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < len(graph) and 0 <= new_col < len(graph[0]) and graph[new_row][new_col] != '#':
                    neighbors.append((new_row, new_col))

        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append((neighbor, path + [current]))

    return None


def bfs_grid(maze, start, end):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current == end:
            return path + [current]

        if current in visited:
            continue
        visited.add(current)

        row, col = current
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] != '#':
                neighbor = (new_row, new_col)
                if neighbor not in visited:
                    queue.append((neighbor, path + [current]))

    return None

# Contoh peta yang diakses dengan bfs
peta = {
    'S': set(['A', 'B', 'D', 'E']), 
    'A': set(['S']), 
    'B': set(['C', 'D', 'S']), 
    'C': set(['B', 'J']), 
    'D': set(['B', 'G', 'S']), 
    'E': set(['G', 'S']), 
    'F': set(['G', 'H']), 
    'G': set(['D', 'E', 'F', 'H', 'J']), 
    'H': set(['F', 'G', 'I']), 
    'I': set(['H', 'J']), 
    'J': set(['C', 'G', 'I']),  
}

# Membaca labirin dari file eksternal
file_labirin = 'peta.txt'

try:
    with open(file_labirin, 'r') as file:
        lines = file.readlines()
        maze = [list(line.strip()) for line in lines]
except FileNotFoundError:
    print("File labirin tidak ditemukan.")
    maze = None

def find_path(graph, start, goal):
    path = bfs(graph, start, goal)
    return path

def find_path_maze(maze, start, goal):
    path = bfs_grid(maze, start, goal)
    return path

# Pencarian jalur di peta dengan BFS
start_node = 'S'
goal_node = 'I'

path = find_path(peta, start_node, goal_node)

if path:
    print("Jalur ditemukan di peta:", ' -> '.join(path))
else:
    print("Tidak ada jalur yang tersedia di peta.")


# Pencarian jalur di labirin dengan BFS
titik_awal = None
titik_akhir = None

if maze:
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                titik_awal = (i, j)
            elif maze[i][j] == 'E':
                titik_akhir = (i, j)

    if titik_awal and titik_akhir:
        jalur = find_path_maze(maze, titik_awal, titik_akhir)
        if jalur:
            print("\nJalur ditemukan di dalam labirin:")
            for i in range(1, len(jalur)):
                row, col = jalur[i]
                # Menandai jalur yang dilalui dengan karakter '+'
                maze[row][col] = '+'

            # Menampilkan labirin dengan jalur yang ditandai
            for baris in maze:
                print(''.join(baris))
        else:
            print("Tidak ditemukan jalur di dalam labirin.")
    else:
        print("Titik awal (S) atau titik akhir (E) tidak ditemukan di dalam labirin.")
