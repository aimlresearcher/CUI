
# 📚 Linked List in Python (Singly, Doubly, Circular)

## 1. Concept of Linked List
- **Definition:** A Linked List is a linear data structure where elements (nodes) are connected using **pointers/references**.  
- Each node typically contains:
  - **Data**
  - **Pointer (reference) to the next node**  

**Types of Linked List:**
1. **Singly Linked List** → Each node points to the next node.  
2. **Doubly Linked List** → Each node points to both next and previous nodes.  
3. **Circular Linked List** → Last node connects back to the first node.  

---

## 2. Singly Linked List Example

```python
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Usage
sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.display()   # 10 -> 20 -> 30 -> None
```

---

## 3. Doubly Linked List Example

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.display()  # 1 <-> 2 <-> 3 <-> None
```

---

## 4. Circular Linked List Example

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def display(self, count=10):
        current = self.head
        c = 0
        while current and c < count:  # limit to avoid infinite loop
            print(current.data, end=" -> ")
            current = current.next
            c += 1
        print("... (circular)")

cll = CircularLinkedList()
cll.append("A")
cll.append("B")
cll.append("C")
cll.display()  # A -> B -> C -> A -> ...
```

---

## 5. Comparison Table

| Type                 | Structure                         | Pros                                   | Cons                        |
|----------------------|-----------------------------------|----------------------------------------|-----------------------------|
| Singly Linked List   | Node → Next                       | Simple, uses less memory                | Cannot traverse backward    |
| Doubly Linked List   | Node → Prev & Next                | Can traverse both directions            | Uses extra memory for `prev`|
| Circular Linked List | Last node points back to first    | Efficient for circular data structures  | More complex implementation |

---

## ✅ Key Takeaways
- **Singly Linked List:** Good for simple sequential traversal.  
- **Doubly Linked List:** Useful when traversal in both directions is needed.  
- **Circular Linked List:** Ideal for scenarios like **round-robin scheduling**.  
