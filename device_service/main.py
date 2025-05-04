from fastapi import FastAPI
from device_service.routers import devices


app = FastAPI()

app.include_router(devices.deviceRouter)
