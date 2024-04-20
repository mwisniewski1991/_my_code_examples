from datetime import datetime
from typing import Tuple, List
from pydantic import BaseModel

class Delivery(BaseModel):
    timestamp: datetime
    dimensions: Tuple[int, int]
    types: List[str]
    number: int


m = Delivery(timestamp='2020-01-02T03:04:05Z', 
            dimensions=[10, 20],
            types=['a', 'b', 'c'],
            number=1)


print(repr(m.timestamp))
print(m.dimensions)
print(m.types)
print(m.number)