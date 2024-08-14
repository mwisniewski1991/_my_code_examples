from itertools import repeat

for i in repeat('HEJ', 3):
        print(i)

squares = list(map(pow, range(10), repeat(2)))
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]