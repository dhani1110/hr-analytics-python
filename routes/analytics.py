from flask import Blueprint, jsonify
from app import db
from models import Employee, Attendance, PerformanceReview
from sqlalchemy import func
from datetime import datetime

bp = Blueprint('analytics', __name__, url_prefix='/api/analytics')

@bp.route('/employee-stats', methods=['GET'])
def employee_stats():
    try:
        total = Employee.query.count()
        active = Employee.query.filter_by(status='Active').count()
        return jsonify({'total': total, 'active': active}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/dashboard-summary', methods=['GET'])
def dashboard_summary():
    try:
        total_emp = Employee.query.count()
        active_emp = Employee.query.filter_by(status='Active').count()
        return jsonify({'total': total_emp, 'active': active_emp}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500