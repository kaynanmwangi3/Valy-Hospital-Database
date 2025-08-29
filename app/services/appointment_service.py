from sqlalchemy.orm import Session
from app.models import Appointment
from app.validators import validate_datetime

class AppointmentService:
    @staticmethod
    def create_appointment(db: Session, appointment_data: dict):
        """Create a new appointment"""
        # Validate input data
        appointment_date = validate_datetime(appointment_data['appointment_date'])
        
        # Create appointment instance
        appointment = Appointment(
            patient_id=appointment_data['patient_id'],
            staff_id=appointment_data['staff_id'],
            appointment_date=appointment_date,
            purpose=appointment_data.get('purpose', ''),
            status=appointment_data.get('status', 'Scheduled')
        )
        
        # Add to database
        db.add(appointment)
        db.commit()
        db.refresh(appointment)
        return appointment

    @staticmethod
    def get_appointment(db: Session, appointment_id: int):
        """Get appointment by ID"""
        return db.query(Appointment).filter(Appointment.id == appointment_id).first()

    @staticmethod
    def get_all_appointments(db: Session):
        """Get all appointments"""
        return db.query(Appointment).all()

    @staticmethod
    def get_patient_appointments(db: Session, patient_id: int):
        """Get all appointments for a specific patient"""
        return db.query(Appointment).filter(Appointment.patient_id == patient_id).all()

    @staticmethod
    def get_staff_appointments(db: Session, staff_id: int):
        """Get all appointments for a specific staff member"""
        return db.query(Appointment).filter(Appointment.staff_id == staff_id).all()

    @staticmethod
    def update_appointment(db: Session, appointment_id: int, update_data: dict):
        """Update appointment information"""
        appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
        if not appointment:
            return None
        
        # Update fields
        if 'appointment_date' in update_data:
            appointment.appointment_date = validate_datetime(update_data['appointment_date'])
        if 'purpose' in update_data:
            appointment.purpose = update_data['purpose']
        if 'status' in update_data:
            appointment.status = update_data['status']
        if 'patient_id' in update_data:
            appointment.patient_id = update_data['patient_id']
        if 'staff_id' in update_data:
            appointment.staff_id = update_data['staff_id']
        
        db.commit()
        db.refresh(appointment)
        return appointment

    @staticmethod
    def delete_appointment(db: Session, appointment_id: int):
        """Delete an appointment"""
        appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
        if appointment:
            db.delete(appointment)
            db.commit()
            return True
        return False