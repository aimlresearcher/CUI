# Question 01
import random

# candidate data 
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
    {"skill": 92, "salary": 63},
]

MAX_BUDGET = 250
POP_SIZE = 50
MUTATION_RATE = 0.05
MAX_GENERATIONS = 100
NO_IMPROVEMENT_LIMIT = 10
TOURNAMENT_SIZE = 3
CHROMOSOME_LENGTH = len(candidates)


def fitness(individual):
    total_skill = total_salary = 0
    for i, bit in enumerate(individual):
        if bit == 1:
            total_skill += candidates[i]["skill"]
            total_salary += candidates[i]["salary"]
    return total_skill if total_salary <= MAX_BUDGET else 0


def create_individual():
    return [random.randint(0, 1) for _ in range(CHROMOSOME_LENGTH)]


def tournament_selection(population):
    competitors = random.sample(population, TOURNAMENT_SIZE)
    return max(competitors, key=fitness)


def crossover(parent1, parent2):
    point = random.randint(1, CHROMOSOME_LENGTH - 1)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]


def mutate(individual):
    if random.random() < MUTATION_RATE:
        index = random.randint(0, CHROMOSOME_LENGTH - 1)
        individual[index] = 1 - individual[index]
    return individual


def genetic_algorithm():
    population = [create_individual() for _ in range(POP_SIZE)]
    best_individual = max(population, key=fitness)
    best_fitness = fitness(best_individual)
    generations_without_improvement = 0

    for generation in range(MAX_GENERATIONS):
        new_population = []
        for _ in range(POP_SIZE // 2):
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutate(child1), mutate(child2)])

        population=new_population
        current_best = max(population, key=fitness)
        current_fitness = fitness(current_best)

        if current_fitness>best_fitness:
            best_fitness=current_fitness
            best_individual=current_best
            generations_without_improvement = 0
        else:
            generations_without_improvement +=1

        if generations_without_improvement>=NO_IMPROVEMENT_LIMIT:
            print(f"No improvement in {NO_IMPROVEMENT_LIMIT} generations. Stopping at generation {generation + 1}.")
            break

    return best_individual, best_fitness


best_team , best_score = genetic_algorithm()
selected_candidates = [i + 1 for i, bit in enumerate(best_team) if bit == 1]
total_salary = sum(candidates[i]["salary"] for i in range(CHROMOSOME_LENGTH) if best_team[i])

print(" Selected Candidates for the TEAM are: ", selected_candidates)
print("The Total SKILLL SCORE of the TEAM is :", best_score)
print("The Total Salary is :", total_salary)

# Question 02
courses = {
    "Course1": 30,
    "Course2": 50,
    "Course3": 40,
    "Course4": 20,
    "Course5": 60
}

#Room Capacity
rooms = {
    "Room1": 50,
    "Room2": 40,
    "Room3": 60
}

# Backtracking function
def backtrack(course_list, room_list, index, assignment, used_rooms, solutions):
    if index == len(course_list):
        solutions.append(assignment.copy())
        return

    course = course_list[index]
    student_count = courses[course]

    for room in room_list:
        if room not in used_rooms and student_count <= rooms[room]:
            assignment[course] = room
            used_rooms.add(room)

            backtrack(course_list, room_list, index + 1, assignment, used_rooms, solutions)

            used_rooms.remove(room)
            del assignment[course]

def find_course_assignments():
    course_list = list(courses.keys())
    room_list = list(rooms.keys())
    assignment = {}
    used_rooms = set()
    solutions = []

    backtrack(course_list, room_list, 0, assignment, used_rooms, solutions)

    if solutions:
        print("Valid Assignments Found:")
        for idx, sol in enumerate(solutions, 1):
            print(f"Solution {idx}:")
            for course, room in sol.items():
                print(f"  {course} → {room}")
            print()
    else:
        print("No solution found.")


find_course_assignments()