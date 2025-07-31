import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#Option 1: Using random.choice
random_name = random.choice(friends)
print(f"{random_name} is going to buy the meal today!")

# Option 2: Using random.randint
random_index = random.randint(0, len(friends) - 1)
random_name = friends[random_index]
print(f"{random_name} is going to buy the meal today!")

# Option 3: Using random sample
random_name = random.sample(friends, 1)[0]
print(f"{random_name} is going to buy the meal today!")

# Option 4: Using random.shuffle
random.shuffle(friends)
random_name = friends[0]
print(f"{random_name} is going to buy the meal today!")

# Option 5: Using random.choices (with weights)
weights = [1, 1, 1, 1, 1]
random_name = random.choices(friends, weights=weights, k=1)[0]
print(f"{random_name} is going to buy the meal today!")

# Option 6: Using random.randrange
random_index = random.randrange(len(friends))
random_name = friends[random_index]
print(f"{random_name} is going to buy the meal today!")

# Option 7: Using random.getrandbits
random_index = random.getrandbits(3) % len(friends)  # Assuming len(friends) <= 8
random_name = friends[random_index]
print(f"{random_name} is going to buy the meal today!")

# Option 8: Using random.random
random_index = int(random.random() * len(friends))
random_name = friends[random_index]
print(f"{random_name} is going to buy the meal today!")

# Option 9: Using random.uniform
random_index = int(random.uniform(0, len(friends)))
random_name = friends[random_index]
print(f"{random_name} is going to buy the meal today!")
