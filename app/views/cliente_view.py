"""Cliente view."""

from flask import redirect, render_template, request, url_for

from app import app
from app.entities import cliente as cliente_entity
from app.forms import cliente_form
from app.models import cliente_model
from app.services import cliente_service


def get_cliente_from_form(form) -> cliente_entity.Cliente:
    """Get an instance of Cliente entity with data from a given `form`."""
    nome = form.nome.data
    email = form.email.data
    data_nascimento = form.data_nascimento.data
    profissao = form.profissao.data
    sexo = form.sexo.data

    return cliente_entity.Cliente(
        nome=nome,
        email=email,
        data_nascimento=data_nascimento,
        profissao=profissao,
        sexo=sexo
    )


@app.route("/cadastrar_cliente", methods=["GET", "POST"])
def cadastrar_cliente():
    """View for create cliente."""
    form = cliente_form.ClienteForm()
    if form.validate_on_submit():
        cliente_data = get_cliente_from_form(form)
        cliente_db = cliente_model.Cliente(
            nome=cliente_data.nome,
            email=cliente_data.email,
            data_nascimento=cliente_data.data_nascimento,
            profissao=cliente_data.profissao,
            sexo=cliente_data.sexo,
        )

        if cliente_service.insert_cliente(cliente_db):
            return redirect(url_for("listar_clientes"))
    else:
        print(form.errors)

    return render_template(
        "clientes/form.html",
        form=form,
        action="insert"
    )


@app.route("/", methods=["GET"])
def listar_clientes():
    """View list of clientes."""
    clientes_db = cliente_service.get_all_clientes()
    return render_template(
        "clientes/lista_clientes.html",
        clientes=clientes_db
    )


@app.route("/detalhe_cliente/<int:pk>", methods=["GET"])
def detalhe_cliente(pk: int):  # pylint: disable=invalid-name
    """View detail of a cliente."""
    cliente_db = cliente_service.get_cliente_by_id(pk)
    return render_template(
        "clientes/detalhe_cliente.html",
        cliente=cliente_db,
        action='detail'
    )


@app.route("/editar_cliente/<int:pk>", methods=["GET", "POST"])
def editar_cliente(pk: int):  # pylint: disable=invalid-name
    """View edit cliente."""
    cliente_db = cliente_service.get_cliente_by_id(pk)
    form = cliente_form.ClienteForm(obj=cliente_db)

    if request.method == 'GET':
        form.sexo.data = cliente_db.sexo

    if form.validate_on_submit():
        cliente_data = get_cliente_from_form(form)

        if cliente_service.edit_cliente(cliente_db, cliente_data):
            return redirect(url_for("listar_clientes"))

    return render_template(
        "clientes/form.html",
        form=form,
        action="edit"
    )


@app.route("/remover_cliente/<int:pk>", methods=["GET", "POST"])
def remover_cliente(pk: int):  # pylint: disable=invalid-name
    """View remove cliente."""
    cliente_db = cliente_service.get_cliente_by_id(pk)

    if request.method == "POST":
        if cliente_service.delete_cliente(cliente_db):
            return redirect(url_for("listar_clientes"))

    return render_template(
        "clientes/detalhe_cliente.html",
        cliente=cliente_db,
        action='delete'
    )

# ----- Examples -----

# @app.route("/hello")
# def hello():
#     """Hello world view."""
#     return "Hello, world from Flask!"


# @app.route("/welcome/<string:name>")
# def welcome(name):
#     """Route with mandatory parameter."""
#     return f"Welcome {name}!"


# @app.route("/goodmorning", defaults={"name": None})
# @app.route("/goodmorning/<string:name>")
# def good_morning(name):
#     """Route with optional parameter."""
#     if name:
#         return f"Good morning, {name}!"
#     return "Good morning!"


# @app.route("/bank", methods={"DELETE"})
# def bank():
#     """Route with specific HTTP method."""
#     return "Contente deleted!"


# @app.route("/", defaults={"name": None}, methods={"GET"})
# @app.route("/<string:name>", methods={"GET"})
# def home(name):
#     """Home view."""
#     return render_template("clientes/home.html", user_name=name)
