from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from models import User


class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=3, max=20)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=3, max=20)])
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=(DataRequired(), Email()))
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password', message='password must match!')])
    confirm_password = PasswordField('Confirm_password', validators=[DataRequired()])
    submit = SubmitField('Register')

    
    def validate_first_name(self, first_name):
        user = User.query.filter_by(first_name=first_name.data).first()
        if user:
            raise ValidationError('Oops!, That name is taken. Please choose another one.')

    def validate_last_name(self, last_name):
        user = User.query.filter_by(last_name=last_name.data).first()
        if user:
            raise ValidationError('Oops!, That name is taken. Please choose another one.')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Oops!, That name is taken. Please choose another one.')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Oops!, That name is taken. Please choose another one.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')