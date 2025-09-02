# 🧠 What is an Intelligent Agent?

An **agent** = anything that perceives its environment through **sensors** and acts upon it with **actuators**.  

An **intelligent agent** = one that **chooses actions rationally** to achieve its goals (best possible outcome given what it knows).  

---

## 💡 Analogy: Student as an Agent
- **Sensors**: eyes, ears → see slides, hear lecture  
- **Actuators**: hands, mouth → write notes, ask questions  
- **Goal**: pass the course with good grades  

---

# 🌍 Types of Agent Environments

According to **Russell & Norvig**, environments are classified using several dimensions:  

---

## 1. Observable vs. Partially Observable
- **Fully Observable**: Agent has access to the complete state of the environment.  
  - *Example*: **Chess** → the board is fully visible.  
  - *Analogy*: Open-book exam → you see all the information.  
- **Partially Observable**: Agent only has limited information.  
  - *Example*: **Poker** → you can’t see the opponent’s cards.  
  - *Analogy*: Closed-book exam → rely on memory, not all info is visible.  

---

## 2. Deterministic vs. Stochastic
- **Deterministic**: Next state is fully determined by current state + action.  
  - *Example*: Solving a math equation.  
  - *Analogy*: Following a recipe → exact ingredients = exact result.  
- **Stochastic**: Involves randomness or uncertainty in outcomes.  
  - *Example*: **Self-driving car in traffic** → can’t predict pedestrians perfectly.  
  - *Analogy*: Playing football → strategy helps, but outcomes are uncertain.  

---

## 3. Episodic vs. Sequential
- **Episodic**: Each action is independent of the previous one.  
  - *Example*: Image classification → each picture is separate.  
  - *Analogy*: Quiz show → each question is unrelated.  
- **Sequential**: Current decision affects future decisions.  
  - *Example*: Driving a car → each turn affects destination.  
  - *Analogy*: Choosing university courses → affects prerequisites and graduation path.  

---

## 4. Static vs. Dynamic
- **Static**: Environment doesn’t change while the agent is deciding.  
  - *Example*: Crossword puzzle → grid doesn’t change.  
  - *Analogy*: Paused game → time frozen while you think.  
- **Dynamic**: Environment changes during decision-making.  
  - *Example*: Driving in traffic → cars keep moving.  
  - *Analogy*: Group discussion → people add points as you think.  

---

## 5. Discrete vs. Continuous
- **Discrete**: Finite set of states, actions, or percepts.  
  - *Example*: Chess → 64 squares, fixed moves.  
  - *Analogy*: Multiple-choice exam → limited answers.  
- **Continuous**: Infinite possible states or actions.  
  - *Example*: Driving → continuous speed and steering.  
  - *Analogy*: Essay exam → endless possible answers.  

---

## 📊 Comparison Table

| **Property**     | **Discrete Example**                | **Continuous Example**            |
|------------------|-------------------------------------|-----------------------------------|
| **Observable**   | Chess (see everything)              | Poker (hidden cards)              |
| **Deterministic**| Solving equations                   | Weather prediction (uncertain)    |
| **Episodic**     | Spam filter (each email separate)   | Self-driving car (turns affect future) |
| **Static**       | Sudoku puzzle                       | Stock market (changes while you think) |
| **Discrete**     | Tic-tac-toe, multiple-choice exam   | Driving, handwriting recognition  |

---

## ✅ Key Idea
The **design of an intelligent agent** depends on its environment:  
- **Chess-playing agent** → needs **strategy & search**.  
- **Self-driving car** → needs **perception, uncertainty handling, and real-time decision-making**.  
