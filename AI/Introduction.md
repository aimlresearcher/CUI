# Week 1 – Fundamentals of Artificial Intelligence  

## CSC462 – Artificial Intelligence  

---

## 🔹 What is Artificial Intelligence?
- AI is the study of making machines **think and act intelligently**.  
- Four approaches:  
  - **Thinking Humanly**  
  - **Acting Humanly**  
  - **Thinking Rationally**  
  - **Acting Rationally**  
- AI aims to **mimic human intelligence** and decision-making.  

---

## 🔹 Weak AI vs Strong AI
- **Weak AI:** Focused on solving specific tasks (e.g., Chess AI, Siri).  
- **Strong AI:** Hypothetical; capable of **general intelligence** like humans.  
- Today’s AI is **mostly Weak AI**.  

---

## 🔹 AI Perspectives
- **Thinking Humanly:** Cognitive modeling.  
- **Acting Humanly:** Turing Test approach.  
- **Thinking Rationally:** Logic-based reasoning.  
- **Acting Rationally:** Rational agents maximizing performance.  

---

## 🔹 Applications of AI
- **Healthcare** – diagnosis, drug discovery  
- **Finance** – fraud detection, trading  
- **Transportation** – self-driving cars  
- **Education** – tutoring systems  
- **Entertainment** – recommendation systems  

---

## 🔹 Challenges & Ethics in AI
- Ambiguity and uncertainty in real-world data  
- Bias in algorithms  
- Transparency and explainability  
- Automation and job loss  
- Security and misuse of AI  

---

## 🔹 Why Study AI?
- Automates tedious tasks  
- Solves complex real-world problems  
- Enhances human decision-making  
- Pushes the boundaries of technology  
- Essential foundation for **future computing**  

---

# Week 2 – Intelligent Agents & Environments  
CSC462 – Artificial Intelligence  

---

## 🔹 What is an Agent?  
- An **agent** perceives its **environment** through sensors and acts through **actuators**.  
- Core cycle: **Perception → Decision → Action**  

---

## 🔹 Examples of Agents  
- 🤖 **Robot vacuum cleaner**  
  - Sensors: dirt detector  
  - Actuators: wheels  

- 💬 **Chatbot**  
  - Sensors: user input  
  - Actuators: text reply  

---

## 🔹 PEAS Model  
To describe an agent:  
- **P** – Performance measure  
- **E** – Environment  
- **A** – Actuators  
- **S** – Sensors  

---

## 🔹 Types of Environments (1/3)  
- **Observable vs. Partially Observable**  
  - Fully observable: chess  
  - Partially observable: poker  

- **Deterministic vs. Stochastic**  
  - Deterministic: tic-tac-toe  
  - Stochastic: weather  

---

## 🔹 Types of Environments (2/3)  
- **Episodic vs. Sequential**  
  - Episodic: spam filtering  
  - Sequential: chess  

- **Static vs. Dynamic**  
  - Static: crossword puzzle  
  - Dynamic: driving  

---

## 🔹 Types of Environments (3/3)  
- **Discrete vs. Continuous**  
  - Discrete: board games  
  - Continuous: self-driving cars  

- **Single-Agent vs. Multi-Agent**  
  - Single: crossword solver  
  - Multi: football match  

- **Simple vs. Complex**  
  - Simple: tic-tac-toe  
  - Complex: stock market  

---

## 🔹 Task Environment  
- Defined by a combination of properties:  
  - observable, deterministic, episodic, etc.  
- Determines **agent design complexity**  

---

## 🔹 Rational Agent  
- A **rational agent** chooses the **best possible action** to maximize performance.  

---

## 🔹 Why Study Environments?  
- Helps design the **right type of agent** for the right problem.  

---


# Week 3 – Types of Agents  
CSC462 – Artificial Intelligence  

---

## 🔹 Simple Reflex Agents  
- Act only on **current perception** (no memory).  
- **Example:** Thermostat (turns on heater if temp < 20°C).  

**Limitations:**  
- Work well only in simple, fully observable environments.  
- Fail in complex or partially observable worlds.  

---

## 🔹 Model-Based Reflex Agents  
- Maintain an **internal model** of the world.  
- Handle **partial observability**.  

**Example:** Self-driving car tracking nearby vehicles.  

---

## 🔹 Goal-Based Agents  
- Choose actions to achieve **specific goals**.  
- **Example:** GPS navigation planning a route.  

**Advantage:** More flexible (long-term planning).  

---

## 🔹 Utility-Based Agents  
- Use a **utility function** to evaluate states.  
- **f(state) → real number** (higher = better).  
- **Example:** Delivery robot choosing between shortest vs safest path.  

**Advantage:** Balances multiple goals.  

---

## 🔹 Learning Agents  
- Improve performance with **experience + feedback**.  
- **Example:** Spam filters adapting to new spam patterns.  

**Components:**  
1. Learning element  
2. Performance element  
3. Critic (feedback)  
4. Problem generator (exploration)  

---

## 🔹 Hierarchy of Agents  
Reflex < Model-Based < Goal-Based < Utility-Based < Learning  

---

## 🔹 Rationality in Agents  
- Each agent type can be **rational** if matched with the right environment.  

---

## 🔹 Trade-offs  
- Reflex → simple, but inflexible  
- Goal-based → flexible, but computationally heavy  
- Utility-based → smarter, but needs utility definition  

---

## 🔹 Real-World Example: Self-Driving Car  
Combines multiple agent types:  
- Reflex → emergency braking  
- Model-based → track cars  
- Goal-based → reach destination  
- Utility-based → balance speed & safety  
- Learning → adapt to driver behavior  

---

## 🔹 Key Takeaway  
👉 Choosing the right type of agent depends on:  
- Environment complexity  
- Uncertainty  
- Agent’s goals  

---

---

# Week 4 – Search Concepts & BFS  
CSC462 – Artificial Intelligence  

---

## 🔹 Problem-Solving in AI  
- Many AI tasks can be seen as **search problems**.  
- Goal: find a path from **start state → goal state**.  

---

## 🔹 Problem Formulation  
Define a problem in terms of:  
- Initial state  
- Actions available  
- Transition model (results of actions)  
- Goal test (check if solved)  
- Path cost (evaluate solution)  

---

## 🔹 Search Space  
- Set of all possible states reachable from initial state.  

## 🔹 Search Algorithm  
- Explores the search space to find a solution path.  

---

## 🔹 Types of Search  
- **Uninformed Search** → blind search (BFS, DFS, Uniform Cost)  
- **Informed Search** → uses heuristics (A*, Greedy Best-First)  

---

# Breadth-First Search (BFS)  

---

## 🔹 BFS Concept  
- Explores all nodes at one depth before moving to the next.  

## 🔹 Implementation  
- Uses a **queue (FIFO)** to expand nodes in order.  

---

## 🔹 BFS Properties  
- **Completeness:** Guaranteed to find solution if one exists.  
- **Optimality:** Finds shortest path (if all costs equal).  

---

## 🔹 BFS Complexity  
- **Time Complexity:** O(b^d)  
  - b = branching factor  
  - d = depth of shallowest solution  

- **Space Complexity:** O(b^d)  
  - must store all nodes at current depth  

---

## 🔹 BFS – Advantages  
- Finds shortest solution path  
- Simple to implement  

## 🔹 BFS – Disadvantages  
- High memory usage for large search spaces  
- Slow if solution is deep  

---

# ✅ Key Point  
BFS is **complete & optimal** (when costs are equal) but requires **huge memory** for deep searches.  
