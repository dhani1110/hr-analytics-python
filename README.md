# HR Analytics Dashboard - Python + SQL + Power BI

A professional HR Analytics Dashboard built with Python (Flask), SQL database, and Power BI for visualization.

## 🎯 Features

### Backend (Python Flask)
- ✅ RESTful API with 30+ endpoints
- ✅ SQL database (MySQL/SQL Server)
- ✅ Employee management
- ✅ Attendance tracking
- ✅ Performance reviews
- ✅ Payroll management
- ✅ Advanced analytics
- ✅ Data export to Excel

### Database (SQL)
- ✅ 7 tables with relationships
- ✅ Indexes for performance
- ✅ Referential integrity
- ✅ Scalable schema

### Power BI Reports
- ✅ Employee dashboards
- ✅ Attendance analytics
- ✅ Performance metrics
- ✅ Salary analysis
- ✅ Turnover reports
- ✅ Department insights

## 📋 Technology Stack

**Backend:**
- Python 3.8+
- Flask
- SQLAlchemy
- PyMySQL

**Database:**
- MySQL or SQL Server
- 7 tables with proper relationships

**Reporting:**
- Power BI Desktop
- Excel data export

## 📁 Project Structure

```
hr-analytics-python/
├── app.py                      # Flask app
├── requirements.txt            # Python dependencies
├── .env.example               # Configuration
├── models/
│   └── __init__.py            # Database models
├── routes/
│   ├── auth.py               # Authentication
│   ├── employees.py          # Employee management
│   ├── analytics.py          # Analytics endpoints
│   ├── attendance.py         # Attendance tracking
│   ├── performance.py        # Performance reviews
│   └── payroll.py            # Payroll management
├── database/
│   └── schema.sql            # Database schema
└── utils/
    └── data_exporter.py      # Excel export & analytics
```

## 🗄️ Database Tables

1. **users** - User accounts
2. **departments** - Department info
3. **employees** - Employee profiles
4. **attendance** - Daily attendance
5. **performance_reviews** - Performance data
6. **leave_requests** - Leave management
7. **payroll** - Salary records

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/dhani1110/hr-analytics-python.git
cd hr-analytics-python
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Database
```bash
mysql -u root -p
CREATE DATABASE hr_analytics;
mysql -u root -p hr_analytics < database/schema.sql
```

### 5. Configure Environment
```bash
cp .env.example .env
# Edit .env with your database credentials
```

### 6. Run Server
```bash
python app.py
```

Server runs on: **http://localhost:5000**

## 📊 API Endpoints

### Employees (6 endpoints)
- GET /api/employees
- GET /api/employees/<id>
- POST /api/employees
- PUT /api/employees/<id>
- DELETE /api/employees/<id>
- GET /api/employees/department/<dept_id>

### Analytics (6 endpoints)
- GET /api/analytics/employee-stats
- GET /api/analytics/attendance-stats
- GET /api/analytics/performance-stats
- GET /api/analytics/salary-analytics
- GET /api/analytics/turnover-analytics
- GET /api/analytics/dashboard-summary

### Attendance (4 endpoints)
- GET /api/attendance
- GET /api/attendance/employee/<id>
- POST /api/attendance
- PUT /api/attendance/<id>

### Performance (4 endpoints)
- GET /api/performance
- GET /api/performance/employee/<id>
- POST /api/performance
- PUT /api/performance/<id>

### Payroll (4 endpoints)
- GET /api/payroll
- GET /api/payroll/employee/<id>
- POST /api/payroll
- PUT /api/payroll/<id>

### Auth (2 endpoints)
- POST /api/auth/login
- POST /api/auth/register

## 📈 Power BI Integration

### Export Data
```python
from utils.data_exporter import DataExporter
DataExporter.export_all_data('output_path')
```

### Connect to Power BI
1. Open Power BI Desktop
2. Get Data → Excel
3. Select exported Excel files
4. Create visualizations

## 🔐 Security

- Use strong database passwords
- Never commit .env file
- Use environment variables
- Validate all inputs
- Add JWT authentication

## 📚 Database Schema

All tables are properly indexed and have foreign key relationships for data integrity.

## 🐛 Troubleshooting

**ModuleNotFoundError**
```bash
pip install -r requirements.txt
```

**Can't connect to MySQL**
- Check MySQL is running
- Verify DATABASE_URL in .env
- Check username/password

**Port 5000 in use**
```python
# Change in app.py
app.run(port=5001)
```

## 📄 License

MIT License

## 👨‍💻 Support

For questions, create an issue in the repository.

---
