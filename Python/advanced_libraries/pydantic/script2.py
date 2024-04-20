from datetime import datetime
from typing import Tuple, List, Dict
from pydantic import BaseModel, EmailStr, validator, field_validator, PositiveFloat, PositiveInt, Field

class User(BaseModel):
    name:str
    email:EmailStr
    account_id:int
    salary:PositiveFloat
    bonus: float = Field(ge=0, le=1)
    items: List[str] = Field(default_factory=list, max_items=2)
    skills: Dict[str, PositiveInt] = Field(default_factory=dict)

    @field_validator("account_id")
    def validate_account_id(cls, value):
        if value <= 0:
            raise ValueError(f"account_ud must be positive: {value}")
        return value
    
    class Config:
        validate_assignment = True



data = {
    'name': 'Pat',
    'email': 'pat@gmail.com',
    'account_id': 10,
    'salary': 123.12,
    'bonus': 0.5,
    'items': ['Laptop', 'mouse'],
    'skills': {'Python': 2}
}

data_str = '{"name": "Pat", "email": "pat@gmail.com","account_id": 10}'

user = User(name='Mat', email='m@gmail.com', account_id=2, salary=1234.00, bonus=0.1)
user2 = User(**data)

# user.salary = -123
# user3 = User.parse_raw(data_str)

print(user)
print()
print(user2)
# print(user2.json())
# print(user2.dict())
print()
# print(user3)
