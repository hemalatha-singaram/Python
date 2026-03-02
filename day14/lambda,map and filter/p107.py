numbers = [1, -2, 3, -4, 5]
positive=list(filter(lambda n:n>0,numbers))
squared_positive=list(map(lambda n:n*n,positive))
print(squared_positive)