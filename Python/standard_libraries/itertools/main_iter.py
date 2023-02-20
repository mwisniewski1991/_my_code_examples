from dataclasses import dataclass
from typing import Iterable

def iter_raw() -> None: 
    print('----')
    countries:tuple = ("Germany", "France", "Italy", "Spain", "Portugal", "Greece")
    country_iter = iter(countries)

    while True:
        try:
            country = next(country_iter)
        except StopIteration:
            break
        else:
            print(country)

def iter_standard() -> None:
    print('----')
    countries:tuple = ("Germany", "France", "Italy", "Spain", "Portugal", "Greece")
    for country in countries:
        print(country)

def iter_from_iter() -> None:
    print('----')
    countries:tuple = ("Germany", "France", "Italy", "Spain", "Portugal", "Greece")
    country_iter = iter(countries)

    print(next(country_iter))
    iter_copy = iter(country_iter)
    print(next(iter_copy ))

def iter_file() -> None:
    print('----')
    with open('countries.txt', 'r') as file:
        for line in iter(file.readline, ""):
            print(line, end="")
    
def iter_dataclass() -> None:
    print('----')
    @dataclass(frozen=True)
    class LineItem:
        price: int
        qty: int

        def total_price(self) -> int:
            return self.price * self.qty

    def print_totals(items: Iterable[LineItem]) -> None:   
        for item in items:
            print(item.total_price())

    
    line_items:list = (
        LineItem(1,2),
        LineItem(3,4),
        LineItem(5,6),
    )

    print_totals(line_items)

def iter_myself() -> None:
    print('----')
    @dataclass
    class InfiniteNumberIterator:
        num:int = 0

        def __iter__(self):
            return self
        
        def __next__(self) -> int:
            self.num += 1 
            return self.num

    @dataclass
    class NumberIterator:
        max:int 
        num:int = 0

        def __iter__(self)  :
            return self
        
        def __next__(self) -> int:
            if self.num >= self.max:
                raise StopIteration
            self.num += 1 
            return self.num

    for num in NumberIterator(3):
        print(num)

if __name__ == "__main__":
    iter_raw()
    iter_standard()
    iter_from_iter()
    iter_file()
    iter_dataclass()
    iter_myself()