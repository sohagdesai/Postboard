"""Routes for posting and editing an article."""
from flask import redirect, render_template, flash, Blueprint, request, url_for
from flask_login import current_user, login_user
from .forms import ArticleForm
from .models import db, User
from .import login_manager


# Blueprint Configuration
article_bp = Blueprint(
    'article_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@article_bp.route('/', methods=['GET', 'POST'])
def add():
    """
    Add article page.

    GET requests serve articles.
    POST requests create articles.
    """
    form = ArticleForm()
    if form.validate_on_submit():
        existing_author = Article.query.filter_by(author=current_user.name).first()
        existing_title = Article.query.filter_by(title=form.title.data).first()
        existing_body = Article.query.filter_by(body=form.body.data).first()
        if existing_author is None:
            article =Article(
                author=current_user.name
            )
            article.set_author(current_user.name)
            db.session.add(author)
            db.session.commit()  # Create new author
        if existing_title is None:
            article =Article(
                title=form.title.data
            )
            article.set_title(form.title.data)
            db.session.add(title)
            db.session.commit()  # Create new title
        if existing_body is None:
            article =Article(
                body=form.body.data
            )
            article.set_body(form.body.data)
            db.session.add(body)
            db.session.commit()  # Create new body
        return redirect(url_for('main_bp.dashboard'))
    return render_template(
        'dashboard.jinja2',
        title='Create an Article.',
        form=form,
        template='dashboard-page',
        body="Title of article."
    )
