from fastapi import APIRouter, HTTPException
from typing import List
from uuid import uuid4
from decimal import Decimal
from db import table
from models.Reading import ReadingCreate, ReadingResponse, ReadingUpdate


readingRouter = APIRouter()


#Create new reading
@readingRouter.post("/readings", response_model=ReadingResponse)
async def create_reading(reading: ReadingCreate):
    reading_id=str(uuid4())
    reading_data=reading.model_dump()
    
    reading_data["id"] = reading_id
    reading_data["timestamp"] = reading.timestamp.isoformat()
    reading_data["glucose_level"] = Decimal(str(reading_data["glucose_level"]))
    print("Saving item to DynamoDB:", reading_data)

    table.put_item(Item=reading_data)
    return reading_data

    #reading_id=str(uuid4())
    #reading_item={"id": reading_id, **reading.model_dump()}
    #print("Saving item to DynamoDB:", reading_item)
    #table.put_item(Item=reading_item)
    #return reading_item


#Get all readings
@readingRouter.get("/readings", response_model=List[ReadingResponse])
async def get_all_readings():
    response = table.scan()
    readings = response.get("Items", [])
    return readings


#Get reading by ID
@readingRouter.get("/readings/{reading_id}", response_model=ReadingResponse)
async def get_reading(reading_id: str):
    response = table.get_item(Key={"id": reading_id})
    reading = response.get("Item")
    if not reading:
        raise HTTPException(status_code=404, detail="Reading not found")
    return reading


#Update reading by ID
@readingRouter.put("/{reading_id}", response_model=ReadingResponse)
async def update_reading(reading_id: str, reading_update: ReadingUpdate):
    # Get existing reading
    existing = table.get_item(Key={"id": reading_id}).get("Item")
    if not existing:
        raise HTTPException(status_code=404, detail="Reading not found")

    # Update only sent fields 
    updated_data = reading_update.model_dump(exclude_unset=True)
    updated_reading = {**existing, **updated_data}
    table.put_item(Item=updated_reading)

    return updated_reading


#Delete reading by ID
@readingRouter.delete("/{reading_id}")
async def delete_reading(reading_id: str):
    response = table.get_item(Key={"id": reading_id})
    reading = response.get("Item")
    if not reading:
        raise HTTPException(status_code=404, detail="Reading not found")

    table.delete_item(Key={"id": reading_id})
    return{"message": f"Reading with id {reading_id} has been successfully deleted."}








