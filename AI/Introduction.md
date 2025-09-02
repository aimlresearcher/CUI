# Week 1 – Fundamentals of Artificial Intelligence

## Definition of AI
The study of how to make machines think and act intelligently.

## Four Main Perspectives
- **Thinking Humanly** – Making machines simulate human thought processes (cognitive modeling).  
- **Acting Humanly** – Machines pass the Turing Test by behaving like humans.  
- **Thinking Rationally** – Machines apply logical reasoning to make correct decisions.  
- **Acting Rationally** – Machines act in ways that maximize performance (rational agents).  

## Types of AI
- **Weak AI** – Focused on solving specific tasks (e.g., chess-playing program, Alexa).  
- **Strong AI** – Hypothetical machines with general human-like intelligence.  

## AI vs Human Intelligence
- AI is faster at calculations.  
- Humans excel at creativity & common sense.  

## Applications of AI
- Healthcare (diagnosis)  
- Finance (fraud detection)  
- Transport (self-driving cars)  
- And more…  

## Branches of AI
- Search  
- Reasoning  
- Planning  
- Learning  
- Natural Language Processing (NLP)  
- Robotics  

## Importance of Rationality
Rational AI chooses the best possible action given available information.

## Challenges of AI
- Ambiguity  
- Uncertainty  
- Incomplete knowledge  
- Real-world complexity  

## Ethical Issues
- Bias in algorithms  
- Job automation  
- Decision transparency  

## Why Study AI?
To build systems that enhance human capabilities, automate tedious tasks, and solve problems beyond human ability.

----

# Week 2 – Intelligent Agents & Environments

## Definition of an Agent
An **agent** is anything that perceives its environment through **sensors** and acts upon it through **actuators**.

### Core Cycle
**Agent = Perception + Action**  
Observe → Decide → Act  

### Examples of Agents
- **Robot vacuum cleaner**  
  - Sensors: dirt detector  
  - Actuators: wheels  
- **Chatbot**  
  - Sensors: user input  
  - Actuators: text reply  

## Environment
The external world with which an agent interacts.

## PEAS Model
Describes any agent in terms of:
- **P**erformance measure  
- **E**nvironment  
- **A**ctuators  
- **S**ensors  

## Types of Environments

### 1. Observable vs. Partially Observable
- **Fully observable** – agent sees everything (e.g., chess)  
- **Partially observable** – agent sees only part (e.g., poker)  

### 2. Deterministic vs. Stochastic
- **Deterministic** – outcome of action is predictable (e.g., tic-tac-toe)  
- **Stochastic** – outcomes involve chance (e.g., weather)  

### 3. Episodic vs. Sequential
- **Episodic** – each decision is independent (e.g., spam filtering)  
- **Sequential** – current decisions affect the future (e.g., chess)  

### 4. Static vs. Dynamic
- **Static** – environment doesn’t change while agent is thinking (e.g., crossword puzzle)  
- **Dynamic** – environment keeps changing (e.g., driving)  

### 5. Discrete vs. Continuous
- **Discrete** – finite states/actions (e.g., board games)  
- **Continuous** – infinite states (e.g., self-driving cars in real world)  

### 6. Single-agent vs. Multi-agent
- **Single-agent** – operates alone (e.g., crossword solver)  
- **Multi-agent** – other agents influence outcomes (e.g., football match)  

### 7. Simple vs. Complex
- **Simple** – easy rules, predictable (e.g., tic-tac-toe)  
- **Complex** – uncertain, dynamic, multiple variables (e.g., stock market)  

## Task Environment
The combination of properties (observable, deterministic, episodic, etc.) defines the complexity of the agent’s task.

## Rational Agent
Always takes the best possible action to maximize performance.

## Goal of Studying Environments
Helps in designing the right type of agent for the right problem.

---

# Week 3 – Types of Agents

