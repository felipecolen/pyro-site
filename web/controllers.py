from flask import Blueprint, render_template

from web.models import Noticia

site = Blueprint('site', __name__)


@site.route("/teste")
def index():
    return "<h1>hello flask</h1>"


@site.route("/", methods=['GET', 'POST'])
@site.route('/home', methods=['GET', 'POST'])
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

    noticias = Noticia.query.order_by(Noticia.data_adicao.desc())

    return render_template('index.html',
                           # title=_('Home'),
                           # form=form,
                           noticias=noticias
                           )
