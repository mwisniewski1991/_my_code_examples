class A:
    def __new__(cls, *args, **kwargs):
        print("Creating new class", cls)
        return super().__new__(cls)
    
    def __init__(self, name:str):
        print('Initialization class.')


a = A('Mat')