
# 📚 Hash Table in Python (dict)

## 1. Concept of Hash Table
- **Definition:** A Hash Table is a data structure that stores data in **key-value pairs**.  
- It uses a **hashing function** to map keys to an index in an array (bucket).  
- In Python, the built-in **`dict`** type is implemented as a hash table.  

**Analogy:** Think of a library catalog where you can quickly find a book by its unique ID rather than searching all books one by one.

---

## 2. Hash Table Using `dict`
```python
# Creating a hash table (dictionary)
student = {
    "name": "Ali",
    "age": 21,
    "roll_no": "BCS123"
}

# Accessing values
print(student["name"])   # Ali

# Inserting a new key-value pair
student["grade"] = "A"

# Updating a value
student["age"] = 22

# Deleting a key-value pair
del student["roll_no"]

print(student)  # {'name': 'Ali', 'age': 22, 'grade': 'A'}
```

✅ Dictionary operations like insert, delete, lookup are **O(1)** on average.

---

## 3. Handling Collisions
- Python handles collisions internally using techniques like **open addressing** and **hash randomization**.  
- As users, we don’t need to manually handle collisions when using `dict`.  

---

## 4. Using `hash()` Function
The `hash()` function gives the hash value of immutable objects.

```python
print(hash("apple"))   # e.g., 453192765187
print(hash(12345))     # e.g., 12345
```

⚠️ Note: Mutable objects (like lists, dicts) cannot be hashed, but immutable ones (str, int, tuple) can.

---

## 5. Real-World Applications of Hash Tables
- **Databases:** Indexing records by unique keys.  
- **Compilers:** Symbol tables for variables/functions.  
- **Caching:** Quick lookup of previously computed results.  
- **Counting/Frequency tables:** Using `dict` or `collections.Counter`.  

```python
from collections import Counter

data = ["apple", "banana", "apple", "orange", "banana"]
freq = Counter(data)
print(freq)  # Counter({'apple': 2, 'banana': 2, 'orange': 1})
```

---

## 6. Comparison Table

| Structure   | Lookup Time | Insertion | Deletion | Ordered? |
|-------------|-------------|-----------|----------|----------|
| List        | O(n)        | O(1)      | O(n)     | Yes      |
| Set         | O(1)        | O(1)      | O(1)     | No       |
| Dict (Hash) | O(1)        | O(1)      | O(1)     | Python 3.7+: Yes |

---

## ✅ Key Takeaways
- Python’s `dict` is a powerful and optimized **hash table**.  
- Provides **constant-time access** on average.  
- Supports insertion, deletion, and update in **O(1)**.  
- Ideal for **fast lookups, caching, and frequency counting**.  