## 1. Simple Reflex Agents
- Act only on the current perception without memory of the past.  
- **Example:** A thermostat that turns on the heater if temperature < 20°C.  

### Limitations
- Work well in fully observable, simple environments.  
- Fail in complex or partially observable environments.  

---

## 2. Model-Based Reflex Agents
- Maintain an internal model of the world to handle partial observability.  
- **Example:** A self-driving car keeping track of nearby vehicles.  

---

## 3. Goal-Based Agents
- Choose actions to achieve specific goals.  
- **Example:** GPS navigation system planning a route to destination.  

### Advantages
- Provide flexibility because actions are chosen with long-term goals in mind.  

---

## 4. Utility-Based Agents
- Use a **utility function** to measure how good an outcome is, balancing multiple goals.  
- **Example:** A delivery robot choosing between shortest path and safest path.  

### Utility Function
Maps states to real numbers, helping the agent pick the “best” option among several.  

---

## 5. Learning Agents
- Improve their performance over time through feedback and experience.  
- **Example:** Spam filters that adapt as new spam patterns appear.  

### Four Components of a Learning Agent
1. **Learning element** – improves performance  
2. **Performance element** – decides actions  
3. **Critic** – provides feedback  
4. **Problem generator** – suggests new actions to explore  

---

## Hierarchy of Agents
**Reflex < Model-Based < Goal-Based < Utility-Based < Learning**  

---

## Rationality in Agents
- Each agent type can be rational if designed for the right environment.  

---

## Trade-offs
- **Reflex:** simple but inflexible.  
- **Goal-based:** flexible but computationally expensive.  
- **Utility-based:** smarter decisions but requires defining utility correctly.  

---

## Real-World Example – Self-Driving Car
Combines multiple agent types for robustness:
- **Reflex** – emergency braking  
- **Model-based** – tracking other cars  
- **Goal-based** – reaching destination  
- **Utility-based** – balancing speed vs safety  
- **Learning** – adapting to driver behavior  

---

## Agents in AI Research
Most real AI systems combine multiple agent types for robustness.  

---

## Key Takeaway
Choosing the right type of agent depends on the **complexity, uncertainty, and goals** of the environment.  

---

# Week 4 – Search Concepts & BFS

## Problem-Solving in AI
Many AI tasks can be seen as **search problems**, where the goal is to find a path from a start state to a goal state.

---

## Problem Formulation
Define a problem in terms of:
- **Initial state**  
- **Actions available**  
- **Transition model** – what happens after each action  
- **Goal test** – check if solved  
- **Path cost** – evaluate solutions  

---

## Search Space
The set of all possible states that can be reached from the initial state by applying actions.

---

## Search Algorithm
A method that explores the search space to find a solution path.

---

## Types of Search
- **Uninformed Search** – No extra knowledge, only uses problem definition.  
- **Informed Search** – Uses heuristics (extra knowledge) to guide search.  

### Examples
- **Uninformed Search** – Breadth-First Search (BFS), Depth-First Search (DFS), Uniform Cost Search.  
- **Informed Search** – A* Search, Greedy Best-First Search.  

---

## Breadth-First Search (BFS)

### Concept
Explores all nodes at one depth before moving to the next depth.

### Implementation
Uses a **queue (FIFO)** to expand nodes in order.

### Completeness
BFS is guaranteed to find a solution if one exists (because it explores level by level).

### Optimality
BFS finds the shortest path (least number of steps) **if all actions have equal cost**.

### Time Complexity
- **O(b^d)**  
where:  
- **b** = branching factor (children per node)  
- **d** = depth of shallowest solution  

### Space Complexity
- **O(b^d)** (stores all nodes at a level in memory).  

---

## Advantages of BFS
- Finds the shortest solution path.  
- Simple to implement.  

## Disadvantages of BFS
- Uses a lot of memory for large search spaces.  
- Can be slow if the solution is deep.  

---

# Week 5 – Depth-First Search (DFS) & BFS vs DFS Comparison

