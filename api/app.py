from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='../templates')

initial_data = [
    {"id": "EMP-001", "name": "สมชาย ใจดี", "gender": "ชาย", "position": "Senior Software Engineer", "department": "IT", "status": "Active", "salary": 75000, "performance": 4.8},
    {"id": "EMP-002", "name": "วิภาวี มั่นคง", "gender": "หญิง", "position": "HR Manager", "department": "HR", "status": "Active", "salary": 65000, "performance": 4.5},
    {"id": "EMP-003", "name": "กิตติพงษ์ สุขเสริฐ", "gender": "ชาย", "position": "Financial Analyst", "department": "Finance", "status": "Active", "salary": 55000, "performance": 4.2},
    {"id": "EMP-004", "name": "นภา วงศ์สว่าง", "gender": "หญิง", "position": "Marketing Specialist", "department": "Marketing", "status": "On Leave", "salary": 42000, "performance": 3.9},
    {"id": "EMP-005", "name": "อนุรักษ์ รักษ์ชาติ", "gender": "ชาย", "position": "DevOps Engineer", "department": "IT", "status": "Active", "salary": 68000, "performance": 4.6},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/employees', methods=['GET'])
def get_employees():
    return jsonify(initial_data)

if __name__ == '__main__':
    app.run(debug=True)
