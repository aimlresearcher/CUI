
# 📚 Graphs in Python (Adjacency List & Adjacency Matrix)

## 1. Concept of Graph
- **Definition:** A Graph is a collection of **nodes (vertices)** connected by **edges**.  
- Can be **directed** or **undirected**, **weighted** or **unweighted**.  

**Applications:** Social networks, Maps/Navigation, Computer Networks, Recommendation systems.

---

## 2. Graph Representation Methods

### (a) Adjacency List
- Each vertex stores a list of its neighbors.  
- Efficient in terms of space, especially for sparse graphs.  

```python
# Graph using adjacency list
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

# Traversal example
for node, neighbors in graph.items():
    print(node, "->", neighbors)
```
**Output:**
```
A -> ['B', 'C']
B -> ['A', 'D']
C -> ['A', 'D']
D -> ['B', 'C']
```

---

### (b) Adjacency Matrix
- A 2D matrix (list of lists) where each cell `[i][j]` indicates presence (and weight) of edge.  
- Efficient for dense graphs, but uses more memory.  

```python
# Graph vertices
vertices = ["A", "B", "C", "D"]
n = len(vertices)

# Initialize adjacency matrix (0 = no edge)
adj_matrix = [[0]*n for _ in range(n)]

# Add edges (undirected)
edges = [("A","B"), ("A","C"), ("B","D"), ("C","D")]

for u, v in edges:
    i, j = vertices.index(u), vertices.index(v)
    adj_matrix[i][j] = 1
    adj_matrix[j][i] = 1  # undirected

# Print matrix
print("Adjacency Matrix:")
for row in adj_matrix:
    print(row)
```
**Output:**
```
[0, 1, 1, 0]
[1, 0, 0, 1]
[1, 0, 0, 1]
[0, 1, 1, 0]
```

---

## 3. Weighted Graph Example (Adjacency List)
```python
# Weighted Graph using adjacency list
weighted_graph = {
    "A": [("B", 5), ("C", 2)],
    "B": [("A", 5), ("D", 4)],
    "C": [("A", 2), ("D", 7)],
    "D": [("B", 4), ("C", 7)]
}

# Traversal
for node, neighbors in weighted_graph.items():
    print(node, "->", neighbors)
```
**Output:**
```
A -> [('B', 5), ('C', 2)]
B -> [('A', 5), ('D', 4)]
C -> [('A', 2), ('D', 7)]
D -> [('B', 4), ('C', 7)]
```

---

## 4. Comparison Table

| Representation     | Space Complexity | Edge Lookup | Best For         |
|--------------------|------------------|-------------|------------------|
| Adjacency List     | O(V + E)         | O(V)        | Sparse graphs    |
| Adjacency Matrix   | O(V^2)           | O(1)        | Dense graphs     |

---

## ✅ Key Takeaways
- **Adjacency List:** Saves space for sparse graphs, widely used.  
- **Adjacency Matrix:** Easy edge lookup, good for dense graphs.  
- Graphs can be **directed/undirected** and **weighted/unweighted** depending on the problem.  
