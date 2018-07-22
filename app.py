import os

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))

from web import create_app
app = create_app()


if __name__ == '__main__':

    app.config.update(
        TESTING=True,
        SECRET_KEY=b'insira_uma_key_aqui',
        DEBUG=True,
        SQLALCHEMY_ECHO=True,
        SQLALCHEMY_DATABASE_URI='sqlite: ///' + os.path.join(basedir, 'banco_app.sqlite'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    app.run(host='0.0.0.0', port=5000)
