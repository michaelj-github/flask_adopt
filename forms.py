from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):

    name = StringField("Pet's Name", validators=[InputRequired()])
    photo_url = StringField("Link to Photo", validators=[URL(), Optional()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30, message=("Age must be between 0 and 30.")), Optional()])
    species = SelectField("Species", choices=[('cat', 'cat'), ('dog', 'dog'), ('porcupine', 'porcupine')])
    notes = StringField("Notes")

class EditPetForm(FlaskForm):

    photo_url = StringField("Link to Photo", validators=[URL(), Optional()])
    notes = StringField("Notes")
    available = BooleanField("Available")

