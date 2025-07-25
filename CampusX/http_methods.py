from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
        return data

@app.get("/")
def hello():
    return {"message" : "Patient management system API"}

@app.get("/about")
def about_section():
    return {"message" : "Fully functional API to management patient data"}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
# the 3 dots (...) means that particular value is required, can't be empty
def view_patient(patient_id: str = Path(..., description="ID of patient in the DB", example="P001")):
    # load all patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    # return {"error": "Patient not found"}
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="Sort on the basis of height, weight or bmi"),
order: str = Query("asc", description="Sort in asc or desc order")):

    valid_fields = ["height", "weight", "bmi"]

# status code 400 -> bad request by client
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid Field. Select from {valid_fields}")
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order select. Select between ascending and descending only")
    
    data = load_data()

    sort_order = True if order=="desc" else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=False)