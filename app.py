import os

from flask import Flask, render_template

basedir = os.path.abspath(os.path.dirname(__file__))
app_site = Flask(__name__)


@app_site.route("/teste")
def index():
    return "<h1>hello flask</h1>"


@app_site.route("/")
def index_html():

    # form = PostForm()
    # if form.validate_on_submit():
    #     language = guess_language(form.post.data)
    #     if language == 'UNKNOWN' or len(language) > 5:
    #         language = ''
    #     post = Post(body=form.post.data, author=current_user,
    #                 language=language)
    #     db.session.add(post)
    #     db.session.commit()
    #     flash(_('Your post is now live!'))
    #     return redirect(url_for('main.index'))
    # page = request.args.get('page', 1, type=int)
    # posts = current_user.followed_posts().paginate(
    #     page, current_app.config['POSTS_PER_PAGE'], False)
    # next_url = url_for('main.index', page=posts.next_num) \
    #     if posts.has_next else None
    # prev_url = url_for('main.index', page=posts.prev_num) \
    #     if posts.has_prev else None

    # noticias = Noticia.query.order_by(Noticia.data_adicao.desc())

    return render_template('index.html',
                           # title=_('Home'),
                           # form=form,
                           # noticias=noticias
                           )


@app_site.route("/eventos")
def eventos_html():

    return render_template('eventos.html', )


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
