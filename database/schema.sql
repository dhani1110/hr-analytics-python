-- HR Analytics Database Schema
-- SQL (MySQL/SQL Server)

-- Users Table
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('admin', 'hr', 'manager', 'employee') DEFAULT 'employee',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Departments Table
CREATE TABLE departments (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Employees Table
CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_code VARCHAR(20) NOT NULL UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(15),
    dept_id INT NOT NULL,
    designation VARCHAR(100),
    salary DECIMAL(10, 2),
    date_of_joining DATE,
    date_of_birth DATE,
    gender ENUM('Male', 'Female', 'Other'),
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50),
    status ENUM('Active', 'Inactive', 'On Leave', 'Terminated') DEFAULT 'Active',
    manager_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id),
    FOREIGN KEY (manager_id) REFERENCES employees(emp_id)
);

-- Attendance Table
CREATE TABLE attendance (
    attendance_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id INT NOT NULL,
    attendance_date DATE NOT NULL,
    status ENUM('Present', 'Absent', 'Leave', 'Half Day', 'Holiday') DEFAULT 'Present',
    check_in_time TIME,
    check_out_time TIME,
    work_hours DECIMAL(5, 2),
    remarks TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
    UNIQUE KEY unique_attendance (emp_id, attendance_date)
);

-- Performance Reviews Table
CREATE TABLE performance_reviews (
    review_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id INT NOT NULL,
    review_period VARCHAR(50),
    rating DECIMAL(3, 2),
    productivity DECIMAL(3, 2),
    communication DECIMAL(3, 2),
    teamwork DECIMAL(3, 2),
    leadership DECIMAL(3, 2),
    technical_skills DECIMAL(3, 2),
    comments TEXT,
    reviewed_by INT,
    review_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
    FOREIGN KEY (reviewed_by) REFERENCES employees(emp_id)
);

-- Leave Requests Table
CREATE TABLE leave_requests (
    leave_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id INT NOT NULL,
    leave_type ENUM('Sick Leave', 'Casual Leave', 'Earned Leave', 'Maternity', 'Paternity', 'Other'),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    number_of_days INT,
    reason TEXT,
    status ENUM('Pending', 'Approved', 'Rejected') DEFAULT 'Pending',
    approved_by INT,
    approval_date DATE,
    comments TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
    FOREIGN KEY (approved_by) REFERENCES employees(emp_id)
);

-- Payroll Table
CREATE TABLE payroll (
    payroll_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id INT NOT NULL,
    payment_month DATE NOT NULL,
    basic_salary DECIMAL(10, 2),
    allowances DECIMAL(10, 2),
    deductions DECIMAL(10, 2),
    net_salary DECIMAL(10, 2),
    payment_date DATE,
    status ENUM('Pending', 'Paid', 'Hold') DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
    UNIQUE KEY unique_payroll (emp_id, payment_month)
);

-- Create Indexes for Better Performance
CREATE INDEX idx_emp_dept ON employees(dept_id);
CREATE INDEX idx_emp_status ON employees(status);
CREATE INDEX idx_attendance_emp ON attendance(emp_id);
CREATE INDEX idx_attendance_date ON attendance(attendance_date);
CREATE INDEX idx_performance_emp ON performance_reviews(emp_id);
CREATE INDEX idx_leave_emp ON leave_requests(emp_id);
CREATE INDEX idx_payroll_emp ON payroll(emp_id);