""""Logged-in page routes."""
import datetime
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user, login_required, logout_user
from .forms import ArticleForm
from .models import db, Article
from . import redis_client
from . import cache
from sqlalchemy.sql import func
import json


TABLE_HEADERS = ["ID", "Author", "Title", "Body", "Created", "Updated"]

# Blueprint Configuration
main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@main_bp.route("/add", methods=['GET','POST'])
@login_required
def add_article():
    """Form to post articles."""
    form = ArticleForm()
    if form.validate_on_submit():
        article = Article(
            author=current_user.name,
            title=form.title.data,
            body=form.body.data,
            created_at=datetime.datetime.utcnow
        )
        article.set_author(current_user.name)
        article.set_title(form.title.data)
        article.set_body(form.body.data)
        create_time = func.now()
        article.set_created_at(create_time)
        article.set_updated_at(create_time)
        db.session.add(article)
        db.session.commit()                                                         # Create new article in db
        db_row = Article.query.filter_by(created_at=article.created_at).first()     # Fetch row for caching
        db_row_dict = row2dict(db_row)                                              # Convert to dictionary
        cache.update_cache(db_row_dict)                                             # Update cache
        return redirect(url_for('main_bp.add_article'))
    return render_template(
        'edit_article.jinja2',
        title='Form to Post Articles.',
        form=form,
        template='add_article-template',
        current_user=current_user,
        body="You may now post an article!"
    )

@main_bp.route("/fetch", methods=['GET'])
@login_required
def fetch_articles():
    """Table to view user's articles."""
    form = ArticleForm()
    article = Article(
        author=current_user.name
    )
    results = Article.query.filter_by(author=current_user.name).order_by(Article.created_at)
    headers = TABLE_HEADERS
    return render_template(
        'show_articles.jinja2',
        title='Article Table.',
        template='add_article-template',
        headers=headers,
        form=form,
        results=results,
        current_user=current_user,
        body="Here are your articles."
    )

@main_bp.route("/edit", methods=['GET', 'POST'])
@login_required
def edit_article():
    """Form to edit article."""
    form = ArticleForm()
    article_id = request.args.get('article_id')
    if article_id is not None:
        article = Article(
            id=article_id
        )
        #print (f"article_id = {article_id}")
        content = cache.get_cache(str(article_id))
        #content = article.query.filter_by(id=article_id).first()
        form.title.data = content["title"]
        form.body.data = content["body"]
    
    else: 
        if form.title.data and form.body.data is not None:
            article = Article(
                title=form.title.data
            )
            article.set_author(current_user.name)
            article.set_title(form.title.data)
            article.set_body(form.body.data)
            content = Article.query.filter_by(title=form.title.data).first()
            if content is not None:
                article.set_id(content.id)
                article.set_updated_at(func.now())
                db.session.merge(article) # Update article
                db.session.flush() 
            else:
                article.set_created_at(func.now())
                article.set_updated_at(article.created_at)
                db.session.add(article)   # Add article
            db.session.commit()
            db_row = Article.query.filter_by(id=article.id).first()  # Fetch row for caching
            db_row_dict = row2dict(db_row)
            cache.update_cache(db_row_dict)  # Update cache
            return redirect(url_for('main_bp.add_article'))

    return render_template(
        'edit_article.jinja2',
        title='Post Article Form.',
        form=form,
        template='add_article-template',
        current_user=current_user
    )

@main_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login'))

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d
