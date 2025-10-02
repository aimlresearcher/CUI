
# 📚 Deque (Double-Ended Queue) in Python

## 1. Concept of Deque
- **Definition:** A Deque (pronounced "deck") is a double-ended queue that allows insertion and removal of elements from both ends.  
- **Analogy:** Think of a line of people where new people can join from **front** or **back**, and leave from **front** or **back**.  

---

## 2. Deque Using `collections.deque`
The `deque` class from the `collections` module is the most efficient way to implement a deque in Python.

```python
from collections import deque

# Create an empty deque
dq = deque()

# Insert at rear (append)
dq.append(10)
dq.append(20)
dq.append(30)
print("Deque after append:", dq)   # deque([10, 20, 30])

# Insert at front (appendleft)
dq.appendleft(5)
print("Deque after appendleft:", dq)  # deque([5, 10, 20, 30])

# Remove from rear (pop)
print("Removed from rear:", dq.pop())  # 30
print("Deque now:", dq)  # deque([5, 10, 20])

# Remove from front (popleft)
print("Removed from front:", dq.popleft())  # 5
print("Deque now:", dq)  # deque([10, 20])
```

✅ Deque supports both stack and queue operations efficiently in **O(1)** time.  

---

## 3. Deque Using `queue` Module
Python also provides `queue.deque` via `multiprocessing`, but in practice, `collections.deque` is preferred because it is simpler and faster.  

---

## 4. Real-World Applications of Deque
- Implementing both **stack and queue** with one structure  
- **Sliding window problems** (like maximum in every window of size k)  
- **Palindrome checking** (compare front and rear)  
- Task scheduling systems  

---

## 5. Comparison with Other Structures

| Structure            | Access Ends | Middle Access | Efficiency |
|-----------------------|-------------|---------------|------------|
| Stack (`list/deque`) | One end     | Not efficient | Fast O(1)  |
| Queue (`deque/Queue`) | Opposite ends | Not efficient | Fast O(1)  |
| Deque (`deque`)      | Both ends   | Not efficient | Fast O(1)  |

---

## ✅ Key Takeaways
- Use `collections.deque` for efficient double-ended operations.  
- Supports both **stack** and **queue** behaviors.  
- Ideal for **palindrome checking, sliding windows, and task schedulers**.  
