import timeit

# Define the setup for the benchmark
setup = """
a = 26342
b = 25050
"""

# Measure the time taken for floor division
floor_division_time = timeit.repeat('c = a // b', setup=setup, number=1000000, repeat=5)

# Measure the time taken for true division
true_division_time = timeit.repeat('c = a / b', setup=setup, number=1000000, repeat=5)

print(f"Floor division time: {floor_division_time}")
print(f"min: {min(floor_division_time)}")
print(f"True division time: {true_division_time}")
print(f"min: {min(true_division_time)}")

setup_2 = """
a = 26342.0
b = 25050.0
"""

# Measure the time taken for floor division
floor_division_time = timeit.repeat('c = a // b', setup=setup_2, number=1000000, repeat=5)

# Measure the time taken for true division
true_division_time = timeit.repeat('c = a / b', setup=setup_2, number=1000000, repeat=5)

print(f"Floor division time: {floor_division_time}")
print(f"min: {min(floor_division_time)}")
print(f"True division time: {true_division_time}")
print(f"min: {min(true_division_time)}")
