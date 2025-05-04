from pydantic import BaseModel, Field
from typing import Literal, Optional
from datetime import datetime


class ReadingBase(BaseModel):
    patient_id: str = Field(..., description = "ID of the patient this reading belongs to")
    device_id: str = Field(..., description = "ID of the device that recorded this reading")
    glucose_level: float = Field(..., gt=0, description = "Measured glucose level")
    unit: Literal['mmol/L','mg/dL'] = Field('mmol/L', description = "Standard units for glucose level measurement")
    timestamp: datetime = Field(default_factory=datetime.now, description = "Date and time of measurement")
    note: Optional[str] = Field(None, description = "Optional notes for measurement")


class ReadingCreate(ReadingBase):
    pass


class ReadingResponse(ReadingBase):
    id: str = Field(..., description = "Unique indentifier for this reading")


class ReadingUpdate(BaseModel):
    glucose_level: Optional[float]
    unit: Optional[Literal['mmol/L','mg/dL']]
    timestamp: Optional[datetime]
    note: Optional[str]


    