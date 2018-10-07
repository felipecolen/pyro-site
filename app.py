import os

from flask import Flask, render_template

from views import eventos

basedir = os.path.abspath(os.path.dirname(__file__))
app_site = Flask(__name__)

app_site.register_blueprint(eventos.modulo_eventos)


@app_site.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app_site.route("/")
def index_html():

    return render_template('index.html', )


@app_site.route("/posts")
def posts_html():

    return render_template('posts.html', )


@app_site.route("/tutoriais")
def tutoriais_html():

    return render_template('tutoriais.html', )


if __name__ == '__main__':
    app_site.config.update(
        TESTING=True,
        SECRET_KEY=b'insira_uma_key_aqui',
        DEBUG=True,
        SQLALCHEMY_ECHO=True,
        SQLALCHEMY_DATABASE_URI='sqlite: ///' + os.path.join(basedir, 'banco_app.sqlite'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    app_site.run(host='0.0.0.0', port=5000)
