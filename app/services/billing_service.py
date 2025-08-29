from sqlalchemy.orm import Session
from app.models import Bill
from app.validators import validate_date, validate_positive_number
from datetime import date, timedelta

class BillingService:
    @staticmethod
    def create_bill(db: Session, bill_data: dict):
        """Create a new bill"""
        # Validate input data
        amount = validate_positive_number(bill_data['amount'], "Amount")
        due_date = validate_date(bill_data['due_date']) if bill_data.get('due_date') else None
        
        # Create bill instance
        bill = Bill(
            patient_id=bill_data['patient_id'],
            amount=amount,
            due_date=due_date,
            description=bill_data.get('description', ''),
            status=bill_data.get('status', 'Unpaid')
        )
        
        # Add to database
        db.add(bill)
        db.commit()
        db.refresh(bill)
        return bill

    @staticmethod
    def get_bill(db: Session, bill_id: int):
        """Get bill by ID"""
        return db.query(Bill).filter(Bill.id == bill_id).first()

    @staticmethod
    def get_all_bills(db: Session):
        """Get all bills"""
        return db.query(Bill).all()

    @staticmethod
    def get_patient_bills(db: Session, patient_id: int):
        """Get all bills for a specific patient"""
        return db.query(Bill).filter(Bill.patient_id == patient_id).all()

    @staticmethod
    def get_unpaid_bills(db: Session):
        """Get all unpaid bills"""
        return db.query(Bill).filter(Bill.status == 'Unpaid').all()

    @staticmethod
    def update_bill(db: Session, bill_id: int, update_data: dict):
        """Update bill information"""
        bill = db.query(Bill).filter(Bill.id == bill_id).first()
        if not bill:
            return None
        
        # Update fields
        if 'amount' in update_data:
            bill.amount = validate_positive_number(update_data['amount'], "Amount")
        if 'due_date' in update_data:
            bill.due_date = validate_date(update_data['due_date']) if update_data['due_date'] else None
        if 'description' in update_data:
            bill.description = update_data['description']
        if 'status' in update_data:
            bill.status = update_data['status']
        
        db.commit()
        db.refresh(bill)
        return bill

    @staticmethod
    def mark_as_paid(db: Session, bill_id: int):
        """Mark a bill as paid"""
        bill = db.query(Bill).filter(Bill.id == bill_id).first()
        if bill:
            bill.status = 'Paid'
            db.commit()
            db.refresh(bill)
            return bill
        return None

    @staticmethod
    def delete_bill(db: Session, bill_id: int):
        """Delete a bill"""
        bill = db.query(Bill).filter(Bill.id == bill_id).first()
        if bill:
            db.delete(bill)
            db.commit()
            return True
        return False