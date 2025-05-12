from flask import Flask, request, jsonify
from models import db, ma, Reminder, ReminderSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db.init_app(app)
ma.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/reminders', methods=['POST'])
def create_reminder():
    data = request.json
    required_fields = ['date', 'time', 'message', 'reminder_type']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    if data['reminder_type'] not in ['SMS', 'Email']:
        return jsonify({'error': 'Invalid reminder type'}), 400

    new_reminder = Reminder(
        date=data['date'],
        time=data['time'],
        message=data['message'],
        reminder_type=data['reminder_type']
    )
    db.session.add(new_reminder)
    db.session.commit()

    return ReminderSchema().jsonify(new_reminder), 201

if __name__ == '__main__':
    app.run(debug=True)
