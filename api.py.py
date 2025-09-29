# api.py
from typing import List
from fastapi import APIRouter, HTTPException, Depends, status, UploadFile, File
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas
import uuid
from datetime import datetime
import csv
from io import StringIO

# Create database tables (if they don't exist)
models.Base.metadata.create_all(bind=engine)

api_router = APIRouter()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Lead Endpoints --- #

@api_router.post("/leads/", response_model=schemas.Lead, status_code=status.HTTP_201_CREATED)
async def create_lead(lead: schemas.LeadCreate, db: Session = Depends(get_db)):
    """Creates a new lead."""
    db_lead = models.Lead(**lead.dict(), leadId=uuid.uuid4(), leadScore=0, createdAt=datetime.utcnow(), updatedAt=datetime.utcnow())
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    return db_lead

@api_router.get("/leads/{lead_id}", response_model=schemas.Lead)
async def read_lead(lead_id: uuid.UUID, db: Session = Depends(get_db)):
    """Retrieves a lead by ID."""
    db_lead = db.query(models.Lead).filter(models.Lead.leadId == lead_id).first()
    if db_lead is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lead not found")
    return db_lead

@api_router.put("/leads/{lead_id}", response_model=schemas.Lead)
async def update_lead(lead_id: uuid.UUID, lead: schemas.LeadCreate, db: Session = Depends(get_db)):
    """Updates a lead by ID."""
    db_lead = db.query(models.Lead).filter(models.Lead.leadId == lead_id).first()
    if db_lead is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lead not found")

    for key, value in lead.dict().items():
        setattr(db_lead, key, value)

    db_lead.updatedAt = datetime.utcnow()
    db.commit()
    db.refresh(db_lead)
    return db_lead

@api_router.delete("/leads/{lead_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_lead(lead_id: uuid.UUID, db: Session = Depends(get_db)):
    """Deletes a lead by ID."""
    db_lead = db.query(models.Lead).filter(models.Lead.leadId == lead_id).first()
    if db_lead is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lead not found")
    db.delete(db_lead)
    db.commit()
    return

@api_router.post("/leads/import")
async def import_leads(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """Imports leads from a CSV file."""
    if file.content_type != "text/csv":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid file type. Only CSV files are supported.")

    contents = await file.read()
    csv_data = StringIO(contents.decode())
    reader = csv.DictReader(csv_data)

    imported_count = 0
    errors = []

    for row in reader:
        try:
            lead_data = schemas.LeadCreate(**row)
            db_lead = models.Lead(**lead_data.dict(), leadId=uuid.uuid4(), leadScore=0, createdAt=datetime.utcnow(), updatedAt=datetime.utcnow())
            db.add(db_lead)
            imported_count += 1
        except Exception as e:
            errors.append(str(e))
            db.rollback()

    db.commit()
    return {"imported": imported_count, "errors": errors}

@api_router.post("/leads/{lead_id}/convert", response_model=schemas.Customer)
async def convert_lead(lead_id: uuid.UUID, db: Session = Depends(get_db)):
    """Converts a lead to a customer."""
    db_lead = db.query(models.Lead).filter(models.Lead.leadId == lead_id).first()
    if db_lead is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lead not found")

    customer_data = db_lead.__dict__
    del customer_data['_sa_instance_state']
    del customer_data['leadId']
    del customer_data['leadScore']
    del customer_data['createdAt']
    del customer_data['updatedAt']
    del customer_data['tags']

    db_customer = models.Customer(**customer_data, customerId=uuid.uuid4(), travelHistory=None, createdAt=datetime.utcnow(), updatedAt=datetime.utcnow())
    db.add(db_customer)
    db.delete(db_lead)
    db.commit()
    db.refresh(db_customer)
    return db_customer

# --- Customer Endpoints --- #

@api_router.post("/customers/", response_model=schemas.Customer, status_code=status.HTTP_201_CREATED)
async def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    """Creates a new customer."""
    db_customer = models.Customer(**customer.dict(), customerId=uuid.uuid4(), travelHistory=None, createdAt=datetime.utcnow(), updatedAt=datetime.utcnow())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@api_router.get("/customers/{customer_id}", response_model=schemas.Customer)
async def read_customer(customer_id: uuid.UUID, db: Session = Depends(get_db)):
    """Retrieves a customer by ID."""
    db_customer = db.query(models.Customer).filter(models.Customer.customerId == customer_id).first()
    if db_customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return db_customer

# --- Email Endpoints --- #

@api_router.post("/emails/", response_model=schemas.Email, status_code=status.HTTP_201_CREATED)
async def send_email(email: schemas.EmailCreate, db: Session = Depends(get_db)):
    """Sends an email."""
    # In a real application, you would integrate with an email provider here
    # For this example, we'll just simulate sending an email
    email_status = "sent" # Or "failed" based on the simulation
    db_email = models.Email(**email.dict(), emailId=uuid.uuid4(), status=email_status)
    db.add(db_email)
    db.commit()
    db.refresh(db_email)
    return db_email

# --- SMS Endpoints --- #

@api_router.post("/sms/", response_model=schemas.SMS, status_code=status.HTTP_201_CREATED)
async def send_sms(sms: schemas.SMSCreate, db: Session = Depends(get_db)):
    """Sends an SMS message."""
    # In a real application, you would integrate with an SMS gateway here
    # For this example, we'll just simulate sending an SMS
    sms_status = "sent" # Or "failed" based on the simulation
    db_sms = models.SMS(**sms.dict(), smsId=uuid.uuid4(), status=sms_status)
    db.add(db_sms)
    db.commit()
    db.refresh(db_sms)
    return db_sms

# --- Suggestion Endpoints --- #

@api_router.get("/suggestions/communication/{lead_id}")
async def get_communication_suggestions(lead_id: uuid.UUID):
    """Retrieves suggested communication messages for a lead."""
    # In a real application, this would call the Agentic Suggestion Engine
    # For this example, we'll just return some dummy data
    email_templates = [
        "Follow up on travel preferences",
        "Special offer for your dream destination"
    ]
    call_scripts = [
        "Inquire about their recent website activity",
        "Offer personalized travel recommendations"
    ]
    return {"emailTemplates": email_templates, "callScripts": call_scripts}
