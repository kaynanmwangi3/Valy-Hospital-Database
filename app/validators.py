import re
from datetime import datetime

def validate_name(name):
    """Validate name contains only letters and spaces"""
    if not re.match(r'^[a-zA-Z\s]+$', name):
        raise ValueError("Name can only contain letters and spaces")
    return name.strip()

def validate_email(email):
    """Validate email format"""
    if email and not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        raise ValueError("Invalid email format")
    return email
def validate_phone(phone):
    """Validate phone number format"""
    if not re.match(r'^\+?[0-9]{10,15}$', phone):
        raise ValueError("Phone number must be 10-15 digits, optionally starting with +")
    return phone

def validate_date(date_str):
    """Validate date format (YYYY-MM-DD)"""
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format")

def validate_datetime(datetime_str):
    """Validate datetime format (YYYY-MM-DD HH:MM)"""
    try:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
    except ValueError:
        raise ValueError("Datetime must be in YYYY-MM-DD HH:MM format")

def validate_gender(gender):
    """Validate gender input"""
    valid_genders = ['Male', 'Female', 'Other']
    if gender not in valid_genders:
        raise ValueError(f"Gender must be one of: {', '.join(valid_genders)}")
    return gender

def validate_positive_number(value, field_name):
    """Validate that a value is a positive number"""
    try:
        num = float(value)
        if num <= 0:
            raise ValueError(f"{field_name} must be a positive number")
        return num
    except ValueError:
        raise ValueError(f"{field_name} must be a valid number")