import random

def monte_carlo_scattering_probability(num_neutrons, num_scattered):
    # Променлива за броя на неутроните, които са били разсеяни
    scattered_count = 0
    
    # Изпълняваме определен брой неутрони
    for _ in range(num_neutrons):
        # Генерираме случайно число между 0 и 1, което представлява вероятността за разсейване
        scattering_chance = random.random()
        
        # Ако вероятността за разсейване е по-голяма или равна на 0.5, неутронът е бил разсеян
        if scattering_chance >= 0.5:
            scattered_count += 1
    
    # Изчисляваме вероятността за разсейване като броя на разсеяните неутрони / общия брой неутрони
    scattering_probability = scattered_count / num_neutrons
    
    return scattering_probability

# Брой неутрони за симулация
num_neutrons = 10000

# Брой от тези неутрони, които са били разсеяни
num_scattered = 0

# Изчисляваме вероятността за разсейване с помощта на метода на Монте Карло
scattering_probability = monte_carlo_scattering_probability(num_neutrons, num_scattered)

# Отпечатваме резултата
print(f"Оценена вероятност за разсейване на неутрони: {scattering_probability}")
