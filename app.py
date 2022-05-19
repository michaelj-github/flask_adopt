from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from forms import EditPetForm, AddPetForm
from models import db, connect_db, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SECRET_KEY'] = "mjm34442"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route("/")
def list_pets():
    """List all pets."""
    pets = Pet.query.all()
    return render_template("list_pets_form.html", pets=pets)

@app.route("/add")
def add_pet_view():
    """Add a pet."""

    form = AddPetForm()
    return render_template("add_pet_form.html", form=form)

@app.route("/add", methods=["POST"])
def add_pet():
    """Add a pet."""

    form = AddPetForm()

    if form.validate_on_submit():
        new_pet = Pet(name=form.name.data, age=form.age.data, species=form.species.data)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template("add_pet_form.html", form=form)

@app.route("/<int:pet_id>")
def edit_pet_view(pet_id):
    """GET request to view the Edit pet page."""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    return render_template("edit_pet_form.html", form=form, pet=pet)

@app.route("/<int:pet_id>", methods=["POST"])
def edit_pet(pet_id):
    """POST request to Edit a pet record."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.photo_url = form.photo_url.data
        pet.available = form.available.data
        db.session.commit()
        return redirect(f"/{pet_id}")
    else:
        return render_template("edit_pet_form.html", form=form, pet=pet)    



