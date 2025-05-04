from fastapi import FastAPI
from patient_service.routers import patients


app = FastAPI()

app.include_router(patients.patientRouter)


