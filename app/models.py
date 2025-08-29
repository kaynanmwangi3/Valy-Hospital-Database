from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String(10), nullable=False)
    contact_number = Column(String(15), nullable=False)
    email = Column(String(100))
    address = Column(String(200))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    appointments = relationship("Appointment", back_populates="patient")
    medical_records = relationship("MedicalRecord", back_populates="patient")
    bills = relationship("Bill", back_populates="patient")
    
    def __repr__(self):
        return f"<Patient(id={self.id}, name={self.first_name} {self.last_name})>"

class Staff(Base):
    __tablename__ = 'staff'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    role = Column(String(50), nullable=False)  # Doctor, Nurse, Admin, etc.
    department = Column(String(50))
    contact_number = Column(String(15), nullable=False)
    email = Column(String(100))
    hire_date = Column(Date, default=datetime.utcnow)
    
    # Relationships
    appointments = relationship("Appointment", back_populates="staff")
    medical_records = relationship("MedicalRecord", back_populates="staff")
    
    def __repr__(self):
        return f"<Staff(id={self.id}, name={self.first_name} {self.last_name}, role={self.role})>"

class Appointment(Base):
    __tablename__ = 'appointments'
    
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    staff_id = Column(Integer, ForeignKey('staff.id'), nullable=False)
    appointment_date = Column(DateTime, nullable=False)
    purpose = Column(String(200))
    status = Column(String(20), default="Scheduled")  # Scheduled, Completed, Cancelled
    
    # Relationships
    patient = relationship("Patient", back_populates="appointments")
    staff = relationship("Staff", back_populates="appointments")
    
    def __repr__(self):
        return f"<Appointment(id={self.id}, patient_id={self.patient_id}, date={self.appointment_date})>"

class MedicalRecord(Base):
    __tablename__ = 'medical_records'
    
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    staff_id = Column(Integer, ForeignKey('staff.id'), nullable=False)
    diagnosis = Column(String(200), nullable=False)
    treatment = Column(String(500))
    admission_date = Column(Date)
    discharge_date = Column(Date)
    duration_of_stay = Column(Integer)  # in days
    medications = Column(String(500))
    notes = Column(String(1000))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    patient = relationship("Patient", back_populates="medical_records")
    staff = relationship("Staff", back_populates="medical_records")
    
    def __repr__(self):
        return f"<MedicalRecord(id={self.id}, patient_id={self.patient_id}, diagnosis={self.diagnosis})>"

class Bill(Base):
    __tablename__ = 'bills'
    
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    amount = Column(Float, nullable=False)
    date_issued = Column(Date, default=datetime.utcnow)
    due_date = Column(Date)
    status = Column(String(20), default="Unpaid")  # Paid, Unpaid
    description = Column(String(500))
    
    # Relationships
    patient = relationship("Patient", back_populates="bills")
    
    def __repr__(self):
        return f"<Bill(id={self.id}, patient_id={self.patient_id}, amount={self.amount}, status={self.status})>"