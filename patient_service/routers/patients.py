from fastapi import APIRouter, HTTPException
from typing import List
from uuid import uuid4
from patient_service.db import table
from patient_service.models.Patient import PatientCreate, PatientResponse, PatientUpdate


patientRouter = APIRouter()


#Create new patient
@patientRouter.post("/patient", response_model=PatientResponse)
async def create_patient(patient: PatientCreate):
    patient_id=str(uuid4())
    patient={"id": patient_id, **patient.model_dump()}
    table.put_item(Item=patient)
    return patient


#Get all patients
@patientRouter.get("/patients", response_model=List[PatientResponse])
async def get_all_patients():
    response = table.scan()
    patients = response.get("Items", [])
    return patients


#Get patient by ID
@patientRouter.get("/patients/{patient_id}", response_model=PatientResponse)
async def get_patient(patient_id: str):
    response = table.get_item(Key={"id": patient_id})
    patient = response.get("Item")
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


#Update patient by ID
@patientRouter.put("/{patient_id}", response_model=PatientResponse)
async def update_patient(patient_id: str, patient_update: PatientUpdate):
    # Get existing patient
    existing = table.get_item(Key={"id": patient_id}).get("Item")
    if not existing:
        raise HTTPException(status_code=404, detail="Patient not found")

    # Update only sent fields 
    updated_data = patient_update.model_dump(exclude_unset=True)
    updated_patient = {**existing, **updated_data}
    table.put_item(Item=updated_patient)

    return updated_patient


#Delete patient by ID
@patientRouter.delete("/{patient_id}")
async def delete_patient(patient_id: str):
    response = table.get_item(Key={"id": patient_id})
    patient = response.get("Item")
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    table.delete_item(Key={"id": patient_id})
    return{"message": f"Patient with id {patient_id} has been successfully deleted."}








