import random
import math
from mpi4py import MPI

def simulate_scattering(num_neutrons):
    scattered_count = 0
    for _ in range(num_neutrons):
        scattering_chance = random.random()
        if scattering_chance >= 0.5:
            scattered_count += 1
    return scattered_count

def monte_carlo_scattering_probability(num_neutrons, num_simulations):
    scattered_count = 0
    
    # Разпределяме симулациите между различните възли на Грид 5000
    local_simulations = math.ceil(num_simulations / comm.size)
    
    for _ in range(local_simulations):
        scattered_count += simulate_scattering(num_neutrons)
    
    # Събираме резултатите от всички възли
    total_scattered = comm.reduce(scattered_count, op=MPI.SUM, root=0)
    
    # Изчисляваме общия брой неутрони, които са били хвърлени във всички симулации
    total_neutrons = num_neutrons * num_simulations
    
    if rank == 0:
        # Изчисляваме вероятността за разсейване
        scattering_probability = total_scattered / total_neutrons
    else:
        scattering_probability = None
    
    # Изпращаме вероятността за разсейване от кореновия възел
    scattering_probability = comm.bcast(scattering_probability, root=0)
    
    return scattering_probability

# Създаваме комуникатор за MPI
comm = MPI.COMM_WORLD
# Определяме номера на текущия възел
rank = comm.Get_rank()

# Брой неутрони за една симулация
num_neutrons = 10000
# Брой симулации, които ще извършим
num_simulations = 4

# Изчисляваме вероятността за разсейване с паралелен подход
scattering_probability = monte_carlo_scattering_probability(num_neutrons, num_simulations)

if rank == 0:
    # Отпечатваме резултата
    print(f"Оценена вероятност за разсейване на неутрони: {scattering_probability}")
