# 📚 Stack Data Structure (Using Python Libraries)

## 1. Concept of Stack

**Definition:** A Stack follows **LIFO (Last In First Out)**.

**Analogy:** Think of a stack of plates:  
The last plate you put on top is the first one you take off.

---

## 2. Stack Using `list`

Although list is not the best for stacks (because `insert(0, x)` is slow), it is often used for simple examples.

```python
stack = []       # create empty stack

# Push elements (append at end)
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)   # [10, 20, 30]

# Pop element (remove last)
print("Popped:", stack.pop())  # 30
print("Stack after pop:", stack)  # [10, 20]
```

✅ Easy, but not efficient if we manipulate from the front.

---

## 3. Stack Using `collections.deque`

`deque` (double-ended queue) is optimized for fast append/pop operations from both ends.  
This is the recommended way.

```python
from collections import deque

stack = deque()

# Push elements
stack.append("A")
stack.append("B")
stack.append("C")

print("Stack:", stack)   # deque(['A', 'B', 'C'])

# Pop elements
print("Popped:", stack.pop())  # C
print("Stack after pop:", stack)  # deque(['A', 'B'])
```

✅ Much faster and memory-efficient than using lists.

---

## 4. Stack Using `queue.LifoQueue`

The `queue` library gives a thread-safe stack (useful in multithreading).

```python
from queue import LifoQueue

# Create stack with max size 3
stack = LifoQueue(maxsize=3)

# Push elements
stack.put(1)
stack.put(2)
stack.put(3)

print("Is stack full?", stack.full())  # True

# Pop elements
print("Popped:", stack.get())   # 3
print("Popped:", stack.get())   # 2
print("Is stack empty?", stack.empty())  # False
```

✅ Used in concurrent programming (safe for multiple threads).

---

## 5. Comparison Table

| Method              | Library        | Pros                          | Cons                          |
|---------------------|----------------|-------------------------------|-------------------------------|
| `list`              | Built-in       | Simple, easy to use           | Slower for large operations   |
| `collections.deque` | collections    | Fast, efficient for push/pop  | Not thread-safe               |
| `queue.LifoQueue`   | queue          | Thread-safe, good for concurrency | Slightly slower due to locking |

---

## 🔑 Key Takeaway

- For **general stack use** → `deque` is best.  
- For **multithreaded applications** → use `LifoQueue`.  
- For **learning basics** → `list` is fine.  
