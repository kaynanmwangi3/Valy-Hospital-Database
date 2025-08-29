# important import modules
import re
from datetime import datetime

# name validation using regex patterns to allow letters and spaces only
def validate_name(name):
    if not re.match(r'^[a-zA-Z\s]+$', name):
        raise ValueError("Name can only contain letters and spaces")
    return name.strip()

# email validation using regex patterns allows letters, numbers and special characters and a value top level dormain name must be atleast 2 letters long
def validate_email(email):
    if email and not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        raise ValueError("Invalid email format")
    return email

# phone number validation using regex patterns to ensure number must be atleast 10 numbers long
def validate_phone(phone):
    if not re.match(r'^\+?[0-9]{10,15}$', phone):
        raise ValueError("Phone number must be 10-15 digits, optionally starting with +")
    return phone

# date validator format (YYYY-MM-DD)
def validate_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format")

# date time validator format (YYYY-MM-DD HH:MM)
def validate_datetime(datetime_str):
    try:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
    except ValueError:
        raise ValueError("Datetime must be in YYYY-MM-DD HH:MM format")

# Gender validator strictly male/female/other
def validate_gender(gender):
    valid_genders = ['Male', 'Female', 'Other']
    if gender not in valid_genders:
        raise ValueError(f"Gender must be one of: {', '.join(valid_genders)}")
    return gender

# ensures value of numbers are always positive
def validate_positive_number(value, field_name):
    try:
        num = float(value)
        if num <= 0:
            raise ValueError(f"{field_name} must be a positive number")
        return num
    except ValueError:
        raise ValueError(f"{field_name} must be a valid number")