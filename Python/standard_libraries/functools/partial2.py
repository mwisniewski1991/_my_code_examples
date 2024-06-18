from functools import partial

def constructor(name:str, number:int, color:int) -> float:
    print(f'{name=}, {number=}, {color=}')


specify_name = partial(constructor, name='Tommy')
specify_name(number=1, color='green')
specify_name(number=2, color='red')

specify_number = partial(constructor, number=3333)
specify_number(name='Bob', color='green')
specify_number(name='Tom', color='red')

specify_color = partial(constructor, color='limone')
specify_color(name='Bob', number=3)
specify_color(name='Tom', number=4)