## Depth-First Search (DFS)

### Concept
Explores as far as possible along one branch before backtracking.

### Data Structure
Implemented using a **stack (LIFO)** or **recursion**.

### Example
Imagine a maze: DFS goes straight down one path until it hits a dead end, then backtracks.

---

### Completeness
- **Finite spaces:** Yes, DFS will eventually find a solution.  
- **Infinite spaces:** No, DFS can get stuck going infinitely deep.  

### Optimality
- DFS is **not optimal** – it may find a longer path before a shorter one.  

### Time Complexity
- **O(b^m)**  
where:  
- **b** = branching factor  
- **m** = maximum depth  

### Space Complexity
- **O(bm)** – much smaller than BFS, since it only needs to store one branch at a time.  

---

## Advantages of DFS
- Low memory usage.  
- Works well when the solution is deep.  
- Useful in topological sorting, scheduling, and path exploration.  

## Disadvantages of DFS
- May get stuck in infinite paths.  
- Does not guarantee the shortest path.  

---

# BFS vs DFS Comparison

### Completeness
- **BFS:** Always finds a solution if one exists.  
- **DFS:** Might fail in infinite search space.  

### Optimality
- **BFS:** Finds shortest path when costs are equal.  
- **DFS:** Does not guarantee shortest path.  

### Time Complexity
- **BFS:** O(b^d), where **d = shallowest solution**.  
- **DFS:** O(b^m), where **m = maximum depth**.  

### Space Complexity
- **BFS:** O(b^d) → exponential space.  
- **DFS:** O(bm) → much smaller.  

---

## When to Use BFS
Best when:
- Solution is shallow.  
- Optimal solution is required.  
- Memory is sufficient.  

## When to Use DFS
Best when:
- Search space is very large.  
- Memory is limited.  
- A quick solution (not necessarily optimal) is acceptable.  

---

# Week 6 – Informed Search

## Uninformed vs Informed Search
- **Uninformed search** – explores blindly.  
- **Informed search** – uses heuristics (extra knowledge) to guide search efficiently.  

---

## Heuristic Function (h(n))
- An estimate of the cost from a state **n** to the goal.  
- **Example:** In a map, straight-line distance is a heuristic for travel cost.  

### Properties of Good Heuristics
- Easy to compute.  
- Closer to the actual cost (more accurate).  
- Should reduce search effort.  

---

## Admissible Heuristic
- A heuristic that **never overestimates** the true cost.  
- Ensures **optimality** in algorithms like A*.  

## Consistent (Monotonic) Heuristic
- Satisfies the triangle inequality:  
  **h(n) ≤ c(n, a, n') + h(n')**  

---

# Greedy Best-First Search

### Concept
- Always expands the node that appears closest to the goal (**minimizes h(n)**).  

### Data Structure
- Uses a **priority queue**, ordered by heuristic value **h(n)**.  

### Advantages
- Often very fast.  
- Good for reaching a goal quickly in large spaces.  

### Disadvantages
- Not complete (can get stuck in loops).  
- Not optimal (may find a longer path than necessary).  

---

# A* Search

### Concept
- Combines path cost and heuristic:  
  **f(n) = g(n) + h(n)**  
  - **g(n):** cost so far  
  - **h(n):** estimated cost to goal  

### Optimality
- If heuristic is **admissible** and **consistent**, A* guarantees the shortest path.  

### Completeness
- Always complete, as long as:  
  - branching factor is finite  
  - step costs > 0  

### Time Complexity
- Depends on heuristic quality:  
  - **Good heuristic →** fewer nodes expanded.  
  - **Bad heuristic →** behaves like BFS/Uniform Cost.  

### Practical Uses
- GPS navigation  
- Game pathfinding  
- Robotics  
- Scheduling problems  

---

# Greedy vs A* Comparison
- **Greedy:** fast but not optimal.  
- **A*:** slower but guarantees optimal solution (with good heuristics).  

