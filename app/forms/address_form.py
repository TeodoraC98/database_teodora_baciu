from wtforms import Form, StringField,RadioField, validators
from wtforms.validators import  InputRequired, Length, DataRequired

class AddressForm(Form):
    street = StringField('Street Address',validators=[InputRequired()])
    apartment = StringField('Apartment (Optional)')
    city = StringField('City',validators=[InputRequired()])
    county = StringField('County',validators=[InputRequired()])
    cost=RadioField("Cost delivery",choices=[("free",'FREE'),("standard",'STANDARD'),("express",'EXPRESS')])
    postcode=StringField('Postcode', validators=[InputRequired(),Length(min=7,max=7)])

