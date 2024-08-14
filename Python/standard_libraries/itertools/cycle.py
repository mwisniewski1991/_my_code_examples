from itertools import cycle

cycle_iter = cycle("<==>")

for i in range(20):
    print(next(cycle_iter))


colors = ['red', 'blue', 'green', 'yellow', 'orange', 'pink', 'grey']
cycle_iter = cycle([1,2,3])
colors_assigned = [name for name in zip(cycle_iter, colors)]
print(colors_assigned)