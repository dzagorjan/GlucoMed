from fastapi import APIRouter, HTTPException
from typing import List
from uuid import uuid4
from db import table
from models.Device import DeviceCreate, DeviceResponse, DeviceUpdate


deviceRouter = APIRouter()


#Create new device
@deviceRouter.post("/devices", response_model=DeviceResponse)
async def create_device(device: DeviceCreate):
    device_id=str(uuid4())
    device_item={"id": device_id, **device.model_dump()}
    print("Saving item to DynamoDB:", device_item)
    table.put_item(Item=device_item)
    return device_item

#Get all devices
@deviceRouter.get("/devices", response_model=List[DeviceResponse])
async def get_all_devices():
    response = table.scan()
    devices = response.get("Items", [])
    return devices


#Get device by ID
@deviceRouter.get("/devices/{device_id}", response_model=DeviceResponse)
async def get_device(device_id: str):
    response = table.get_item(Key={"id": device_id})
    device = response.get("Item")
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device


#Update device by ID
@deviceRouter.put("/{device_id}", response_model=DeviceResponse)
async def update_device(device_id:str, device_update: DeviceUpdate):
    # Get existing device
    existing = table.get_item(Key={"id": device_id}).get("Item")
    if not existing:
        raise HTTPException(status_code=404, detail="Device not found")

    # Update only sent fields 
    updated_data = device_update.model_dump(exclude_unset=True)
    updated_device = {**existing, **updated_data}
    table.put_item(Item=updated_device)

    return updated_device


#Delete device by ID
@deviceRouter.delete("/{device_id}")
async def delete_device(device_id: str):
    response = table.get_item(Key={"id": device_id})
    device = response.get("Item")
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")

    table.delete_item(Key={"id": device_id})
    return{"message": f"Device with id {device_id} has been successfully deleted."}








