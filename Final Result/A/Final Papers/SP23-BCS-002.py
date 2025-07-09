# Question 01
import random


candidates = [
    {"skill": 80, "salary": 50},
    {"skill": 70, "salary": 40},
    {"skill": 90, "salary": 60},
    {"skill": 85, "salary": 55},
    {"skill": 75, "salary": 45},
    {"skill": 95, "salary": 65},
    {"skill": 60, "salary": 30},
    {"skill": 78, "salary": 48},
    {"skill": 88, "salary": 58},
    {"skill": 92, "salary": 63}
]

BUDGET = 250
POPULATION_SIZE = 30
GENERATIONS = 100
NO_IMPROVEMENT_LIMIT = 10


def fitness(individual):
    total_skill = 0
    total_salary = 0
    for i, gene in enumerate(individual):
        if gene == 1:
            total_skill += candidates[i]["skill"]
            total_salary += candidates[i]["salary"]
    if total_salary <= BUDGET:
        return total_skill
    return 0


def create_individual():
    return [random.randint(0, 1) for _ in range(10)]


def tournament_selection(population, k=3):
    selected = random.sample(population, k)
    selected.sort(key=lambda x: fitness(x), reverse=True)
    return selected[0]


def crossover(parent1, parent2):
    point = random.randint(1, len(parent1)-1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2


def mutate(individual, mutation_rate=0.01):
    return [bit if random.random() > mutation_rate else 1-bit for bit in individual]


def genetic_algorithm():
    population = [create_individual() for _ in range(POPULATION_SIZE)]
    best_individual = max(population, key=fitness)
    best_fitness = fitness(best_individual)
    no_improvement = 0

    for generation in range(GENERATIONS):
        new_population = []
        while len(new_population) < POPULATION_SIZE:
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.extend([child1, child2])

        population = new_population
        current_best = max(population, key=fitness)
        current_fitness = fitness(current_best)

        if current_fitness > best_fitness:
            best_fitness = current_fitness
            best_individual = current_best
            no_improvement = 0
        else:
            no_improvement += 1

        print(f"Generation {generation+1}: Best Skill = {best_fitness}")

        if no_improvement >= NO_IMPROVEMENT_LIMIT:
            print("No improvement for 10 generations. Stopping...")
            break

    return best_individual, best_fitness


best_team, best_skill = genetic_algorithm()


print("\nBest Team Configuration:\n")

selected_candidates = []
total_salary = 0

for i, bit in enumerate(best_team):
    if bit == 1:
        candidate = candidates[i]
        selected_candidates.append(
            f"Candidate {i+1} is selected with Skill = {candidate['skill']} and Salary = {candidate['salary']}"
        )
        total_salary += candidate['salary']

for line in selected_candidates:
    print(line)

print(f"\nTotal Skill Score of Team: {best_skill}")
print(f"Total Salary Used: {total_salary}")

# Question 02
courses = {
    'Course 1': 30,
    'Course 2': 50,
    'Course 3': 40,
    'Course 4': 20,
    'Course 5': 60
}

rooms = {
    'Room 1': 50,
    'Room 2': 40,
    'Room 3': 60
}

def backtrack(assignment, unassigned_courses, available_rooms):
    if not unassigned_courses:
        return assignment

    course = unassigned_courses[0]
    students = courses[course]

    for room in available_rooms:
        capacity = rooms[room]

        if students <= capacity:
            assignment[course] = room
            new_rooms = available_rooms.copy()
            new_rooms.remove(room)

            result = backtrack(assignment, unassigned_courses[1:], new_rooms)
            if result:
                return result

            del assignment[course]

    return None

solution = backtrack({}, list(courses.keys()), list(rooms.keys()))

if solution:
    print("Valid Assignment:")
    for course, room in solution.items():
        print(f"{course} → {room} (Students: {courses[course]}, Capacity: {rooms[room]})")
else:
    print("No solution exists because there are 5 courses and only 3 rooms, and each room can hold only one course.")
