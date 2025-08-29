from sqlalchemy.orm import Session
from app.models import Patient
from app.validators import validate_name, validate_email, validate_phone, validate_date, validate_gender
from datetime import date

class PatientService:
    @staticmethod
    def create_patient(db: Session, patient_data: dict):
        """Create a new patient"""
        # Validate input data
        first_name = validate_name(patient_data['first_name'])
        last_name = validate_name(patient_data['last_name'])
        date_of_birth = validate_date(patient_data['date_of_birth'])
        gender = validate_gender(patient_data['gender'])
        contact_number = validate_phone(patient_data['contact_number'])
        email = validate_email(patient_data.get('email', ''))
        
        # Create patient instance
        patient = Patient(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            gender=gender,
            contact_number=contact_number,
            email=email,
            address=patient_data.get('address', '')
        )
        
        # Add to database
        db.add(patient)
        db.commit()
        db.refresh(patient)
        return patient

    @staticmethod
    def get_patient(db: Session, patient_id: int):
        """Get patient by ID"""
        return db.query(Patient).filter(Patient.id == patient_id).first()

    @staticmethod
    def get_all_patients(db: Session):
        """Get all patients"""
        return db.query(Patient).all()

    @staticmethod
    def search_patients(db: Session, search_term: str):
        """Search patients by name"""
        return db.query(Patient).filter(
            (Patient.first_name.ilike(f"%{search_term}%")) | 
            (Patient.last_name.ilike(f"%{search_term}%"))
        ).all()

    @staticmethod
    def update_patient(db: Session, patient_id: int, update_data: dict):
        """Update patient information"""
        patient = db.query(Patient).filter(Patient.id == patient_id).first()
        if not patient:
            return None
        
        # Validate and update fields
        if 'first_name' in update_data:
            patient.first_name = validate_name(update_data['first_name'])
        if 'last_name' in update_data:
            patient.last_name = validate_name(update_data['last_name'])
        if 'date_of_birth' in update_data:
            patient.date_of_birth = validate_date(update_data['date_of_birth'])
        if 'gender' in update_data:
            patient.gender = validate_gender(update_data['gender'])
        if 'contact_number' in update_data:
            patient.contact_number = validate_phone(update_data['contact_number'])
        if 'email' in update_data:
            patient.email = validate_email(update_data.get('email', ''))
        if 'address' in update_data:
            patient.address = update_data['address']
        
        db.commit()
        db.refresh(patient)
        return patient

    @staticmethod
    def delete_patient(db: Session, patient_id: int):
        """Delete a patient"""
        patient = db.query(Patient).filter(Patient.id == patient_id).first()
        if patient:
            db.delete(patient)
            db.commit()
            return True
        return False