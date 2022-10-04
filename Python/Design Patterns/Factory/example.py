from abc import ABCMeta, ABC, abstractmethod
from dataclasses import make_dataclass
from telnetlib import IP
from time import perf_counter

class IPerson(ABC):

    @abstractmethod
    def person_method(self):
        """Inferance Method"""

class Student(IPerson):
    def __init__(self) -> None:
        self.name = 'Student'

    def person_method(self):
        print('I am a student !!!')

class Teacher(IPerson):
    def __init__(self) -> None:
        self.name = 'Techer'

    def person_method(self):
        print('I am a teacher !!!')

class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == 'student':
            return Student()
        if person_type == 'teacher':
            return Teacher()
        print('Invalid type')
        return None        
    

if __name__ == '__main__':
    choice = input('What person do you want to create?')
    person = PersonFactory.build_person(choice)
    person.person_method()