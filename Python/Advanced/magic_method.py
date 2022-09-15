class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __del__(self):
        print('Object destroyed !!!')
        
    def ____(self):
        print('Object created')
        
p = Person('Mat', 25)