from fastapi import FastAPI
from reading_service.routers import readings


app = FastAPI()

app.include_router(readings.readingRouter)
