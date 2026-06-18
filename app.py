from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL',
    'mysql+pymysql://root:password@localhost:3306/hr_analytics'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import models
from models import (
    User, Department, Employee, Attendance, 
    PerformanceReview, LeaveRequest, Payroll
)

# Import routes
from routes import auth, employees, analytics, attendance, performance, payroll

# Register blueprints
app.register_blueprint(auth.bp)
app.register_blueprint(employees.bp)
app.register_blueprint(analytics.bp)
app.register_blueprint(attendance.bp)
app.register_blueprint(performance.bp)
app.register_blueprint(payroll.bp)

@app.route('/')
def index():
    return {'message': 'HR Analytics API - Python Flask'}

@app.errorhandler(404)
def not_found(error):
    return {'error': 'Resource not found'}, 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return {'error': 'Internal server error'}, 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)