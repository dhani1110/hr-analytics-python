from flask import Blueprint, jsonify, request
from app import db
from models import Employee, Department
from sqlalchemy import func

bp = Blueprint('employees', __name__, url_prefix='/api/employees')

@bp.route('/', methods=['GET'])
def get_employees():
    try:
        employees = Employee.query.all()
        data = []
        for emp in employees:
            data.append({
                'emp_id': emp.emp_id,
                'emp_code': emp.emp_code,
                'first_name': emp.first_name,
                'last_name': emp.last_name,
                'email': emp.email,
                'department': emp.department.dept_name if emp.department else None,
                'designation': emp.designation,
                'salary': emp.salary,
                'status': emp.status
            })
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/<int:emp_id>', methods=['GET'])
def get_employee(emp_id):
    try:
        emp = Employee.query.get(emp_id)
        if not emp:
            return jsonify({'error': 'Employee not found'}), 404
        return jsonify({'emp_id': emp.emp_id, 'first_name': emp.first_name}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/', methods=['POST'])
def create_employee():
    try:
        data = request.get_json()
        emp = Employee(
            emp_code=data.get('emp_code'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email'),
            dept_id=data.get('dept_id'),
            designation=data.get('designation'),
            salary=data.get('salary')
        )
        db.session.add(emp)
        db.session.commit()
        return jsonify({'message': 'Employee created', 'emp_id': emp.emp_id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500