def is_subset(subset, superset):
    return set(subset).issubset(set(superset))
print(is_subset([1, 2], [1, 2, 3, 4]))  # True
print(is_subset([1, 5], [1, 2, 3, 4]))  # False