
# 📚 Trees in Python (Binary Tree, BST, AVL Tree, Heap, Trie, Segment Tree)

## 1. Concept of Tree
- **Definition:** A Tree is a hierarchical data structure consisting of nodes, with a single root node and sub-nodes (children).  
- **Applications:** File systems, Databases, Indexing, Parsers, Memory management.

---

## 2. Binary Tree
Each node has at most **two children** (left and right).

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Example tree
root = Node(10)
root.left = Node(20)
root.right = Node(30)

print(root.data)       # 10
print(root.left.data)  # 20
print(root.right.data) # 30
```

---

## 3. Binary Search Tree (BST)
- Left child < Root < Right child  
- Used for fast searching (O(log n) on average).

```python
class BST:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def insert(self, root, data):
        if root is None:
            return self.Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

bst = BST()
root = None
for val in [50, 30, 70, 20, 40, 60, 80]:
    root = bst.insert(root, val)

bst.inorder(root)  # 20 30 40 50 60 70 80
```

---

## 4. AVL Tree (Self-Balancing BST)
- Ensures tree height difference (balance factor) is ≤ 1.  
- Rotations (LL, RR, LR, RL) keep tree balanced.  

(Pseudocode/Conceptual only – full implementation is long.)

```python
# AVL Tree ensures O(log n) insert, delete, search
# Example applications: Databases, memory indexing.
```

---

## 5. Heap (Binary Heap)
- **Complete binary tree**.  
- Min-Heap: Parent ≤ Children.  
- Max-Heap: Parent ≥ Children.  

```python
import heapq

# Min-Heap
heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)

print(heapq.heappop(heap))  # 5 (smallest element)

# Max-Heap (use negative values)
max_heap = []
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -20)

print(-heapq.heappop(max_heap))  # 20 (largest element)
```

---

## 6. Trie (Prefix Tree)
- Used for string storage and prefix searching (like autocomplete).

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word

trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  # True
print(trie.search("app"))    # False
```

---

## 7. Segment Tree
- Tree structure for **range queries** (like sum/min/max over subarrays).  
- Used in competitive programming.

```python
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        self.build(arr)

    def build(self, arr):
        # Insert leaf nodes
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        # Build tree by calculating parents
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def query(self, l, r):
        res = 0
        l += self.n
        r += self.n
        while l < r:
            if l % 2:
                res += self.tree[l]
                l += 1
            if r % 2:
                r -= 1
                res += self.tree[r]
            l //= 2
            r //= 2
        return res

arr = [1, 3, 5, 7, 9, 11]
st = SegmentTree(arr)
print(st.query(1, 4))  # Sum of [3,5,7] = 15
```

---

## 8. Comparison Table

| Tree Type         | Key Feature                         | Use Case                              |
|-------------------|--------------------------------------|---------------------------------------|
| Binary Tree       | Each node has ≤2 children           | Basic hierarchical data               |
| BST               | Left<Root<Right                     | Fast search, sorted data              |
| AVL Tree          | Self-balancing BST                  | Databases, indexing                   |
| Heap              | Complete tree, min/max property     | Priority queues, scheduling           |
| Trie              | Prefix-based string tree            | Autocomplete, dictionary search       |
| Segment Tree      | Range query structure               | Competitive programming, queries      |

---

## ✅ Key Takeaways
- **Binary Tree** is the foundation.  
- **BST** allows ordered searching.  
- **AVL Tree** ensures balance for efficiency.  
- **Heap** is great for priority-based tasks.  
- **Trie** is ideal for strings and prefixes.  
- **Segment Tree** excels in range queries.  
