
# 📚 Queue Data Structure in Python (Using Libraries)

## 1. Concept of Queue
- **Definition:** A Queue follows **FIFO** (First In First Out).  
- **Analogy:** Think of people standing in a line:  
  - The first person in the line is served first.  

---

## 2. Queue Using `list`
Using `list` is possible but not efficient, because `pop(0)` is **O(n)**.

```python
queue = []

# Enqueue (append at end)
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)   # [10, 20, 30]

# Dequeue (remove first element)
print("Dequeued:", queue.pop(0))  # 10
print("Queue after dequeue:", queue)  # [20, 30]
```

---

## 3. Queue Using `collections.deque`
Best and most efficient way to implement queues in Python.

```python
from collections import deque

queue = deque()

# Enqueue
queue.append("A")
queue.append("B")
queue.append("C")

print("Queue:", queue)   # deque(['A', 'B', 'C'])

# Dequeue
print("Dequeued:", queue.popleft())  # A
print("Queue after dequeue:", queue)  # deque(['B', 'C'])
```

✅ Fast enqueue and dequeue at both ends.  

---

## 4. Queue Using `queue.Queue`
The `queue.Queue` class is **thread-safe** and designed for multithreading.

```python
from queue import Queue

# Create queue with max size
q = Queue(maxsize=3)

# Enqueue
q.put(1)
q.put(2)
q.put(3)

print("Is queue full?", q.full())  # True

# Dequeue
print("Dequeued:", q.get())  # 1
print("Dequeued:", q.get())  # 2
print("Is queue empty?", q.empty())  # False
```

✅ Used in producer-consumer problems and multithreading.

---

## 5. Comparison Table

| Method               | Library       | Pros                                | Cons                        |
|-----------------------|--------------|------------------------------------|-----------------------------|
| `list`               | Built-in     | Simple, easy to understand          | Slow (`O(n)`) for dequeue   |
| `collections.deque`  | collections  | Fast `O(1)` enqueue/dequeue         | Not thread-safe             |
| `queue.Queue`        | queue        | Thread-safe, good for concurrency   | Slightly slower due to locks|

---

## ✅ Key Takeaways
- For **simple use** → use `deque`.  
- For **threading/multithreading** → use `queue.Queue`.  
- For **learning basics** → `list` is fine but inefficient.  
