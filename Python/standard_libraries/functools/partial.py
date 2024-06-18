from functools import partial

def division(number:int, division:int) -> float:
    return number / division

division_by_2 = partial(division, division=2)
division_by_5 = partial(division, division=5)
division_by_10 = partial(division, division=10)

print(f'{division_by_2(10)=}')
print(f'{division_by_5(10)=}')
print(f'{division_by_10(10)=}')

