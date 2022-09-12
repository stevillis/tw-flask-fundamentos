"""Form validation for Cliente."""

from flask_wtf import FlaskForm
from wtforms import DateField, EmailField, SelectField, StringField
from wtforms.validators import DataRequired, Email


class ClienteForm(FlaskForm):
    """Form validation rules for Cliente."""

    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('N', 'Nenhuma das opções')
    ]

    nome = StringField('nome', validators=[DataRequired()])
    email = EmailField('email', validators=[Email(), DataRequired()])
    data_nascimento = DateField('data_nascimento', validators=[DataRequired()])
    profissao = StringField('profissao', validators=[DataRequired()])
    sexo = SelectField(
        'sexo',
        validators=[DataRequired()],
        choices=SEXO_CHOICES
    )
