from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {'id': 101, 'name': "User404", 'is_active': False}

# The User model constructor expects individual keyword arguments like: User(id=101, name="User404", is_active=False)
# The ** operator(unpacking operator, specifically the double asterisk **, to unpack a dictionary into keyword arguments.) 
# unpacks the dictionary so that: User(**input_data) becomes equivalent to: User(id=101, name="User404", is_active=False)
# Without **, Python would treat the dictionary as a single positional argument: User(input_data)  # ❌ This will raise a ValidationError or TypeError

user = User(**input_data)
print(user)