import random

def monte_carlo_probability_estimation(num_trials):
    # Брой успешни събития (хвърляне на "орел")
    successes = 0
    
    # Изпълняваме определен брой опити (т.е. хвърляния на зар)
    for _ in range(num_trials):
        # Хвърляме зара - генерираме случайно число от 1 до 6
        roll = random.randint(1, 6)
        
        # Проверяваме дали сме хвърлили "орел" (т.е. число 1)
        if roll == 1:
            successes += 1
    
    # Изчисляваме вероятността като успешните събития / общия брой опити
    probability = successes / num_trials
    
    return probability

# Брой опити за оценка на вероятността
num_trials = 100000

# Извършваме оценка на вероятността за хвърляне на "орел"
estimated_probability = monte_carlo_probability_estimation(num_trials)

# Отпечатваме резултата
print(f"Оценената вероятност за хвърляне на 'орел': {estimated_probability}")
