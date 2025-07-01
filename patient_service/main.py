from fastapi import FastAPI
from routers import patients
#from dotenv import load_dotenv

#load_dotenv()


app = FastAPI()

app.include_router(patients.patientRouter)


