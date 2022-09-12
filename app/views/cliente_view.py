"""Cliente view."""


from app import app, db
from app.forms import cliente_form
from app.models import cliente_model
from flask import render_template


@app.route('/cadastrar_cliente', methods=['GET', 'POST'])
def cadastrar_cliente():
    """View for create cliente."""
    print('entrou')
    form = cliente_form.ClienteForm()
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        data_nascimento = form.data_nascimento.data
        profissao = form.profissao.data
        sexo = form.sexo.data

        cliente = cliente_model.Cliente(
            nome=nome,
            email=email,
            data_nascimento=data_nascimento,
            profissao=profissao,
            sexo=sexo,
        )

        try:
            db.session.add(cliente)
            db.session.commit()
        except:
            print('Cliente não cadastrado.')
    else:
        print(form.errors)
        print(form)

    return render_template('clientes/form.html', form=form)


# ----- Examples -----

# @app.route('/hello')
# def hello():
#     """Hello world view."""
#     return 'Hello, world from Flask!'


# @app.route('/welcome/<string:name>')
# def welcome(name):
#     """Route with mandatory parameter."""
#     return f'Welcome {name}!'


# @app.route('/goodmorning', defaults={'name': None})
# @app.route('/goodmorning/<string:name>')
# def good_morning(name):
#     """Route with optional parameter."""
#     if name:
#         return f'Good morning, {name}!'
#     return 'Good morning!'


# @app.route('/bank', methods={'DELETE'})
# def bank():
#     """Route with specific HTTP method."""
#     return 'Contente deleted!'


# @app.route('/', defaults={'name': None}, methods={'GET'})
# @app.route('/<string:name>', methods={'GET'})
# def home(name):
#     """Home view."""
#     return render_template('clientes/home.html', user_name=name)
