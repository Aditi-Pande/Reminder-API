from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    time = db.Column(db.String(8), nullable=False)
    message = db.Column(db.String(255), nullable=False)
    reminder_type = db.Column(db.String(10), nullable=False)

class ReminderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Reminder
