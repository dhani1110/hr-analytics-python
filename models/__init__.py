from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default='employee')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Department(db.Model):
    __tablename__ = 'departments'
    
    dept_id = db.Column(db.Integer, primary_key=True)
    dept_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    employees = db.relationship('Employee', backref='department', lazy=True)

class Employee(db.Model):
    __tablename__ = 'employees'
    
    emp_id = db.Column(db.Integer, primary_key=True)
    emp_code = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15))
    dept_id = db.Column(db.Integer, db.ForeignKey('departments.dept_id'), nullable=False)
    designation = db.Column(db.String(100))
    salary = db.Column(db.Float)
    date_of_joining = db.Column(db.Date)
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.String(20))
    address = db.Column(db.Text)
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    country = db.Column(db.String(50))
    status = db.Column(db.String(20), default='Active')
    manager_id = db.Column(db.Integer, db.ForeignKey('employees.emp_id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    attendance = db.relationship('Attendance', backref='employee', lazy=True)
    performance_reviews = db.relationship('PerformanceReview', backref='employee', lazy=True)
    leave_requests = db.relationship('LeaveRequest', backref='employee', lazy=True)
    payroll = db.relationship('Payroll', backref='employee', lazy=True)

class Attendance(db.Model):
    __tablename__ = 'attendance'
    
    attendance_id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.Integer, db.ForeignKey('employees.emp_id'), nullable=False)
    attendance_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), default='Present')
    check_in_time = db.Column(db.Time)
    check_out_time = db.Column(db.Time)
    work_hours = db.Column(db.Float)
    remarks = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class PerformanceReview(db.Model):
    __tablename__ = 'performance_reviews'
    
    review_id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.Integer, db.ForeignKey('employees.emp_id'), nullable=False)
    review_period = db.Column(db.String(50))
    rating = db.Column(db.Float)
    productivity = db.Column(db.Float)
    communication = db.Column(db.Float)
    teamwork = db.Column(db.Float)
    leadership = db.Column(db.Float)
    technical_skills = db.Column(db.Float)
    comments = db.Column(db.Text)
    reviewed_by = db.Column(db.Integer, db.ForeignKey('employees.emp_id'))
    review_date = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class LeaveRequest(db.Model):
    __tablename__ = 'leave_requests'
    
    leave_id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.Integer, db.ForeignKey('employees.emp_id'), nullable=False)
    leave_type = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    number_of_days = db.Column(db.Integer)
    reason = db.Column(db.Text)
    status = db.Column(db.String(20), default='Pending')
    approved_by = db.Column(db.Integer, db.ForeignKey('employees.emp_id'))
    approval_date = db.Column(db.Date)
    comments = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Payroll(db.Model):
    __tablename__ = 'payroll'
    
    payroll_id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.Integer, db.ForeignKey('employees.emp_id'), nullable=False)
    payment_month = db.Column(db.Date, nullable=False)
    basic_salary = db.Column(db.Float)
    allowances = db.Column(db.Float)
    deductions = db.Column(db.Float)
    net_salary = db.Column(db.Float)
    payment_date = db.Column(db.Date)
    status = db.Column(db.String(20), default='Pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)