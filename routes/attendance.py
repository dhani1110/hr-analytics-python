from flask import Blueprint, jsonify, request
from app import db
from models import Attendance

bp = Blueprint('attendance', __name__, url_prefix='/api/attendance')

@bp.route('/', methods=['GET'])
def get_attendance():
    try:
        records = Attendance.query.all()
        return jsonify([{'id': r.attendance_id, 'status': r.status} for r in records]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500