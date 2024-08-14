from itertools import count

count_iter = count()

for i in range(0,10):
    print(next(count_iter))

for i in count(100):
    print(i)
    if i >= 110:
        break

colors = ['red', 'blue', 'green']
indexed_colors = [color for color in zip(count(), colors)] #like enumerate
print(indexed_colors)