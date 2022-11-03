
# Use @property for providing Read-Only attributes
class WriteCoordinateError(Exception):
    pass

class Point:
    def __init__(self, x:int, y:int) -> None:
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int) -> None:
        raise WriteCoordinateError("x coordinate is read-only")

    @property
    def y(self) -> int:
        return self._y
    
    @y.setter
    def y(self, value: int) -> None:
        raise WriteCoordinateError("y coordinate is read-only")

    
point = Point(10, 5)
print(point.x)
point.x = 10 #This line cause error. x and y can not be change.


# Use @property for providing Write-Only attributes
import hashlib
import os

class User:
    def __init__(self, name:str, password:str) -> None:
        self.name = name
        self.password = password

    @property
    def password(self) -> None:
        raise AttributeError("Password is write-only")

    @password.setter
    def password(self, plaintext: str) -> None:
        salt = os.urandom(32)
        self._hashed_password = hashlib.pbkdf2_hmac("sha256", plaintext.encode("utf-8"), salt, 100_00)

        
mat = User('mat', 'pass123456')
print(mat._hashed_password)
print(mat.password) #This line cause error. Password can only be change. User can not read this.

mat.password = "123"
print(mat._hashed_password)