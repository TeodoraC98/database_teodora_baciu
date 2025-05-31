from wtforms import Form, BooleanField, StringField, PasswordField, SubmitField,EmailField, TelField,validators
from wtforms.validators import Length, DataRequired, EqualTo, InputRequired,Email

class RegistrationUser(Form):
    name=StringField('First name',validators=(Length(min=4,max=25),InputRequired(message="Please enter your first name!")))
    surname=StringField('Surname',validators=(Length(min=4,max=25),InputRequired()))
    email=EmailField('Email',validators=(InputRequired(), Length(min=10,max=40),Email("Please enter your email address.")))
    password=PasswordField("Password",validators=[Length(min=10, max=20),InputRequired()])
    confirm_password=PasswordField('Confirm Password', validators=(InputRequired(),EqualTo('password',message="Password don't match!")))
    phone=TelField("Contact  number", validators=(InputRequired(message="Contact number invalid!"), Length(min=8, max=15)))
    accept_term=BooleanField("I agree that my data will be processed in accordance with GDPR and I accept the Privacy Policy", validators=[DataRequired()])
    submit=SubmitField('Create account')

class LogIn(Form):
    email=EmailField("Email", [validators.DataRequired(message="Please provide a valid email!"),validators.Email()])
    password=PasswordField("Password",validators=[DataRequired()])
    submit=SubmitField('Login')
