from fastapi import FastAPI
from routers import readings


app = FastAPI()

app.include_router(readings.readingRouter)
