import heapq


def dijkstra(start, end, graph):
    distances = {place: float('inf') for place in graph}
    distances[start] = 0

    priority_queue = [(start, 0)]
    prevs = {}
    while priority_queue:
        current_place, current_distance = heapq.heappop(priority_queue)

        if current_place == end:
            break

        for neighbor, weight in graph[current_place].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                prevs[neighbor] = current_place
                heapq.heappush(priority_queue, (neighbor, distance))

    path = []
    while end in prevs:
        path.append(end)
        end = prevs[end]
    path.append(end)
    path.reverse()

    return distances, path


graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'D': 4},
    'C': {'B': 3, 'E': 6, 'D': 5},
    'D': {'F': 5},
    'E': {'F': 0},
    'F': {}
}

shortest_weith, shortest_path = dijkstra('A', 'F', graph)
print(f"Eng qisqa yo'l qiymati:{shortest_weith}\n"
      f"Eng qisqa yo'l yo'nalishi:", " -> ".join(shortest_path))