---

# Week 7 – Local Search & Optimization

## Local Search Idea
- Instead of exploring entire search trees, local search algorithms start with a **candidate solution** and improve it step by step.  

## Optimization Focus
- Goal is not just to find **any solution**, but the **best (optimal or near-optimal)** solution.  

## State-Space Landscape
- Imagine a 3D map where **elevation = solution quality**.  
- Local search moves “uphill” toward better states.  

---

# Hill Climbing

### Concept
- Continuously move to a better neighbor state (**higher value, lower cost**).  

### Types of Hill Climbing
- **Simple Hill Climbing** – picks the first better neighbor.  
- **Steepest-Ascent Hill Climbing** – picks the best among all neighbors.  
- **Stochastic Hill Climbing** – randomly chooses among better neighbors.  

### Advantages
- Simple and fast.  
- Requires little memory.  
- Works well in many optimization problems.  

### Disadvantages
- Gets stuck in **local maxima** (a peak that isn’t the highest).  
- Can loop on **plateaus** (flat regions).  
- Can slow down at **ridges** (narrow peaks).  

### Solutions
- **Random restarts**  
- **Sideways moves** (allow some non-improving moves)  
- **Simulated Annealing** – gradual random exploration  

---

# Genetic Algorithms (GA)

### Inspiration
- Based on **natural selection and genetics** in biology.  

### Representation
- Solutions are represented as **chromosomes** (bit strings or encoded structures).  

### Population
- GA works with a **population** of candidate solutions instead of one solution.  

### Operators
- **Selection:** Choose best candidates (fittest).  
- **Crossover:** Combine two parents to create children.  
- **Mutation:** Randomly alter genes to introduce diversity.  

### Advantages
- Explores large search spaces effectively.  
- Avoids being trapped in local maxima through diversity.  
- Flexible and applicable to many optimization problems.  

### Disadvantages
- Computationally expensive.  
- Requires careful tuning of parameters (population size, mutation rate).  
- May converge slowly.  

---

# Applications of Local Search & GA
- Scheduling (timetables, airline crew)  
- Route planning  
- Game AI  
- Machine learning feature selection  

---

# Week 8 – Games as Search Problems

## Why Games in AI?
- Games provide **controlled environments** to test AI strategies, reasoning, and decision-making.  

## Game as a Search Problem
- The AI’s goal is to find a strategy that **maximizes its winning chances**, similar to solving a search problem.  

---

# Key Concepts in Game Search

### Two-Person Games
- Involve two players who alternate turns (e.g., chess, checkers, tic-tac-toe).  

### Zero-Sum Games
- One player’s gain = the other player’s loss (classic competitive games).  

### Game Tree
- A **tree representation** of all possible moves.  
  - **Nodes =** states  
  - **Edges =** moves  

---

## Game Formulation

- **Initial State** – The starting position (e.g., chessboard at the beginning).  
- **Player Function** – Indicates which player moves (Max or Min).  
- **Actions Function** – Lists all legal moves from a state.  
- **Result Function** – Defines the new state after an action.  
- **Terminal States** – States where the game ends (win, lose, draw).  
- **Utility Function (Payoff)** – Assigns a numeric value to terminal states:  
  - +1 → win  
  - -1 → loss  
  - 0 → draw  

---

## Perfect Decisions
- If the **game tree is fully expanded**, an agent can compute the exact best move.  

---

## Deterministic vs. Chance Games
- **Deterministic** – No randomness (e.g., chess).  
- **Chance** – Includes randomness (e.g., backgammon with dice).  

---

## Perfect Information Games
- Both players can see the **full state of the game** (e.g., chess, tic-tac-toe).  

---

## Importance of Game Search
- Builds the foundation for **adversarial search** strategies such as:  
  - **Minimax**  
  - **Alpha-Beta pruning**  
(to be covered in later weeks).  

---

