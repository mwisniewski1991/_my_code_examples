class Guitar:
    def __init__(self, n_strings:int = 6) -> None:
        self.n_strings = n_strings

    def play(self) -> None:
        print('pam pam dam dam')

class BassGuitar(Guitar):
    pass

class ElectricGuitar(Guitar):
    def __init__(self, n_strings:int = 8) -> None:
        super().__init__()
        self.n_strings = n_strings
        self.color = ("#000000", '#ffffff')
        self.__cost = 50

    def play_louder(self)-> None:
        print('pam pam dam dam'.upper())

    def __secret(self) -> None:
        print(f'this guitar cost {self.__cost}')



my_guitar = Guitar(6)
print(f'my_guitar strings: {my_guitar.n_strings}')
print('-- -- --')

my_bass_guitar = BassGuitar(6)
print(f'my_bass_guitar strings: {my_bass_guitar.n_strings}')
print('-- -- --')

my_electric_guitar = ElectricGuitar(8)
print(f'my_electric_guitar strings: {my_electric_guitar.n_strings}')
print('-- -- --')

my_guitar.play()
my_electric_guitar.play_louder()
print('-- -- --')

print(my_electric_guitar._ElectricGuitar__cost)
my_electric_guitar._ElectricGuitar__secret()
print('-- -- --')