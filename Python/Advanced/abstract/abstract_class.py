from abc import ABC, abstractmethod
from collections import namedtuple

Attack = namedtuple('Attack', ('name', 'damage'))
AttackSpecial = namedtuple('Attack', ('name', 'damage'))


class BasicPokemon(ABC):
    def __init__(self, name:str) -> None:
        self.name = name
        self._level = 1

    @abstractmethod
    def main_attack(self):
        pass


class Pikachu(BasicPokemon):
    def main_attack(self) -> namedtuple:
        print('ATTACK')
        return Attack('Thunder', 5)

class Charizard(BasicPokemon):
    def main_attack(self) -> namedtuple:
        print('ATTACK')
        return Attack('Fire ball', 5)

pikachu1 = Pikachu('pika')
chari1 = Charizard('chari1')

pikachu1.main_attack()
chari1.main_attack()