# models.py
from typing import List, Optional
from pydantic import BaseModel, EmailStr, validator
import uuid
from datetime import date, datetime

# --- Data Structures --- #

class LeadBase(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    phone: str
    travelPreferences: Optional[str] = None
    source: Optional[str] = None

class LeadCreate(LeadBase):
    pass

class Lead(LeadBase):
    leadId: uuid.UUID
    leadScore: int
    tags: List[str] = []
    createdAt: datetime
    updatedAt: datetime

    class Config:
        orm_mode = True

class CustomerBase(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    phone: str
    preferences: Optional[str] = None

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    customerId: uuid.UUID
    travelHistory: Optional[str] = None
    createdAt: datetime
    updatedAt: datetime

    class Config:
        orm_mode = True

class BookingBase(BaseModel):
    customerId: uuid.UUID
    bookingDate: date
    destination: str
    travelDates: date
    bookingStatus: str

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    bookingId: uuid.UUID

    class Config:
        orm_mode = True

class EmailBase(BaseModel):
    recipient: EmailStr
    subject: str
    body: str

class EmailCreate(EmailBase):
    pass

class Email(EmailBase):
    emailId: uuid.UUID
    status: str # "sent" | "failed"

    class Config:
        orm_mode = True

class SMSBase(BaseModel):
    recipient: str # Phone number
    body: str

class SMSCreate(SMSBase):
    pass

class SMS(SMSBase):
    smsId: uuid.UUID
    status: str # "sent" | "failed"

    class Config:
        orm_mode = True

# --- Validation Examples --- #

# Example of custom validator (can be added to any BaseModel)
# class LeadCreate(LeadBase):
#     @validator('phone')
#     def phone_must_be_valid(cls, phone):
#         # Implement phone number validation logic here
#         if not phone.startswith('+'):
#             raise ValueError('Phone number must start with +')
#         return phone
