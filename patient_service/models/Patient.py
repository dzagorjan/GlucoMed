from pydantic import BaseModel, EmailStr, Field
from typing import Literal, Optional
from datetime import date, datetime


class PatientBase(BaseModel):
    name: str = Field(..., description = "Name of the patient")
    date_of_birth: Optional[date] = Field(None, description = "Date of birth of the patient")
    gender: Optional[Literal['Male','Female','Other']] = Field('Other', description = "Gender of the patient, Male, Female or Other")
    email: Optional[EmailStr] = Field(None, description = "Email of the patient")
    phone: Optional[str] = Field(None, description = "Patient's phone number")
    address: Optional[str] = Field(None, description = "Patient's address")


class PatientCreate(PatientBase):
    pass


class PatientResponse(PatientBase):
    id: str = Field(..., description = "Unique indentifier of a patient")


class PatientUpdate(BaseModel):
    name: Optional[str]
    date_of_birth: Optional[date]
    gender: Optional[str]
    email: Optional[EmailStr]
    phone: Optional[str]
    address: Optional[str]
    