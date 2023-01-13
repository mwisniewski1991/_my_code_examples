import time
import operator
import functools
import dis

def add_1(numbers: list[float]) -> float:
    sum:float = 0
    for num in numbers:
        sum += num
    return sum

def add_2(numbers: list[float]) -> float:
    return functools.reduce(operator.add, numbers)

def add_3(numbers: list[float]) -> float:
    return sum(numbers)

# def add_4(numbers: list[float]) -> float:
#     return np.sum(numbers)


def execution() -> None:
    print('''
    
    
    ''')
    numbers: list = [i for i in range(90_000_000)]

    start_time = time.perf_counter()  # get the current time [start]
    print(add_1(numbers))
    end_time = time.perf_counter()  # get the current time [end]
    print(f"Duration add_1: {end_time - start_time } seconds") 

    start_time = time.perf_counter()  # get the current time [start]
    print(add_2(numbers))
    end_time = time.perf_counter()  # get the current time [end]
    print(f"Duration add_2: {end_time - start_time } seconds") 

    start_time = time.perf_counter()  # get the current time [start]
    print(add_3(numbers))
    end_time = time.perf_counter()  # get the current time [end]
    print(f"Duration add_3: {end_time - start_time } seconds") 

if __name__ == "__main__":
    # execution()
    
    dis.dis(add_1)
    print('---------------')
    dis.dis(add_2)
    print('---------------')
    dis.dis(add_3)