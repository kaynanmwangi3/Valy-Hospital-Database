from sqlalchemy.orm import Session
from app.models import MedicalRecord
from app.validators import validate_date
from datetime import date, timedelta

class MedicalRecordService:
    @staticmethod
    def create_medical_record(db: Session, record_data: dict):
        #Create a new medical record
        # Validate input data
        admission_date = validate_date(record_data['admission_date']) if record_data.get('admission_date') else None
        discharge_date = validate_date(record_data['discharge_date']) if record_data.get('discharge_date') else None
        
        # Calculate duration of stay if both dates are provided
        duration_of_stay = None
        if admission_date and discharge_date:
            duration_of_stay = (discharge_date - admission_date).days
        
        # Create medical record instance
        record = MedicalRecord(
            patient_id=record_data['patient_id'],
            staff_id=record_data['staff_id'],
            diagnosis=record_data['diagnosis'],
            treatment=record_data.get('treatment', ''),
            admission_date=admission_date,
            discharge_date=discharge_date,
            duration_of_stay=duration_of_stay,
            medications=record_data.get('medications', ''),
            notes=record_data.get('notes', '')
        )
        
        # Add to database
        db.add(record)
        db.commit()
        db.refresh(record)
        return record

    @staticmethod
    def get_medical_record(db: Session, record_id: int):
        #Get medical record by ID
        return db.query(MedicalRecord).filter(MedicalRecord.id == record_id).first()

    @staticmethod
    def get_all_medical_records(db: Session):
        #Get all medical records
        return db.query(MedicalRecord).all()

    @staticmethod
    def get_patient_medical_records(db: Session, patient_id: int):
        #Get all medical records for a specific patient
        return db.query(MedicalRecord).filter(MedicalRecord.patient_id == patient_id).all()

    @staticmethod
    def update_medical_record(db: Session, record_id: int, update_data: dict):
        #Update medical record information
        record = db.query(MedicalRecord).filter(MedicalRecord.id == record_id).first()
        if not record:
            return None
        
        # Update fields
        if 'diagnosis' in update_data:
            record.diagnosis = update_data['diagnosis']
        if 'treatment' in update_data:
            record.treatment = update_data['treatment']
        if 'medications' in update_data:
            record.medications = update_data['medications']
        if 'notes' in update_data:
            record.notes = update_data['notes']
        if 'admission_date' in update_data:
            record.admission_date = validate_date(update_data['admission_date']) if update_data['admission_date'] else None
        if 'discharge_date' in update_data:
            record.discharge_date = validate_date(update_data['discharge_date']) if update_data['discharge_date'] else None
        
        # Recalculate duration of stay if dates are updated
        if ('admission_date' in update_data or 'discharge_date' in update_data) and record.admission_date and record.discharge_date:
            record.duration_of_stay = (record.discharge_date - record.admission_date).days
        else:
            record.duration_of_stay = None
        
        db.commit()
        db.refresh(record)
        return record

    @staticmethod
    def delete_medical_record(db: Session, record_id: int):
        #Delete a medical record
        record = db.query(MedicalRecord).filter(MedicalRecord.id == record_id).first()
        if record:
            db.delete(record)
            db.commit()
            return True
        return False