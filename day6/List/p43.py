'''Challenge 2: Write a function remove_negatives that takes a list and returns a new list with only the positive numbers.
remove_negatives([1, -2, 3, -4, 5])  # should return [1, 3, 5]'''
def remove_negatives(lst):
    new_lst=[]
    for num in lst:
        if num > 0:
            new_lst.append(num)
    return new_lst
numbers = [1, -2, 3, -4, 5]
print(remove_negatives(numbers))
    