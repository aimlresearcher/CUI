# Q 01
import random

candidates = [
    ("can1", 80, 50),
    ("can2", 70, 40),
    ("can3", 90, 60),
    ("can4", 85, 55),
    ("can5", 75, 45),
    ("can6", 95, 65),
    ("can7", 60, 30),
    ("can8", 78, 48),
    ("can9", 88, 58),
    ("can10", 92, 63)
]

budget = 250
pop_size = 20
chrom_length = len(candidates)
mutation_rate = 0.1

def generate_chromosome():
    return [random.randint(0, 1) for _ in range(chrom_length)]

def fitness(chrom):
    total_skill = 0
    total_salary = 0
    for i in range(chrom_length):
        if chrom[i] == 1:
            total_skill += candidates[i][1]
            total_salary += candidates[i][2]
    return total_skill if total_salary <= budget else 0

def tournament_selection(pop):
    k = 3
    selected = random.sample(pop, k)
    selected.sort(key=fitness, reverse=True)
    return selected[0]

def crossover(parent1, parent2):
    point = random.randint(1, chrom_length - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(chrom):
    if random.random() < mutation_rate:
        point = random.randint(0, chrom_length - 1)
        chrom[point] = 1 - chrom[point]
    return chrom

def genetic_algorithm():
    population = [generate_chromosome() for _ in range(pop_size)]
    best_solution = None
    best_fitness = 0
    no_improvement = 0
    gen_no = 0

    for generation in range(100):
        population.sort(key=fitness, reverse=True)
        current_best = fitness(population[0])
        if current_best > best_fitness:
            best_fitness = current_best
            best_solution = population[0]
            no_improvement = 0
        else:
            no_improvement += 1

        if no_improvement >= 10:
            break

        new_population = []
        while len(new_population) < pop_size:
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1))
            new_population.append(mutate(child2))
        population = new_population
        gen_no = generation

    print("Best Fitness:", best_fitness)
    print("Selected Team:")
    total_salary = 0
    for i in range(chrom_length):
        if best_solution[i] == 1:
            print(candidates[i][0], "Skill:", candidates[i][1], "Salary:", candidates[i][2])
            total_salary += candidates[i][2]
    print("Total Salary:", total_salary)
    print("Generations:", gen_no)

genetic_algorithm()

# Q 02
courses = {
    "Course1": 30,
    "Course2": 50,
    "Course3": 40,
    "Course4": 20,
    "Course5": 60
}

rooms = {
    "Room1": 50,
    "Room2": 40,
    "Room3": 60
}

def is_valid(course, room, assignment):
    return room not in assignment.values() and courses[course] <= rooms[room]

def backtrack(course_list, assignment):
    if not course_list:
        return assignment

    course = course_list[0]
    for room in rooms:
        if is_valid(course, room, assignment):
            assignment[course] = room
            result = backtrack(course_list[1:], assignment)
            if result:
                return result
            del assignment[course]
    return None

result = backtrack(list(courses.keys()), {})

if result:
    for course, room in result.items():
        print(f"{course} -> {room}")
else:
    print("No Solution Found.")
