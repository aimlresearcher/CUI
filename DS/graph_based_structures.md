
# 📚 Graph-based Structures in Python (DAGs, Social Network Graphs, etc.)

## 1. Concept of Graph-based Structures
Graph-based structures extend basic graphs to model more **specialized relationships**.  
Common types include:
- **Directed Acyclic Graphs (DAGs)** → No cycles, often used in scheduling.  
- **Social Network Graphs** → Represent people as nodes and relationships as edges.  
- **Weighted/Flow Graphs** → Edges carry weights or capacities.  
- **Bipartite Graphs** → Nodes divided into two sets, edges only connect across sets.  

---

## 2. Directed Acyclic Graph (DAG)
- A directed graph with **no cycles**.  
- Used in **task scheduling, dependency resolution, topological sorting**.  

```python
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.topological_sort_util(neighbor, visited, stack)
        stack.insert(0, v)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        print("Topological Sort:", stack)

g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)
g.topological_sort()  # Example output: [5, 4, 2, 3, 1, 0]
```

---

## 3. Social Network Graph
- Graph where nodes = people, edges = friendships/follows.  
- Useful for **recommendations, shortest path (friend of friend)**, influence spreading.  

```python
# Social Network Graph (Adjacency List)
social_graph = {
    "Alice": ["Bob", "Charlie"],
    "Bob": ["Alice", "David"],
    "Charlie": ["Alice", "Eve"],
    "David": ["Bob", "Eve"],
    "Eve": ["Charlie", "David"]
}

# Example: find friends of Alice
print("Friends of Alice:", social_graph["Alice"])
```

---

## 4. Weighted Graph / Flow Network
- Each edge has a weight/capacity.  
- Used in **shortest path (Dijkstra, Bellman-Ford)** or **max flow (Ford-Fulkerson)**.  

```python
import heapq

def dijkstra(graph, start):
    pq = [(0, start)]
    dist = {node: float("inf") for node in graph}
    dist[start] = 0
    while pq:
        current_dist, node = heapq.heappop(pq)
        if current_dist > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return dist

weighted_graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("C", 2), ("D", 6)],
    "C": [("D", 3)],
    "D": []
}

print(dijkstra(weighted_graph, "A"))  
# {'A': 0, 'B': 1, 'C': 3, 'D': 6}
```

---

## 5. Bipartite Graph
- Graph where vertices can be divided into two disjoint sets.  
- Used in **matching problems** (e.g., job assignment, dating apps).  

```python
# Bipartite Graph Example
U = ["u1", "u2", "u3"]
V = ["v1", "v2"]
edges = [("u1", "v1"), ("u2", "v2"), ("u3", "v1")]

bipartite_graph = {u: [] for u in U}
for u, v in edges:
    bipartite_graph[u].append(v)

print("Bipartite Graph:", bipartite_graph)
```

---

## 6. Comparison Table

| Graph Type          | Properties                    | Applications                         |
|---------------------|--------------------------------|--------------------------------------|
| DAG                 | Directed, no cycles           | Scheduling, compiler optimization    |
| Social Graph        | People & relationships        | Social networks, recommendations     |
| Weighted Graph      | Edges with weights            | Shortest paths, network flows        |
| Bipartite Graph     | Two disjoint sets of vertices | Matching, assignments, clustering    |

---

## ✅ Key Takeaways
- **DAGs** → great for dependencies & scheduling.  
- **Social Graphs** → used in social networks, influencer ranking.  
- **Weighted Graphs** → foundation of routing and optimization.  
- **Bipartite Graphs** → useful in real-world matching problems.  
