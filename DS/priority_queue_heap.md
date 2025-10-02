
# 📚 Priority Queue / Heap in Python

## 1. Concept of Priority Queue
- **Definition:** A Priority Queue is a data structure where each element has a **priority**.  
- Elements with **higher priority** are removed before elements with lower priority.  
- If two elements have the same priority, they are served in the order they were added (depending on implementation).  

**Analogy:** Think of a hospital emergency room: patients with more critical conditions are treated before less critical ones, regardless of arrival order.

---

## 2. Priority Queue Using `queue.PriorityQueue`
Python provides a thread-safe priority queue in the `queue` module.

```python
from queue import PriorityQueue

pq = PriorityQueue()

# Insert elements (priority, value)
pq.put((2, "Task 2"))
pq.put((1, "Task 1"))
pq.put((3, "Task 3"))

# Remove elements (lowest priority number first)
print(pq.get())  # (1, 'Task 1')
print(pq.get())  # (2, 'Task 2')
print(pq.get())  # (3, 'Task 3')
```

✅ Lowest priority number comes out first (like min-heap).  

---

## 3. Priority Queue Using `heapq`
`heapq` is a built-in library that provides a **min-heap** implementation.  
- Smallest element has the highest priority.  

```python
import heapq

# Create an empty list to use as heap
heap = []

# Push elements
heapq.heappush(heap, (2, "Task 2"))
heapq.heappush(heap, (1, "Task 1"))
heapq.heappush(heap, (3, "Task 3"))

print("Heap:", heap)

# Pop elements (always smallest priority number first)
print(heapq.heappop(heap))  # (1, 'Task 1')
print(heapq.heappop(heap))  # (2, 'Task 2')
print(heapq.heappop(heap))  # (3, 'Task 3')
```

✅ Efficient for maintaining a dynamic set of priorities.  

---

## 4. Max-Heap Using `heapq`
By default, `heapq` is a min-heap. For max-heap behavior, store negative priorities.

```python
import heapq

max_heap = []
heapq.heappush(max_heap, (-1, "Task 1"))
heapq.heappush(max_heap, (-3, "Task 3"))
heapq.heappush(max_heap, (-2, "Task 2"))

print("Max-Heap:", max_heap)

# Pop elements (highest priority first)
print(heapq.heappop(max_heap))  # (-3, 'Task 3')
print(heapq.heappop(max_heap))  # (-2, 'Task 2')
print(heapq.heappop(max_heap))  # (-1, 'Task 1')
```

---

## 5. Comparison Table

| Method                 | Library       | Pros                                | Cons                          |
|-------------------------|--------------|------------------------------------|-------------------------------|
| `queue.PriorityQueue`  | queue        | Thread-safe, easy to use            | Slower due to locking         |
| `heapq` (min-heap)     | heapq        | Fast, efficient, flexible           | Not thread-safe, low-level    |
| `heapq` (max-heap)     | heapq        | Max-heap simulated with negatives   | Slightly less readable        |

---

## ✅ Key Takeaways
- Use **`heapq`** for efficient heap/priority queue in single-threaded programs.  
- Use **`queue.PriorityQueue`** for multithreaded/thread-safe applications.  
- Min-heap is default in Python; use **negative values** for max-heap.  
