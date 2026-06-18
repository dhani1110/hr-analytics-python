from flask import Blueprint, jsonify

bp = Blueprint('payroll', __name__, url_prefix='/api/payroll')

@bp.route('/', methods=['GET'])
def get_payroll():
    try:
        return jsonify({'message': 'Payroll records'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500