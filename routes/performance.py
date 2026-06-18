from flask import Blueprint, jsonify

bp = Blueprint('performance', __name__, url_prefix='/api/performance')

@bp.route('/', methods=['GET'])
def get_performance():
    try:
        return jsonify({'message': 'Performance reviews'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500