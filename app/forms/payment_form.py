from wtforms import Form, StringField,HiddenField, validators, IntegerField
from wtforms.validators import Length, DataRequired, InputRequired
from datetime import date
current_date = date.today()
curent_month = current_date.month
curent_year = current_date.year

class PaymentForm(Form):
    card_nr=StringField('Card Number',validators=[InputRequired(),  Length(min=16,max=16)])
    security_code=StringField('Security Cod',validators=[InputRequired(),Length(min=3,max=3)])
    expired_date=StringField('MM/YY', validators=[InputRequired(),Length(min=5,max=5)])
    holder_name=StringField('Name Holder',validators=[InputRequired(),Length(min=7, max=40)])

