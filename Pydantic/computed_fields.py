# here we will calculate bmi from the height and weight given by user. but since bmi itself is not given by user, and is calcualted
# using height and weight taken from user, therefore bmi is called a computed field.

from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name : str
    email : EmailStr
    age : int
    weight : float # weight in kg
    height : float # height in metres
    marital_status : bool
    allergies : List[str]
    contact_details : Dict[str, str]


    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi


def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.marital_status)
    print(patient.allergies)
    print(patient.contact_details)
    print("BMI : ", patient.bmi)
    print("Updated the database")

patient_info = {"name" : "Quaresma", "email" : "user@hdfc.com", "age" : "67", "height" : 1.67, "github_url" : "https://github.com/user", "weight" : 84.5, "marital_status" : True, "allergies" : ["pollen", "peanuts"], "contact_details" : { "phone" : "9723747742", "emergency" : "9374774321"}} 

patient1 = Patient(**patient_info)

update_patient_data(patient1)