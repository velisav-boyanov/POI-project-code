import random
from multiprocessing import Pool

def simulate_scattering(num_neutrons):
    scattered_count = 0
    for _ in range(num_neutrons):
        scattering_chance = random.random()
        if scattering_chance >= 0.5:
            scattered_count += 1
    return scattered_count

def monte_carlo_scattering_probability(num_neutrons, num_simulations):
    # Създаваме пул от процеси с броя налични процесори
    with Pool() as pool:
        # Изпълняваме множество симулации паралелно
        results = pool.map(simulate_scattering, [num_neutrons] * num_simulations)
    
    # Сумираме резултатите от всички симулации
    total_scattered = sum(results)
    
    # Изчисляваме общия брой неутрони, които са били хвърлени във всички симулации
    total_neutrons = num_neutrons * num_simulations
    
    # Изчисляваме вероятността за разсейване
    scattering_probability = total_scattered / total_neutrons
    
    return scattering_probability

# Брой неутрони за една симулация
num_neutrons = 10000
# Брой симулации, които ще извършим
num_simulations = 4

# Изчисляваме вероятността за разсейване с паралелен подход
scattering_probability = monte_carlo_scattering_probability(num_neutrons, num_simulations)

# Отпечатваме резултата
print(f"Оценена вероятност за разсейване на неутрони: {scattering_probability}")
