from pydantic import BaseModel

class Address(BaseModel):
    city  :str
    state : str
    pin : str

class Patient(BaseModel):
    name : str
    gender : str
    age : int
    address : Address # here address takes value from another model Address which is made above. This is done so that any part of address can be extracted easily without complications which would have arised if address was also in the same model.

address_dict = {"city" : "Howrah", "state" : "West Bengal", "pin" : "700002"}

address1 = Address(**address_dict)

patient_dict = {"name" : "Abhi", "gender" : "male", "age" : 22, "address" : address1}

patient1 = Patient(**patient_dict)

print(patient1) # output = name='Abhi' gender='male' age=22 address=Address(city='Howrah', state='West Bengal', pin='700002')

print(patient1.address.city) # output = Howrah

temp = patient1.model_dump()
temp2 = patient1.model_dump_json() # this converts model to json whose type is string
print(temp) # output = {'name': 'Abhi', 'gender': 'male', 'age': 22, 'address': {'city': 'Howrah', 'state': 'West Bengal', 'pin': '700002'}}
print(type(temp)) # output = <class "dict">


# # (method) def model_dump(
#     *,
#     mode: str | Literal['json', 'python'] = 'python',
#     include: IncEx | None = None,
#     exclude: IncEx | None = None,
#     context: Any | None = None,
#     by_alias: bool = False,
#     exclude_unset: bool = False,
#     exclude_defaults: bool = False,
#     exclude_none: bool = False,
#     round_trip: bool = False,
#     warnings: bool | Literal['none', 'warn', 'error'] = True,
#     serialize_as_any: bool = False
# ) -> dict[str, Any]
# Usage docs: https://docs.pydantic.dev/2.10/concepts/serialization/#modelmodel_dump

# Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

# Args
# mode
# The mode in which to_python should run. If mode is 'json', the output will only contain JSON serializable types. If mode is 'python', the output may contain non-JSON-serializable Python objects.

# include
# A set of fields to include in the output.

# exclude
# A set of fields to exclude from the output.

# context
# Additional context to pass to the serializer.

# by_alias
# Whether to use the field's alias in the dictionary key if defined.

# exclude_unset
# Whether to exclude fields that have not been explicitly set.

# exclude_defaults
# Whether to exclude fields that are set to their default value.

# exclude_none
# Whether to exclude fields that have a value of None.

# round_trip
# If True, dumped values should be valid as input for non-idempotent types such as Json[T].

# warnings
# How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors, "error" raises a [PydanticSerializationError][pydantic_core.PydanticSerializationError].

# serialize_as_any
# Whether to serialize fields with duck-typing serialization behavior.

# Returns
# out
# A dictionary representation of the model.