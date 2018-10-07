from flask import render_template, Blueprint, abort

modulo_eventos = Blueprint('eventos', __name__, url_prefix='/eventos')


@modulo_eventos.route("/")
def index_eventos_html():

    return render_template('eventos.html', )


@modulo_eventos.route('/<string:slug>/', methods=['GET'])
def evento_html(slug):
    # dados_do_evento = Evento.query.get(slug)
    dados_do_evento = None
    if dados_do_evento is None:
        abort(404)

    return render_template(
        'evento.html',
        dados_do_evento=dados_do_evento
    )
