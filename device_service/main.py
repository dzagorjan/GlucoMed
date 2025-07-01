from fastapi import FastAPI
from routers import devices


app = FastAPI()

app.include_router(devices.deviceRouter)
