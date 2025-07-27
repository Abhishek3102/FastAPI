from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name : str
    email : EmailStr
    age : int
    weight : float
    marital_status : bool
    allergies : List[str]
    contact_details : Dict[str, str]

# this field validtor checks whether the email domain of patient is included in valid domains or not. this is a specific usecase in this situation, 
# where if patient's email in in valid domains then only they will get free treatment in this hospital
    @field_validator("email")
    @classmethod
    def email_validator(cls, value):
        valid_domains = ["hdfc.com", "icici.com"]
        # abc@gmail.com
        domain_name = value.split("@")[-1] # take the part after the @ from the email

        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")
        
        return value
    
    # this field validator helps in a field transformation which is to convert the patients' name into upper case.
    @field_validator("name")
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    

# the following error was given when before mode was used : TypeError: '<' not supported between instances of 'int' and 'str'
# this is because the value that was sent in field validator was before the type coercion. to remove this error, use mode = "after", this is the default mode too in all field validators
    @field_validator("age", mode="after")
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError("Provide valid age between 1 and 100")

def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.marital_status)
    print(patient.allergies)
    print(patient.contact_details)
    print("Updated the database")

patient_info = {"name" : "Quaresma", "email" : "user@hdfc.com", "age" : "39", "github_url" : "https://github.com/user", "weight" : 84.5, "marital_status" : True, "allergies" : ["pollen", "peanuts"], "contact_details" : { "phone" : "9723747742"}} 

patient1 = Patient(**patient_info)

update_patient_data(patient1)