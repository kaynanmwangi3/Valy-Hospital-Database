from sqlalchemy.orm import Session
from app.models import Staff
from app.validators import validate_name, validate_email, validate_phone, validate_date

class StaffService:
    @staticmethod
    def create_staff(db: Session, staff_data: dict):
        """Create a new staff member"""
        # Validate input data
        first_name = validate_name(staff_data['first_name'])
        last_name = validate_name(staff_data['last_name'])
        contact_number = validate_phone(staff_data['contact_number'])
        email = validate_email(staff_data.get('email', ''))
        hire_date = validate_date(staff_data.get('hire_date')) if staff_data.get('hire_date') else None
        
        # Create staff instance
        staff = Staff(
            first_name=first_name,
            last_name=last_name,
            role=staff_data['role'],
            department=staff_data.get('department', ''),
            contact_number=contact_number,
            email=email,
            hire_date=hire_date
        )
        
        # Add to database
        db.add(staff)
        db.commit()
        db.refresh(staff)
        return staff

    @staticmethod
    def get_staff(db: Session, staff_id: int):
        """Get staff by ID"""
        return db.query(Staff).filter(Staff.id == staff_id).first()

    @staticmethod
    def get_all_staff(db: Session):
        """Get all staff members"""
        return db.query(Staff).all()

    @staticmethod
    def search_staff(db: Session, search_term: str):
        """Search staff by name or role"""
        return db.query(Staff).filter(
            (Staff.first_name.ilike(f"%{search_term}%")) | 
            (Staff.last_name.ilike(f"%{search_term}%")) |
            (Staff.role.ilike(f"%{search_term}%"))
        ).all()

    @staticmethod
    def update_staff(db: Session, staff_id: int, update_data: dict):
        """Update staff information"""
        staff = db.query(Staff).filter(Staff.id == staff_id).first()
        if not staff:
            return None
        
        # Validate and update fields
        if 'first_name' in update_data:
            staff.first_name = validate_name(update_data['first_name'])
        if 'last_name' in update_data:
            staff.last_name = validate_name(update_data['last_name'])
        if 'contact_number' in update_data:
            staff.contact_number = validate_phone(update_data['contact_number'])
        if 'email' in update_data:
            staff.email = validate_email(update_data.get('email', ''))
        if 'role' in update_data:
            staff.role = update_data['role']
        if 'department' in update_data:
            staff.department = update_data['department']
        if 'hire_date' in update_data:
            staff.hire_date = validate_date(update_data['hire_date'])
        
        db.commit()
        db.refresh(staff)
        return staff

    @staticmethod
    def delete_staff(db: Session, staff_id: int):
        """Delete a staff member"""
        staff = db.query(Staff).filter(Staff.id == staff_id).first()
        if staff:
            db.delete(staff)
            db.commit()
            return True
        return False