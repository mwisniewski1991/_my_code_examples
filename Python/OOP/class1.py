class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def describe_fruit(self):
        print(f'This is {self.name}. {self.name.capitalize()} is {self.color}') 

my_fruit = Fruit('apple', 'red')
print('-- --')
print(my_fruit.__dict__)
print('-')
my_fruit.describe_fruit()
print('--  --')
