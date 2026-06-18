import pandas as pd
import os
from app import db
from models import Employee, Attendance, PerformanceReview, Payroll

class DataExporter:
    @staticmethod
    def export_employees_to_excel(filename='employees.xlsx'):
        employees = Employee.query.all()
        data = []
        for emp in employees:
            data.append({
                'Employee ID': emp.emp_code,
                'First Name': emp.first_name,
                'Last Name': emp.last_name,
                'Email': emp.email,
                'Department': emp.department.dept_name if emp.department else '',
                'Salary': emp.salary,
                'Status': emp.status
            })
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
        return filename
    
    @staticmethod
    def export_all_data(output_path='hr_data'):
        os.makedirs(output_path, exist_ok=True)
        DataExporter.export_employees_to_excel(f'{output_path}/employees.xlsx')
        return f"Data exported to {output_path}/"