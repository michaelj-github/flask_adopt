from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):

    name = StringField("Pet's Name", validators=[InputRequired()])
    photo_url = StringField("Link to Photo")
    age = IntegerField("Age")
    species = StringField("Species")
    notes = StringField("Notes")

class EditPetForm(FlaskForm):

    name = StringField("Pet's Name")
    photo_url = StringField("Photo")
    available = BooleanField("Available?")

