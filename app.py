from flask import Flask, render_template, redirect, url_for
from model import db, Pet 
from form import PetForm
from datetime import datetime  

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'rathna-flask-test'

db.init_app(app)

with app.app_context():
    db.create_all() 

@app.route('/add_pet', methods=['GET', 'POST'])
def add_pet():
    form = PetForm()
    if form.validate_on_submit():
        pet = Pet(name=form.name.data, age=form.age.data, pet_type=form.pet_type.data)  
        db.session.add(pet)
        db.session.commit()
        return redirect(url_for('pet_list')) 
    
    return render_template('add_pet.html', form=form, current_year=datetime.now().year)

@app.route('/pet_list')
def pet_list():
    pets = Pet.query.all()  
    return render_template('view_pets.html', pets=pets, current_year=datetime.now().year)  
@app.route('/')
def index():
    return render_template('home.html')  

@app.route('/remove_pet/<int:pet_id>', methods=['POST'])
def remove_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)  
    db.session.delete(pet) 
    db.session.commit() 
    return redirect(url_for('pet_list'))  

if __name__ == '__main__':
    app.run(debug=True)
