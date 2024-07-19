X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(X[::-1])
print(*X[::-1])
print(zip(*X[::-1]))
result = list(zip(*X[::-1]))
print(result)


