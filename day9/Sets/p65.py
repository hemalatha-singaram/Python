fruits = {"apple", "banana", "mango"}

fruits.add("grape")       # adds one item
fruits.remove("banana")   # removes item, error if not found
fruits.discard("kiwi")    # removes item, NO error if not found
print(len(fruits))        # number of items