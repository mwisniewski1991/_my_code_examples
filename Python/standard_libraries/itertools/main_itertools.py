import itertools

def itertools_count() -> None:
    print("----")
    for i in itertools.count(10):
        print(i)
        if i == 15:
            break

def itertools_repeat() -> None:
    print("----")
    for i in itertools.repeat(5, 5):
        print(i)

def itertools_acumulate() -> None:
    print("----")
    for i in itertools.accumulate(range(1,11)):
        print(i)

def itertools_permutations() ->   None:
    print("----")
    items:list = ["A", "B", "C"]
    permi = itertools.permutations(items)

    for i in permi:
        print(i)

def itertools_combinations() -> None:
    print("----")
    items:list = ["A", "B", "C"]
    combinations = itertools.combinations(items, 2)

    for i in combinations:
        print(i)

def itertools_combinations_with_replacement() -> None:
    print("----")
    items:list = ["A", "B", "C"]
    combinations = itertools.combinations_with_replacement(items, 2)

    # for i in combinations:
    #     print(i)
    print(list(combinations))

def itertools_chain() -> None:
    print("----")
    items:list = ["A", "B", "C"]
    more_items:list = ["D", "E", "F"]

    chain = itertools.chain(items, more_items)
    print(list(chain))

def itertools_others() -> None:
    print("----")
    items:list = ["A", "B", "C"]
    more_items:list = ["D", "E", "F"]

    filterfalse = itertools.filterfalse(lambda x: x % 2  == 0, range(10))
    print(list(filterfalse))

    takewhile = itertools.takewhile(lambda x: x % 2  == 0, range(10))
    print(list(takewhile))

    starmap = itertools.starmap(lambda x,y: x * y, [(2,6), (3,7), (4,8)])
    print(list(starmap))


if __name__ == "__main__":
    itertools_count()
    itertools_repeat()
    itertools_acumulate()
    itertools_permutations()
    itertools_combinations()
    itertools_combinations_with_replacement()
    itertools_chain()
    itertools_others()