from flask import Flask, render_template, redirect, url_for
from model import db, Pet  # Import the db and Pet model
from form import PetForm
from datetime import datetime  # Import datetime for current year

app = Flask(__name__)

# Flask configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'rathna-flask-test'

# Initialize the SQLAlchemy database object with the Flask app
db.init_app(app)

# Create the tables if they don't exist
with app.app_context():
    db.create_all()  # This line creates the tables in your database

@app.route('/add_pet', methods=['GET', 'POST'])
def add_pet():
    form = PetForm()
    if form.validate_on_submit():
        pet = Pet(name=form.name.data, age=form.age.data, pet_type=form.pet_type.data)  # Adjusted pet_type to type
        db.session.add(pet)
        db.session.commit()
        return redirect(url_for('pet_list'))  # Redirect to pet_list after adding a pet
    
    return render_template('add_pet.html', form=form, current_year=datetime.now().year)

@app.route('/pet_list')
def pet_list():
    pets = Pet.query.all()  
    return render_template('view_pets.html', pets=pets, current_year=datetime.now().year)  # Pass pets to the template

@app.route('/')
def index():
    return render_template('home.html')  # This could be a home page or landing page4

@app.route('/remove_pet/<int:pet_id>', methods=['POST'])
def remove_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)  # Get the pet by ID or return a 404 if not found
    db.session.delete(pet)  # Remove the pet from the session
    db.session.commit()  # Commit the changes to the database
    return redirect(url_for('pet_list'))  # Redirect to the pet list page


if __name__ == '__main__':
    app.run(debug=True)
