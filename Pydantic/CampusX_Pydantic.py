def insert_patient_data(name, age):
# def insert_patient_data(name : str, age : int): here these data types are just to show the user, they don't give errors if not used as it is written
    
    # self made type validation. this works but is not scalable
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError("Age can't be ngative")
        else:
            print(name)
            print(age)
            print("Inserted into database")
    else:
        raise TypeError("Incorrect data type used")

# here age is sent in string, still it works bcoz there is no type validation in python
# insert_patient_data("user1", "sixty")


# now using pydantic, type, value validation is taken care of. 
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

# basemodel has to be included in the created class then only it will become a pydantic model
class Patient(BaseModel):
    name : Annotated[str, Field(max_length=50, title="Name of patient", description="Provide name of patient in less than 50 characters", examples=["Kaka", "Marcelo"])] 
    email : EmailStr # this validates the given email
    age : int = Field(gt = 0, lt=120) # range of age from 0 to 120
    github_url : AnyUrl
    weight : Annotated[float, Field(gt = 0, strict=True)] # only positive integers will be accepted and strict=True means auto type conversion will not happen here. like if user sends weight as string then it won't be converted to float unlike elsewhere when this condition is not used.
    marital_status : bool = True # default value is true
    allergies : Optional[List[str]] = Field(default=None, max_length=5) # this validates that allergies is a list with all strings inside it. this is an optional field rest all are required. Whenever declaring anything as optional, a default value has to be given. In this case it is none
    contact_details : Dict[str, str] # str, str means both key and value are string

patient_info = {"name" : "Quaresma", "email" : "user@gmail.com", "age" : 39, "github_url" : "https://github.com/user", "weight" : 84.5, "marital_status" : True, "allergies" : ["pollen", "peanuts"], "contact_details" : { "phone" : "9723747742"}} 

# When you see something like:
# patient1 = Patient(**patient_info)
# …it means : patient_info is a dictionary. the ** is called the unpack operator.

# The ** operator unpacks this dictionary into keyword arguments.
# So it's equivalent to calling:

# patient1 = Patient(name='John', age=30, condition='Flu') — assuming the dictionary contains those keys.
patient1 = Patient(**patient_info)

def insert_patient_data_pydantic(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.marital_status)
    print(patient.allergies)
    print(patient.contact_details)
    print("Inserted into database")

def update_patient_data_pydantic(patient : Patient):
    print(patient.name)
    print(patient.age)
    print("Updated the database!")

insert_patient_data_pydantic(patient1)
# update_patient_data_pydantic(patient1)

