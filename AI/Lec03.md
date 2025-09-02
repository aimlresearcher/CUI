# 🧑‍💻 Types of Intelligent Agents

---

## 1. Simple Reflex Agents
- **Definition**: Act only on the current percept (what they see right now). They follow simple “if–then” rules.  
- **Example**: Thermostat → *“If temperature < 20°C, turn on heater.”*  
- **Student Analogy**: A student who hears *“quiz today”* and immediately panics — no long-term thinking, just reacts.  
- **Real AI Example**: Spam filter → *“If email has word ‘lottery,’ mark as spam.”*  

---

## 2. Model-Based Reflex Agents
- **Definition**: Keep an internal model of the world (memory of past states). Useful in partially observable environments.  
- **Example**: Self-driving car → remembers a pedestrian walked behind a truck even if they’re not visible now.  
- **Student Analogy**: A student who remembers what was taught last lecture and uses it to understand today’s lesson.  
- **Real AI Example**: **Roomba vacuum** → builds a map of your house to clean efficiently.  

---

## 3. Goal-Based Agents
- **Definition**: Take actions to achieve specific goals, not just reflexes.  
- **Example**: GPS navigation → goal = *reach destination*; chooses path accordingly.  
- **Student Analogy**: A student aiming to graduate carefully chooses which courses to take (not just reacting each semester).  
- **Real AI Example**: **Chess-playing AI** → goal = *win the game*.  

---

## 4. Utility-Based Agents
- **Definition**: Maximize happiness (utility) by choosing the best among many options.  
- **Example**: Choosing between 2 driving routes: both reach the destination, but one is faster and safer → higher utility.  
- **Student Analogy**: A student wants to graduate but also maximize GPA, enjoy courses, and have free time.  
- **Real AI Example**: **Netflix recommender** → suggests movies to maximize enjoyment, not just any movie.  

---

## 5. Learning Agents
- **Definition**: Improve performance over time by learning from experience.  
- **Example**: A spam filter that adapts to new types of spam.  
- **Student Analogy**: A student who reviews past mistakes, studies smarter, and performs better next time.  
- **Real AI Example**: **AlphaGo** → learned by playing millions of games against itself and humans.  

---

## 📊 Comparison Table

| **Agent Type**       | **Memory?** | **Goal-Oriented?** | **Optimizes (Utility)?** | **Learns?** | **Example (AI)**          | **Analogy (Student Life)**                 |
|-----------------------|-------------|---------------------|---------------------------|-------------|----------------------------|--------------------------------------------|
| **Simple Reflex**     | ❌ No       | ❌ No               | ❌ No                     | ❌ No       | Thermostat, Spam filter    | Student panicking at *“quiz today”*        |
| **Model-Based Reflex**| ✅ Yes      | ❌ No               | ❌ No                     | ❌ No       | Roomba vacuum              | Student remembering last lecture           |
| **Goal-Based**        | ✅ Yes      | ✅ Yes              | ❌ No                     | ❌ No       | GPS navigation, Chess AI   | Student planning path to graduation        |
| **Utility-Based**     | ✅ Yes      | ✅ Yes              | ✅ Yes                    | ❌ No       | Netflix recommender        | Student balancing GPA + free time          |
| **Learning Agent**    | ✅ Yes      | ✅ Yes              | ✅ Yes                    | ✅ Yes      | AlphaGo, Adaptive spam filter | Student learning from past mistakes     |

---

## ✅ Key Takeaway
- **Reflex** → *“React.”*  
- **Model-Based** → *“Remember.”*  
- **Goal-Based** → *“Plan.”*  
- **Utility-Based** → *“Choose best.”*  
- **Learning Agent** → *“Improve.”*  
