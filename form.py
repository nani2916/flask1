from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

# Define the PetForm form
class PetForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=0, message="Age must be positive.")])
    pet_type = StringField('Type', validators=[DataRequired()])  # Changed 'type' to 'pet_type'
    submit = SubmitField('Add a pet to the database')
