# algorithms/genetic_algorithm.py
import random
from core.puzzle import get_neighbors, heuristic, generate_random_state
from core.config import goal_state

def genetic_algorithm(start_state_unused, population_size=100, generations=1000, mutation_rate=0.1):
    def create_random_state():
        numbers = list(range(9))
        random.shuffle(numbers)
        return [numbers[i:i + 3] for i in range(0, 9, 3)]

    def fitness(state):
        return heuristic(state)

    def crossover(parent1, parent2):
        flat1 = sum(parent1, [])
        flat2 = sum(parent2, [])
        cut = random.randint(1, 7)
        child = flat1[:cut] + [n for n in flat2 if n not in flat1[:cut]]
        return [child[i:i + 3] for i in range(0, 9, 3)]

    def mutate(state):
        flat = sum(state, [])
        if random.random() < mutation_rate:
            i, j = random.sample(range(9), 2)
            flat[i], flat[j] = flat[j], flat[i]
        return [flat[i:i + 3] for i in range(0, 9, 3)]

    population = [create_random_state() for _ in range(population_size)]
    best_path = []  # Danh sách lưu trạng thái tốt nhất qua từng thế hệ

    for _ in range(generations):
        population.sort(key=fitness) # Sắp xếp từ tốt nhất đến tệ nhất
        best_state = population[0]
        best_path.append(best_state)  # Lưu trạng thái tốt nhất của thế hệ này

        if best_state == goal_state:
            return best_path  # Trả về danh sách trạng thái qua từng thế hệ

        next_population = population[:10]
        while len(next_population) < population_size:
            parent1, parent2 = random.sample(population[:50], 2)
            child = mutate(crossover(parent1, parent2))
            next_population.append(child)
        population = next_population

    return best_path  # Trả về danh sách trạng thái tốt nhất qua từng thế hệ