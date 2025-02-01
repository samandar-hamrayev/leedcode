import heapq

def dijkstra(graph, start):
    # Boshlang'ich tugundan masofalarni saqlash uchun dictionary
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Priority queue (heap) ishga tushirish
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Katta masofalar uchun davom etmaslik
        if current_distance > distances[current_vertex]:
            continue

        # Qo'shni tugunlarni ko'rib chiqish
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Yangi eng qisqa yo'l topilgan bo'lsa
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Misol grafik
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1},
}

# 'A' tugundan barcha tugunlarga eng qisqa yo'llar
print(dijkstra(graph, 'A'))  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}