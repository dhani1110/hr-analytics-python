from flask import Blueprint, jsonify, request

bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({'error': 'Username and password required'}), 400
        
        return jsonify({
            'message': 'Login successful',
            'token': 'demo_token_12345',
            'user': {'username': username, 'role': 'admin'}
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        if not all([username, email, password]):
            return jsonify({'error': 'All fields required'}), 400
        
        return jsonify({
            'message': 'Registration successful',
            'username': username,
            'email': email
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
