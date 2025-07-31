#random function
# This code generates a random integer between 1 and 10 and prints it.
import random
random_number = random.randint(1, 10)
print(random_number)

# This code generates a random floating-point number between 0.0 and 1.0 and prints it.
random_num = random.random()
print(random_num)

# This code generates a random floating-point number between 1.0 and 10.0 and prints it.
random_float = random.uniform(1.0, 10.0)
print(random_float)

# This code generates a random choice from a list of options and prints it.
random_head_or_tail = random.choice(['Heads', 'Tails'])
print(random_head_or_tail)
