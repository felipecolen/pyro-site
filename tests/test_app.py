import pytest
from flask import url_for

from app import app_site


@pytest.fixture
def app():
    return app_site


def test_index(client):
    response = client.get(url_for('index_html'))
    deve_conter_na_pagina = 'Site da PyRO'

    assert response.status_code == 200
    assert deve_conter_na_pagina
    assert 'esse texto não aparece na página index' not in deve_conter_na_pagina


def test_eventos(client):
    response = client.get(url_for('eventos.index_eventos_html'))
    deve_conter_na_pagina = 'Eventos'

    assert response.status_code == 200
    assert deve_conter_na_pagina
    assert 'esse texto não aparece na página Eventos' not in deve_conter_na_pagina


def test_posts(client):
    response = client.get(url_for('posts_html'))
    deve_conter_na_pagina = 'Posts'

    assert response.status_code == 200
    assert deve_conter_na_pagina
    assert 'esse texto não aparece na página Posts' not in deve_conter_na_pagina


def test_turoriais(client):
    response = client.get(url_for('tutoriais_html'))
    deve_conter_na_pagina = 'Tutoriais'

    assert response.status_code == 200
    assert deve_conter_na_pagina
    assert 'esse texto não aparece na página Tutoriais' not in deve_conter_na_pagina


