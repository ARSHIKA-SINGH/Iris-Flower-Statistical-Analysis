import random


# Recursive sum function
def recursive_sum(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + recursive_sum(lst[1:])


# Recursive count function
def recursive_count(lst):
    if len(lst) == 0:
        return 0
    return 1 + recursive_count(lst[1:])


# Return 10 random unique tuples
def get_random_unique(unique_set):
    return random.sample(list(unique_set), 10)