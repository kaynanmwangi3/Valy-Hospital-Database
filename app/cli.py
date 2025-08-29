import sys
import os
from tabulate import tabulate
from datetime import datetime

# Add the parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now import your modules
from app.database import get_db, init_db
from app.services.patient_service import PatientService
from app.services.staff_service import StaffService
from app.services.appointment_service import AppointmentService
from app.services.medical_record_service import MedicalRecordService
from app.services.billing_service import BillingService
from app.validators import validate_name, validate_email, validate_phone, validate_date, validate_datetime, validate_gender, validate_positive_number

class HospitalCLI:
    def __init__(self):
        init_db()
        self.db = next(get_db())
        
        # Main menu options
        self.menu_options = {
            '1': {'name': 'Patient Management', 'function': self.patient_menu},
            '2': {'name': 'Staff Management', 'function': self.staff_menu},
            '3': {'name': 'Appointment Management', 'function': self.appointment_menu},
            '4': {'name': 'Medical Records Management', 'function': self.medical_record_menu},
            '5': {'name': 'Billing Management', 'function': self.billing_menu},
            '6': {'name': 'Exit', 'function': self.exit_program}
        }
        
        # Patient menu options
        self.patient_options = {
            '1': {'name': 'Register New Patient', 'function': self.register_patient},
            '2': {'name': 'View All Patients', 'function': self.view_all_patients},
            '3': {'name': 'Search Patient', 'function': self.search_patient},
            '4': {'name': 'Update Patient', 'function': self.update_patient},
            '5': {'name': 'Delete Patient', 'function': self.delete_patient},
            '6': {'name': 'Back to Main Menu', 'function': self.main_menu}
        }
        
        # Staff menu options
        self.staff_options = {
            '1': {'name': 'Register New Staff', 'function': self.register_staff},
            '2': {'name': 'View All Staff', 'function': self.view_all_staff},
            '3': {'name': 'Search Staff', 'function': self.search_staff},
            '4': {'name': 'Update Staff', 'function': self.update_staff},
            '5': {'name': 'Delete Staff', 'function': self.delete_staff},
            '6': {'name': 'Back to Main Menu', 'function': self.main_menu}
        }
        
        # Appointment menu options
        self.appointment_options = {
            '1': {'name': 'Schedule New Appointment', 'function': self.schedule_appointment},
            '2': {'name': 'View All Appointments', 'function': self.view_all_appointments},
            '3': {'name': 'View Patient Appointments', 'function': self.view_patient_appointments},
            '4': {'name': 'View Staff Appointments', 'function': self.view_staff_appointments},
            '5': {'name': 'Update Appointment', 'function': self.update_appointment},
            '6': {'name': 'Delete Appointment', 'function': self.delete_appointment},
            '7': {'name': 'Back to Main Menu', 'function': self.main_menu}
        }
        
        # Medical record menu options
        self.medical_record_options = {
            '1': {'name': 'Create New Medical Record', 'function': self.create_medical_record},
            '2': {'name': 'View All Medical Records', 'function': self.view_all_medical_records},
            '3': {'name': 'View Patient Medical Records', 'function': self.view_patient_medical_records},
            '4': {'name': 'Update Medical Record', 'function': self.update_medical_record},
            '5': {'name': 'Delete Medical Record', 'function': self.delete_medical_record},
            '6': {'name': 'Back to Main Menu', 'function': self.main_menu}
        }
        
        # Billing menu options
        self.billing_options = {
            '1': {'name': 'Create New Bill', 'function': self.create_bill},
            '2': {'name': 'View All Bills', 'function': self.view_all_bills},
            '3': {'name': 'View Patient Bills', 'function': self.view_patient_bills},
            '4': {'name': 'View Unpaid Bills', 'function': self.view_unpaid_bills},
            '5': {'name': 'Mark Bill as Paid', 'function': self.mark_bill_paid},
            '6': {'name': 'Update Bill', 'function': self.update_bill},
            '7': {'name': 'Delete Bill', 'function': self.delete_bill},
            '8': {'name': 'Back to Main Menu', 'function': self.main_menu}
        }

    def display_menu(self, options):
        """Display a menu with the given options"""
        print("\n" + "="*50)
        for key, value in options.items():
            print(f"{key}. {value['name']}")
        print("="*50)

    def get_user_choice(self, options):
        """Get and validate user choice from menu options"""
        while True:
            choice = input("\nEnter your choice: ").strip()
            if choice in options:
                return choice
            else:
                print("Invalid choice. Please try again.")

    def main_menu(self):
        """Display the main menu"""
        while True:
            self.display_menu(self.menu_options)
            choice = self.get_user_choice(self.menu_options)
            if choice == '6':
                self.menu_options[choice]['function']()
            else:
                self.menu_options[choice]['function']()

    def patient_menu(self):
        """Display the patient management menu"""
        while True:
            self.display_menu(self.patient_options)
            choice = self.get_user_choice(self.patient_options)
            if choice == '6':
                return
            else:
                self.patient_options[choice]['function']()

    def staff_menu(self):
        """Display the staff management menu"""
        while True:
            self.display_menu(self.staff_options)
            choice = self.get_user_choice(self.staff_options)
            if choice == '6':
                return
            else:
                self.staff_options[choice]['function']()

    def appointment_menu(self):
        """Display the appointment management menu"""
        while True:
            self.display_menu(self.appointment_options)
            choice = self.get_user_choice(self.appointment_options)
            if choice == '7':
                return
            else:
                self.appointment_options[choice]['function']()

    def medical_record_menu(self):
        """Display the medical records management menu"""
        while True:
            self.display_menu(self.medical_record_options)
            choice = self.get_user_choice(self.medical_record_options)
            if choice == '6':
                return
            else:
                self.medical_record_options[choice]['function']()

    def billing_menu(self):
        """Display the billing management menu"""
        while True:
            self.display_menu(self.billing_options)
            choice = self.get_user_choice(self.billing_options)
            if choice == '8':
                return
            else:
                self.billing_options[choice]['function']()

    # Patient management methods
    def register_patient(self):
        """Register a new patient"""
        print("\n--- Register New Patient ---")
        
        # Using tuple for patient data collection
        patient_data = (
            input("First Name: "),
            input("Last Name: "),
            input("Date of Birth (YYYY-MM-DD): "),
            input("Gender (Male/Female/Other): "),
            input("Contact Number: "),
            input("Email (optional): "),
            input("Address (optional): ")
        )
        
        # Using dict for structured data storage
        patient_dict = {
            'first_name': patient_data[0],
            'last_name': patient_data[1],
            'date_of_birth': patient_data[2],
            'gender': patient_data[3],
            'contact_number': patient_data[4],
            'email': patient_data[5],
            'address': patient_data[6]
        }
        
        try:
            patient = PatientService.create_patient(self.db, patient_dict)
            print(f"\nPatient registered successfully! Patient ID: {patient.id}")
        except Exception as e:
            print(f"\nError: {e}")

    def view_all_patients(self):
        """View all patients"""
        patients = PatientService.get_all_patients(self.db)
        
        if not patients:
            print("\nNo patients found.")
            return
        
        # Prepare data for tabular display
        table_data = []
        for patient in patients:
            table_data.append([
                patient.id,
                f"{patient.first_name} {patient.last_name}",
                patient.date_of_birth,
                patient.gender,
                patient.contact_number,
                patient.email
            ])
        
        headers = ["ID", "Name", "Date of Birth", "Gender", "Contact", "Email"]
        print("\n" + tabulate(table_data, headers=headers, tablefmt="grid"))

    def search_patient(self):
        """Search for patients by name"""
        search_term = input("\nEnter patient name to search: ").strip()
        patients = PatientService.search_patients(self.db, search_term)
        
        if not patients:
            print("\nNo patients found.")
            return
        
        # Prepare data for tabular display
        table_data = []
        for patient in patients:
            table_data.append([
                patient.id,
                f"{patient.first_name} {patient.last_name}",
                patient.date_of_birth,
                patient.gender,
                patient.contact_number,
                patient.email
            ])
        
        headers = ["ID", "Name", "Date of Birth", "Gender", "Contact", "Email"]
        print("\n" + tabulate(table_data, headers=headers, tablefmt="grid"))

    def update_patient(self):
        """Update patient information"""
        patient_id = input("\nEnter patient ID to update: ").strip()
        
        try:
            patient_id = int(patient_id)
        except ValueError:
            print("Invalid patient ID. Please enter a number.")
            return
        
        patient = PatientService.get_patient(self.db, patient_id)
        if not patient:
            print("Patient not found.")
            return
        
        print(f"\nUpdating patient: {patient.first_name} {patient.last_name}")
        print("Leave field blank to keep current value.")
        
        update_data = {}
        fields = [
            ('first_name', 'First Name'),
            ('last_name', 'Last Name'),
            ('date_of_birth', 'Date of Birth (YYYY-MM-DD)'),
            ('gender', 'Gender (Male/Female/Other)'),
            ('contact_number', 'Contact Number'),
            ('email', 'Email'),
            ('address', 'Address')
        ]
        
        for field, prompt in fields:
            new_value = input(f"{prompt} [{getattr(patient, field)}]: ").strip()
            if new_value:
                update_data[field] = new_value
        
        if update_data:
            try:
                updated_patient = PatientService.update_patient(self.db, patient_id, update_data)
                print("Patient updated successfully!")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("No changes made.")

    def delete_patient(self):
        """Delete a patient"""
        patient_id = input("\nEnter patient ID to delete: ").strip()
        
        try:
            patient_id = int(patient_id)
        except ValueError:
            print("Invalid patient ID. Please enter a number.")
            return
        
        patient = PatientService.get_patient(self.db, patient_id)
        if not patient:
            print("Patient not found.")
            return
        
        confirm = input(f"Are you sure you want to delete {patient.first_name} {patient.last_name}? (y/n): ").strip().lower()
        if confirm == 'y':
            success = PatientService.delete_patient(self.db, patient_id)
            if success:
                print("Patient deleted successfully!")
            else:
                print("Error deleting patient.")
        else:
            print("Deletion cancelled.")

    # Staff management methods
    def register_staff(self):
        """Register a new staff member"""
        print("\n--- Register New Staff ---")
        
        staff_data = {
            'first_name': input("First Name: "),
            'last_name': input("Last Name: "),
            'role': input("Role (Doctor/Nurse/Admin/etc.): "),
            'department': input("Department (optional): "),
            'contact_number': input("Contact Number: "),
            'email': input("Email (optional): "),
            'hire_date': input("Hire Date (YYYY-MM-DD, optional): ")
        }
        
        try:
            staff = StaffService.create_staff(self.db, staff_data)
            print(f"\nStaff registered successfully! Staff ID: {staff.id}")
        except Exception as e:
            print(f"\nError: {e}")

    def view_all_staff(self):
        """View all staff members"""
        staff_members = StaffService.get_all_staff(self.db)
        
        if not staff_members:
            print("\nNo staff members found.")
            return
        
        # Prepare data for tabular display
        table_data = []
        for staff in staff_members:
            table_data.append([
                staff.id,
                f"{staff.first_name} {staff.last_name}",
                staff.role,
                staff.department,
                staff.contact_number,
                staff.email
            ])
        
        headers = ["ID", "Name", "Role", "Department", "Contact", "Email"]
        print("\n" + tabulate(table_data, headers=headers, tablefmt="grid"))

    def search_staff(self):
        """Search for staff by name or role"""
        search_term = input("\nEnter staff name or role to search: ").strip()
        staff_members = StaffService.search_staff(self.db, search_term)
        
        if not staff_members:
            print("\nNo staff members found.")
            return
        
        # Prepare data for tabular display
        table_data = []
        for staff in staff_members:
            table_data.append([
                staff.id,
                f"{staff.first_name} {staff.last_name}",
                staff.role,
                staff.department,
                staff.contact_number,
                staff.email
            ])
        
        headers = ["ID", "Name", "Role", "Department", "Contact", "Email"]
        print("\n" + tabulate(table_data, headers=headers, tablefmt="grid"))

    def update_staff(self):
        """Update staff information"""
        staff_id = input("\nEnter staff ID to update: ").strip()
        
        try:
            staff_id = int(staff_id)
        except ValueError:
            print("Invalid staff ID. Please enter a number.")
            return
        
        staff = StaffService.get_staff(self.db, staff_id)
        if not staff:
            print("Staff not found.")
            return
        
        print(f"\nUpdating staff: {staff.first_name} {staff.last_name}")
        print("Leave field blank to keep current value.")
        
        update_data = {}
        fields = [
            ('first_name', 'First Name'),
            ('last_name', 'Last Name'),
            ('role', 'Role'),
            ('department', 'Department'),
            ('contact_number', 'Contact Number'),
            ('email', 'Email'),
            ('hire_date', 'Hire Date (YYYY-MM-DD)')
        ]
        
        for field, prompt in fields:
            new_value = input(f"{prompt} [{getattr(staff, field)}]: ").strip()
            if new_value:
                update_data[field] = new_value
        
        if update_data:
            try:
                updated_staff = StaffService.update_staff(self.db, staff_id, update_data)
                print("Staff updated successfully!")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("No changes made.")

    def delete_staff(self):
        """Delete a staff member"""
        staff_id = input("\nEnter staff ID to delete: ").strip()
        
        try:
            staff_id = int(staff_id)
        except ValueError:
            print("Invalid staff ID. Please enter a number.")
            return
        
        staff = StaffService.get_staff(self.db, staff_id)
        if not staff:
            print("Staff not found.")
            return
        
        confirm = input(f"Are you sure you want to delete {staff.first_name} {staff.last_name}? (y/n): ").strip().lower()
        if confirm == 'y':
            success = StaffService.delete_staff(self.db, staff_id)
            if success:
                print("Staff deleted successfully!")
            else:
                print("Error deleting staff.")
        else:
            print("Deletion cancelled.")

    # Appointment management methods
    def schedule_appointment(self):
        """Schedule a new appointment"""
        print("\n--- Schedule New Appointment ---")
        
        appointment_data = {
            'patient_id': input("Patient ID: "),
            'staff_id': input("Staff ID: "),
            'appointment_date': input("Appointment Date (YYYY-MM-DD HH:MM): "),
            'purpose': input("Purpose: "),
            'status': input("Status (Scheduled/Completed/Cancelled, default: Scheduled): ") or "Scheduled"
        }
        
        try:
            appointment = AppointmentService.create_appointment(self.db, appointment_data)
            print(f"\nAppointment scheduled successfully! Appointment ID: {appointment.id}")
        except Exception as e:
            print(f"\nError: {e}")

    def view_all_appointments(self):
        """View all appointments"""
        appointments = AppointmentService.get_all_appointments(self.db)
        
        if not appointments:
            print("\nNo appointments found.")
            return
        
        # Prepare data for tabular display
        table_data = []
        for appointment in appointments:
            table_data.append([
                appointment.id,
                appointment.patient_id,
                appointment.staff_id,
                appointment.appointment_date,
                appointment.purpose,
                appointment.status
            ])
        
        headers = ["ID", "Patient ID", "Staff ID", "Date", "Purpose", "Status"]
        print("\n" + tabulate(table_data, headers=headers, tablefmt="grid"))

    def view_patient_appointments(self):
        """View appointments for a specific patient"""
        patient_id = input("\nEnter patient ID: ").strip()
        
        try:
            patient_id = int(patient_id)
        except ValueError:
            print("Invalid patient ID. Please enter a number.")
            return
        
        appointments = AppointmentService.get_patient_appointments(self.db, patient_id)
        
        if not appointments:
            print("\nNo appointments found for this patient.")
            return
        
        # Prepare data for tabular display
        table_data = []
        for appointment in appointments:
            table_data.append([
                appointment.id,
                appointment.staff_id,
                appointment.appointment_date,
                appointment.purpose,
                appointment.status
            ])
        
        headers = ["ID", "Staff ID", "Date", "Purpose", "Status"]
        print(f"\nAppointments for Patient ID {patient_id}:")
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

    def view_staff_appointments(self):
        """View appointments for a specific staff member"""
        staff_id = input("\nEnter staff ID: ").strip()
        
        try:
            staff_id = int(staff_id)
        except ValueError:
            print("Invalid staff ID. Please enter a number.")
            return
        
        appointments = AppointmentService.get_staff_appointments(self.db, staff_id)
        
        if not appointments:
            print("\nNo appointments found for this staff member.")
            return
        
        # Prepare data for tabular display
        table_data = []
        for appointment in appointments:
            table_data.append([
                appointment.id,
                appointment.patient_id,
                appointment.appointment_date,
                appointment.purpose,
                appointment.status
            ])
        
        headers = ["ID", "Patient ID", "Date", "Purpose", "Status"]
        print(f"\nAppointments for Staff ID {staff_id}:")
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

    def update_appointment(self):
        """Update appointment information"""
        appointment_id = input("\nEnter appointment ID to update: ").strip()
        
        try:
            appointment_id = int(appointment_id)
        except ValueError:
            print("Invalid appointment ID. Please enter a number.")
            return
        
        appointment = AppointmentService.get_appointment(self.db, appointment_id)
        if not appointment:
            print("Appointment not found.")
            return
        
        print(f"\nUpdating appointment ID: {appointment.id}")
        print("Leave field blank to keep current value.")
        
        update_data = {}
        fields = [
            ('patient_id', 'Patient ID'),
            ('staff_id', 'Staff ID'),
            ('appointment_date', 'Appointment Date (YYYY-MM-DD HH:MM)'),
            ('purpose', 'Purpose'),
            ('status', 'Status (Scheduled/Completed/Cancelled)')
        ]
        
        for field, prompt in fields:
            new_value = input(f"{prompt} [{getattr(appointment, field)}]: ").strip()
            if new_value:
                update_data[field] = new_value
        
        if update_data:
            try:
                updated_appointment = AppointmentService.update_appointment(self.db, appointment_id, update_data)
                print("Appointment updated successfully!")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("No changes made.")

    def delete_appointment(self):
        """Delete an appointment"""
        appointment_id = input("\nEnter appointment ID to delete: ").strip()
        
        try:
            appointment_id = int(appointment_id)
        except ValueError:
            print("Invalid appointment ID. Please enter a number.")
            return
        
        appointment = AppointmentService.get_appointment(self.db, appointment_id)
        if not appointment:
            print("Appointment not found.")
            return
        
        confirm = input(f"Are you sure you want to delete appointment ID {appointment_id}? (y/n): ").strip().lower()
        if confirm == 'y':
            success = AppointmentService.delete_appointment(self.db, appointment_id)
            if success:
                print("Appointment deleted successfully!")
            else:
                print("Error deleting appointment.")
        else:
            print("Deletion cancelled.")

    # Medical record management methods
    def create_medical_record(self):
        """Create a new medical record"""
        print("\n--- Create New Medical Record ---")
        
        record_data = {
            'patient_id': input("Patient ID: "),
            'staff_id': input("Staff ID: "),
            'diagnosis': input("Diagnosis: "),
            'treatment': input("Treatment: "),
            'admission_date': input("Admission Date (YYYY-MM-DD, optional): "),
            'discharge_date': input("Discharge Date (YYYY-MM-DD, optional): "),
            'medications': input("Medications (optional): "),
            'notes': input("Notes (optional): ")
        }
        
        try:
            record = MedicalRecordService.create_medical_record(self.db, record_data)
            print(f"\nMedical record created successfully! Record ID: {record.id}")
        except Exception as e:
            print(f"\nError: {e}")

    def view_all_medical_records(self):
        """View all medical records"""
        records = MedicalRecordService.get_all_medical_records(self.db)
        
        if not records:
            print("\nNo medical records found.")
            return
        
        # Prepare data for tabular display
        table_data = []
        for record in records:
            table_data.append([
                record.id,
                record.patient_id,
                record.staff_id,
                record.diagnosis,
                record.admission_date,
                record.discharge_date,
                record.duration_of_stay
            ])
        
        headers = ["ID", "Patient ID", "Staff ID", "Diagnosis", "Admission", "Discharge", "Days"]
        print("\n" + tabulate(table_data, headers=headers, tablefmt="grid"))

    def view_patient_medical_records(self):
        """View medical records for a specific patient"""
        patient_id = input("\nEnter patient ID: ").strip()
        
        try:
            patient_id = int(patient_id)
        except ValueError:
            print("Invalid patient ID. Please enter a number.")
            return
        
        records = MedicalRecordService.get_patient_medical_records(self.db, patient_id)
        
        if not records:
            print("\nNo medical records found for this patient.")
            return
        
        # Prepare data for tabular display
        table_data = []
        for record in records:
            table_data.append([
                record.id,
                record.staff_id,
                record.diagnosis,
                record.admission_date,
                record.discharge_date,
                record.duration_of_stay
            ])
        
        headers = ["ID", "Staff ID", "Diagnosis", "Admission", "Discharge", "Days"]
        print(f"\nMedical Records for Patient ID {patient_id}:")
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

    def update_medical_record(self):
        """Update medical record information"""
        record_id = input("\nEnter medical record ID to update: ").strip()
        
        try:
            record_id = int(record_id)
        except ValueError:
            print("Invalid record ID. Please enter a number.")
            return
        
        record = MedicalRecordService.get_medical_record(self.db, record_id)
        if not record:
            print("Medical record not found.")
            return
        
        print(f"\nUpdating medical record ID: {record.id}")
        print("Leave field blank to keep current value.")
        
        update_data = {}
        fields = [
            ('diagnosis', 'Diagnosis'),
            ('treatment', 'Treatment'),
            ('admission_date', 'Admission Date (YYYY-MM-DD)'),
            ('discharge_date', 'Discharge Date (YYYY-MM-DD)'),
            ('medications', 'Medications'),
            ('notes', 'Notes')
        ]
        
        for field, prompt in fields:
            new_value = input(f"{prompt} [{getattr(record, field)}]: ").strip()
            if new_value:
                update_data[field] = new_value
        
        if update_data:
            try:
                updated_record = MedicalRecordService.update_medical_record(self.db, record_id, update_data)
                print("Medical record updated successfully!")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("No changes made.")

    def delete_medical_record(self):
        """Delete a medical record"""
        record_id = input("\nEnter medical record ID to delete: ").strip()
        
        try:
            record_id = int(record_id)
        except ValueError:
            print("Invalid record ID. Please enter a number.")
            return
        
        record = MedicalRecordService.get_medical_record(self.db, record_id)
        if not record:
            print("Medical record not found.")
            return
        
        confirm = input(f"Are you sure you want to delete medical record ID {record_id}? (y/n): ").strip().lower()
        if confirm == 'y':
            success = MedicalRecordService.delete_medical_record(self.db, record_id)
            if success:
                print("Medical record deleted successfully!")
            else:
                print("Error deleting medical record.")
        else:
            print("Deletion cancelled.")

    # Billing management methods
    def create_bill(self):
        """Create a new bill"""
        print("\n--- Create New Bill ---")
        
        bill_data = {
            'patient_id': input("Patient ID: "),
            'amount': input("Amount: "),
            'due_date': input("Due Date (YYYY-MM-DD, optional): "),
            'description': input("Description: "),
            'status': input("Status (Paid/Unpaid, default: Unpaid): ") or "Unpaid"
        }
        
        try:
            bill = BillingService.create_bill(self.db, bill_data)
            print(f"\nBill created successfully! Bill ID: {bill.id}")
        except Exception as e:
            print(f"\nError: {e}")

    def view_all_bills(self):
        """View all bills"""
        bills = BillingService.get_all_bills(self.db)
        
        if not bills:
            print("\nNo bills found.")
            return
        
        # Prepare data for tabular display
        table_data = []
        for bill in bills:
            table_data.append([
                bill.id,
                bill.patient_id,
                bill.amount,
                bill.date_issued,
                bill.due_date,
                bill.status
            ])
        
        headers = ["ID", "Patient ID", "Amount", "Issued", "Due", "Status"]
        print("\n" + tabulate(table_data, headers=headers, tablefmt="grid"))

    def view_patient_bills(self):
        """View bills for a specific patient"""
        patient_id = input("\nEnter patient ID: ").strip()
        
        try:
            patient_id = int(patient_id)
        except ValueError:
            print("Invalid patient ID. Please enter a number.")
            return
        
        bills = BillingService.get_patient_bills(self.db, patient_id)
        
        if not bills:
            print("\nNo bills found for this patient.")
            return
        
        # Prepare data for tabular display
        table_data = []
        for bill in bills:
            table_data.append([
                bill.id,
                bill.amount,
                bill.date_issued,
                bill.due_date,
                bill.status
            ])
        
        headers = ["ID", "Amount", "Issued", "Due", "Status"]
        print(f"\nBills for Patient ID {patient_id}:")
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

    def view_unpaid_bills(self):
        """View all unpaid bills"""
        bills = BillingService.get_unpaid_bills(self.db)
        
        if not bills:
            print("\nNo unpaid bills found.")
            return
        
        # Prepare data for tabular display
        table_data = []
        for bill in bills:
            table_data.append([
                bill.id,
                bill.patient_id,
                bill.amount,
                bill.date_issued,
                bill.due_date
            ])
        
        headers = ["ID", "Patient ID", "Amount", "Issued", "Due"]
        print("\nUnpaid Bills:")
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

    def mark_bill_paid(self):
        """Mark a bill as paid"""
        bill_id = input("\nEnter bill ID to mark as paid: ").strip()
        
        try:
            bill_id = int(bill_id)
        except ValueError:
            print("Invalid bill ID. Please enter a number.")
            return
        
        bill = BillingService.mark_as_paid(self.db, bill_id)
        if bill:
            print(f"Bill ID {bill_id} marked as paid successfully!")
        else:
            print("Bill not found.")

    def update_bill(self):
        """Update bill information"""
        bill_id = input("\nEnter bill ID to update: ").strip()
        
        try:
            bill_id = int(bill_id)
        except ValueError:
            print("Invalid bill ID. Please enter a number.")
            return
        
        bill = BillingService.get_bill(self.db, bill_id)
        if not bill:
            print("Bill not found.")
            return
        
        print(f"\nUpdating bill ID: {bill.id}")
        print("Leave field blank to keep current value.")
        
        update_data = {}
        fields = [
            ('amount', 'Amount'),
            ('due_date', 'Due Date (YYYY-MM-DD)'),
            ('description', 'Description'),
            ('status', 'Status (Paid/Unpaid)')
        ]
        
        for field, prompt in fields:
            new_value = input(f"{prompt} [{getattr(bill, field)}]: ").strip()
            if new_value:
                update_data[field] = new_value
        
        if update_data:
            try:
                updated_bill = BillingService.update_bill(self.db, bill_id, update_data)
                print("Bill updated successfully!")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("No changes made.")

    def delete_bill(self):
        """Delete a bill"""
        bill_id = input("\nEnter bill ID to delete: ").strip()
        
        try:
            bill_id = int(bill_id)
        except ValueError:
            print("Invalid bill ID. Please enter a number.")
            return
        
        bill = BillingService.get_bill(self.db, bill_id)
        if not bill:
            print("Bill not found.")
            return
        
        confirm = input(f"Are you sure you want to delete bill ID {bill_id}? (y/n): ").strip().lower()
        if confirm == 'y':
            success = BillingService.delete_bill(self.db, bill_id)
            if success:
                print("Bill deleted successfully!")
            else:
                print("Error deleting bill.")
        else:
            print("Deletion cancelled.")

    def exit_program(self):
        """Exit the program"""
        print("\nThank you for using Hospital Management System. Goodbye!")
        sys.exit(0)

def main():
    """Main function to run the CLI"""
    cli = HospitalCLI()
    print("Welcome to Hospital Management System!")
    cli.main_menu()

if __name__ == "__main__":
    main()