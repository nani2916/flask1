from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define the Pet model
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    pet_type = db.Column(db.String(100), nullable=False)  # Changed 'type' to 'pet_type'
