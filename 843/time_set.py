import timeit

# Function to create a set directly
def create_set_directly():
  my_set = set()
  for i in range(10000):
    my_set.add(i)

# Function to create a list and then convert it to a set
def create_list_then_set():
  my_list = [i for i in range(10000)]
  my_set = set(my_list)

# Function to create a tuple and then convert it to a set
def create_tuple_then_set():
  my_tuple = tuple(i for i in range(10000))
  my_set = set(my_tuple)

def gen_then_set():
  my_tuple = (i for i in range(10000))
  my_set = set(my_tuple)

def inline_set():
  my_tuple = {i for i in range(10000)}


# Measure the time taken by each function
time_directly = timeit.timeit(create_set_directly, number=1000)
time_list_then_set = timeit.timeit(create_list_then_set, number=1000)
time_tuple_then_set = timeit.timeit(create_tuple_then_set, number=1000)
time_gen_then_set = timeit.timeit(gen_then_set, number=1000)
time_inline_set = timeit.timeit(inline_set, number=1000)

print(f"Time taken to create set directly: {time_directly:.6f} seconds")
print(f"Time taken to create list then convert to set: {time_list_then_set:.6f} seconds")
print(f"Time taken to create tuple then convert to set: {time_tuple_then_set:.6f} seconds")
print(f"Time taken to create generator then convert to set: {time_gen_then_set:.6f} seconds")
print(f"Time taken to create set inline: {time_inline_set:.6f} seconds")