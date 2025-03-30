from pydantic import BaseModel, Field
from typing import Literal, Optional
from datetime import date, datetime


class DeviceBase(BaseModel):
    name: str = Field(..., description = "Name of the device. Like Glucose meter")
    manufacturer: Optional[str] = Field(None, description = "Manufacturer of device. Like AccuSure")
    model: Optional[str] = Field(None, description = "Model name or number. Like Simple")
    assigned_to_patient_id: Optional[str] = Field(None, description = "ID of the patient the device is assigned to")
    autonomy: Optional[str] = Field(None, description = "The autonomy of device in hours")
    battery_type: Optional[str] = Field(None, description = "Type of battery installed in device, Li-Ion, NiMh etc.")


class DeviceCreate(DeviceBase):
    pass


class DeviceResponse(DeviceBase):
    id: str = Field(..., description = "Unique indentifier of a device")


class DeviceUpdate(BaseModel):
    name: Optional[str]
    manufacturer: Optional[str]
    model: Optional[str]
    assigned_to_patient_id: Optional[str]
    autonomy: Optional[str]
    battery_type: Optional[str]