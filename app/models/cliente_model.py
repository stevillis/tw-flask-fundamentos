"""Cliente model related."""
from sqlalchemy_utils import ChoiceType

from app import db


class Cliente(db.Model):
    """Cliente model definition."""
    __tablename__ = 'clientes'

    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('N', 'Nenhuma das opções'),
    ]

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(200), unique=True)
    data_nascimento = db.Column(db.DateTime)
    profissao = db.Column(db.String(30))
    sexo = db.Column(ChoiceType(SEXO_CHOICES))
