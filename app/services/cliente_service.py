"""Cliente service layer related."""

from typing import List

from app import db
from app.entities import cliente as cliente_entity
from app.models import cliente_model


def get_all_clientes() -> List[cliente_model.Cliente]:
    """Get all clientes from db."""
    return cliente_model.Cliente.query.all()


def get_cliente_by_id(pk: int) -> cliente_model.Cliente:  # pylint: disable=invalid-name
    """Get a cliente from db by id.

    Attributes:
        pk: the cliente id.
    """
    return cliente_model.Cliente.query.filter_by(id=pk).first()


def insert_cliente(cliente: cliente_model.Cliente) -> bool:
    """Insert a cliente on the database.

    cliente: The cliente data to store on the database.

    Returns: True if insert cliente successfully, False otherwise.
    """
    try:
        db.session.add(cliente)
        db.session.commit()
        return True
    except Exception as e:  # pylint: disable=invalid-name, broad-except
        print("Cliente não cadastrado.", e)

    return False


def edit_cliente(
        cliente_old: cliente_model.Cliente,
        cliente_new: cliente_entity.Cliente
) -> bool:
    """Update cliente data on the database.

    cliente_old: The cliente with old data retrievied from the database.
    cliente_new: The cliente new data submited from the form.

    Returns: True if edit cliente successfully, False otherwise.
    """
    cliente_old.nome = cliente_new.nome
    cliente_old.email = cliente_new.email
    cliente_old.data_nascimento = cliente_new.data_nascimento
    cliente_old.profissao = cliente_new.profissao
    cliente_old.sexo = cliente_new.sexo

    try:
        db.session.commit()
        return True
    except Exception as e:  # pylint: disable=invalid-name, broad-except
        print("Não foi possível editar o cliente.", e)

    return False


def delete_cliente(cliente_db: cliente_model.Cliente) -> bool:
    """Detele a cliente from the database.

    cliente_db: The cliente to be removed from the database.

    Returns: True if remove cliente successfully, False otherwise.
    """
    try:
        db.session.delete(cliente_db)
        db.session.commit()
        return True
    except Exception as e:  # pylint: disable=invalid-name, broad-except
        print("Não foi possível remover o cliente.", e)

    return False
