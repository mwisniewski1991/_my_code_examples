
# Use @property for providing Read-Only attributes
class WriteCoordinateError(Exception):
    pass

class Point:
    def __init__(self, x:int, y:int) -> None:
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        raise WriteCoordinateError("x coordinate is read-only")

    @property
    def y(self):
        return self._y
    
    @x.setter
    def y(self, value):
        raise WriteCoordinateError("y coordinate is read-only")

    
# point = Point(10, 5)
# print(point.x)
# point.x = 10



# Use @property for providing Write-Only attributes
import hashlib
import os

class User:
    def __init__(self, name:str, password:str) -> None:
        self.name = name
        self.password = password

    @property
    def password(self):
        raise AttributeError("Password is write-only")

    @password.setter
    def password(self, plaintext):
        salt = os.urandom(32)
        self._hashed_password = hashlib.pbkdf2_hmac("sha256", plaintext.encode("utf-8"), salt, 100_00)

        
mat = User('mat', 'pass123456')
print(mat._hashed_password)
# print(mat.password)

mat.password = "123"
print(mat._hashed_password)
