# Hospital Database Management System

#### A comprehensive hospital management system built with Python, SQLite, and SQLAlchemy, June 27, 2025

#### By **Kaynan Mwangi**

## Description
The Hospital Database Management System is a robust, command-line interface application designed to streamline hospital operations through efficient data management. This system provides a complete solution for managing patient records, staff information, appointments, medical records, and billing processes. Built with modern Python technologies including SQLAlchemy ORM and Alembic for database migrations, it offers a scalable foundation for hospital administration with proper data validation and persistence.

### Project Goals

- **Centralized Patient Management**: Complete CRUD operations for patient registration, updates, and records management
- **Staff Administration**: Comprehensive staff management with role-based tracking
- **Appointment Scheduling**: Efficient scheduling system for patient appointments with medical staff
- **Medical Records Management**: Detailed medical history tracking with diagnosis, treatment, and admission data
- **Billing System**: Integrated billing with payment status tracking and financial reporting
- **Data Integrity**: Robust input validation and database constraints to ensure data accuracy
- **User-Friendly CLI**: Intuitive command-line interface with clear navigation and prompts

### Features

- **Patient CRUD Operations**: Register new patients, update information, search, and delete records
- **Staff Management**: Complete staff directory with role and department tracking
- **Appointment System**: Schedule, view, update, and cancel patient appointments
- **Medical Records**: Detailed medical history including diagnoses, treatments, and hospital stay duration
- **Billing Module**: Create bills, track payments, and generate financial reports
- **Input Validation**: Comprehensive validation for all user inputs including dates, emails, and phone numbers
- **Database Persistence**: SQLite database with proper schema migrations using Alembic
- **Tabular Data Display**: Clean, formatted output using the Tabulate library

## Setup/Installation Requirements

### Prerequisites
- Python 3.8 or higher
- pipenv for dependency management

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kaynanmwangi3/Valy-Hospital-Database.git
   cd Valy-Hospital-Database
   ```

2. **Install dependencies using pipenv**:
   ```bash
   pipenv install
   ```

3. **Activate the virtual environment**:
   ```bash
   pipenv shell
   ```

4. **Initialize the database**:
   ```bash
   # Using Alembic migrations
   alembic upgrade head

5. **Run the application**:
   ```bash
   # Method 1: Using the main entry point
   python main.py
   
   # Method 2: Direct module execution
   python -m app.cli
   

### Database Configuration

The system uses SQLite by default, creating a `hospital.db` file in the project directory. For production use, you can modify the connection string in `app/database.py` to use other databases supported by SQLAlchemy.

## Known Bugs
{The application works as intended with no known bugs at this time.}

## Technologies Used
This application was built using:

- **Python 3.8+**: Core programming language
- **SQLAlchemy ORM**: Database object-relational mapping and query building
- **Alembic**: Database migration management
- **SQLite**: Lightweight database engine for data persistence
- **Tabulate**: Library for formatted table output in CLI
- **Python-dateutil**: Advanced date parsing and manipulation

### Architecture

- **Model-View-Controller Pattern**: Separation of data models, business logic, and user interface
- **Service Layer Architecture**: Dedicated service classes for each entity type
- **Modular Design**: Independent components for easy maintenance and testing
- **Input Validation Layer**: Comprehensive validation before database operations

## Support and Contact Details
If you encounter any issues or have questions about the Hospital Database Management System, please reach out:

- **Email**: caeserkaynan@gmail.com
- **GitHub**: kaynanmwangi3
- **Project Repository**: https://github.com/kaynanmwangi3/Valy-Hospital-Database
- **Documentation**: Full documentation available in the `/docs` directory

For bug reports or feature requests, please open an issue on the GitHub repository with detailed information about the problem or suggestion.

### License
This project is licensed under the MIT License. Copyright © 2025 Kaynan Mwangi. All rights reserved.