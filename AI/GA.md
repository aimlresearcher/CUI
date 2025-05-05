# 🧬 Genetic Algorithms (GAs) — Summary

## Definition
Genetic Algorithms are search and optimization algorithms inspired by the process of natural selection and genetics. They are widely used to solve complex optimization and search problems.

---

## 🔎 Key Concepts

- **Population**: A set of possible solutions.
- **Chromosome (Individual)**: A single solution represented often as a string (binary, real-valued, etc.).
- **Gene**: Part of a chromosome, representing a specific feature of the solution.

---

## 🔄 Basic Steps of a Genetic Algorithm

1. **Initialization**
   - Create an initial population randomly or heuristically.
2. **Evaluation (Fitness Function)**
   - Assess how good each solution is (assign a fitness score).
3. **Selection**
   - Choose the fittest individuals to reproduce (e.g., roulette wheel, tournament selection).
4. **Crossover (Recombination)**
   - Combine parts of two parents to create offspring.
5. **Mutation**
   - Randomly alter some genes to maintain diversity.
6. **Replacement**
   - Form the new generation, possibly replacing the least fit solutions.
7. **Termination**
   - Stop when a solution meets the criteria or after a set number of generations.

---

## 🔥 Example Problem (Simple)

**Optimize**: Maximize the function _f(x) = x²_ where _x_ is an integer between 0 and 31.

- **Encoding**: 5-bit binary string.
- **Fitness Function**: _f(x) = x²_.
- **Operations**: Perform selection, crossover, mutation until the best _x_ is found.

---

## 📊 Applications

- Scheduling problems
- Game playing strategies
- Neural network training
- Engineering design
- Machine learning model hyperparameter tuning

---

## 📖 Why GAs Are Important in AI

Genetic Algorithms are a key example of evolutionary computation — algorithms inspired by natural processes — and are used when:

- The search space is large and complex.
- Traditional methods fail or are inefficient.
- You want to avoid local minima in optimization.

---

## ✅ Additional Resources (If Needed)

- Simple code example (Python or pseudocode).
- Diagram explaining the GA flow (for your slides).
- Quiz questions to prepare for Week 8.

---

# 🎯 Problem

Maximize:  
**f(x) = x²** for **x ∈ {0, 31}**

We will use **5-bit chromosomes** because:  
**2⁵ = 32** (0 to 31)

---

## 🔥 Step 1: Initial Population

Let’s randomly pick 4 chromosomes for simplicity:

| Chromosome | Binary | Decimal (x) | Fitness f(x) = x² |
|------------|--------|-------------|--------------------|
| C1         | 01100  | 12          | 144                |
| C2         | 10101  | 21          | 441                |
| C3         | 00111  | 7           | 49                 |
| C4         | 11100  | 28          | 784                |

---

## 🔥 Step 2: Calculate Selection Probability

**Total Fitness** = 144 + 441 + 49 + 784 = **1418**

Now, calculate selection probability for each chromosome:

| Chromosome | Fitness | Probability = Fitness / Total |
|------------|---------|-------------------------------|
| C1         | 144     | 0.1015                        |
| C2         | 441     | 0.3109                        |
| C3         | 49      | 0.0345                        |
| C4         | 784     | 0.5529                        |

**Observation**: C4 and C2 have the highest chances to be selected as parents.

---

## 🔥 Step 3: Selection (Roulette Wheel)

Random selection picks:

- **Parent 1**: C4 (11100, x = 28)
- **Parent 2**: C2 (10101, x = 21)

---

## 🔥 Step 4: Crossover

Let’s assume a crossover point **after the 2nd bit**:

---

Perfect! Let me give you a basic Python implementation of a Genetic Algorithm.

We’ll solve a simple problem:

👉 Maximize the function **f(x) = x²**, where **x** is an integer between **0 and 31**.  
👉 Chromosomes will be **5-bit binary strings**.

---

## 🔥 Genetic Algorithm in Python
```python
import random

# ---- Parameters ----
POP_SIZE = 6          # Number of individuals in population
GENES = 5             # Bits per chromosome (for numbers 0 to 31)
GENERATIONS = 20      # Number of generations
MUTATION_RATE = 0.1   # Probability of mutation

# ---- Fitness Function ----
def fitness(x):
    return x ** 2

# ---- Helper Functions ----

def random_chromosome():
    return ''.join(random.choice('01') for _ in range(GENES))

def decode(chromosome):
    return int(chromosome, 2)

def select(population):
    # Roulette Wheel Selection based on fitness
    total_fitness = sum(fitness(decode(ch)) for ch in population)
    pick = random.uniform(0, total_fitness)
    current = 0
    for ch in population:
        current += fitness(decode(ch))
        if current >= pick:
            return ch

def crossover(parent1, parent2):
    point = random.randint(1, GENES - 1)
    return parent1[:point] + parent2[point:]

def mutate(chromosome):
    if random.random() < MUTATION_RATE:
        point = random.randint(0, GENES - 1)
        flipped = '1' if chromosome[point] == '0' else '0'
        chromosome = chromosome[:point] + flipped + chromosome[point + 1:]
    return chromosome

# ---- Genetic Algorithm ----

# Step 1: Initialize Population
population = [random_chromosome() for _ in range(POP_SIZE)]

for generation in range(GENERATIONS):
    # Decode and calculate fitness
    decoded = [decode(ch) for ch in population]
    fitness_values = [fitness(x) for x in decoded]
    
    # Print the best individual
    best = max(zip(population, fitness_values), key=lambda x: x[1])
    print(f"Generation {generation}: Best = {decode(best[0])}, Fitness = {best[1]}")
    
    # Step 2: Create new population
    new_population = []
    for _ in range(POP_SIZE):
        parent1 = select(population)
        parent2 = select(population)
        child = crossover(parent1, parent2)
        child = mutate(child)
        new_population.append(child)
    
    population = new_population

# Final Best Solution
decoded = [decode(ch) for ch in population]
fitness_values = [fitness(x) for x in decoded]
best = max(zip(population, fitness_values), key=lambda x: x[1])
print("\nFinal Best Solution:")
print(f"x = {decode(best[0])}, Fitness = {best[1]}")

```