from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name : str
    email : EmailStr
    age : int
    weight : float
    marital_status : bool
    allergies : List[str]
    contact_details : Dict[str, str]

    @model_validator(mode="after")
    def validate_emergency_contact(cls, model):
        if model.age > 60 and "emergency" not in model.contact_details:
            raise ValueError("Patients older than 60 yrs. of age must have an emergency contact in their contact details")
        
        return model
        

def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.marital_status)
    print(patient.allergies)
    print(patient.contact_details)
    print("Updated the database")

patient_info = {"name" : "Quaresma", "email" : "user@hdfc.com", "age" : "67", "github_url" : "https://github.com/user", "weight" : 84.5, "marital_status" : True, "allergies" : ["pollen", "peanuts"], "contact_details" : { "phone" : "9723747742", "emergency" : "9374774321"}} 

patient1 = Patient(**patient_info)

update_patient_data(patient1)