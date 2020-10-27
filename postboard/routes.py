""""Logged-in page routes."""
import datetime
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user, login_required, logout_user
from .forms import ArticleForm
from .models import db, Article
from sqlalchemy.sql import func


TABLE_HEADERS = ["ID", "Author", "Title", "Body", "Posted On"]

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
            posted_on=datetime.datetime.utcnow
        )
        print ("======================================")
        print (f"form.title.data = {form.title.data}")
        print (f"form.body.data= {form.body.data}")
        print ("======================================")
        article.set_author(current_user.name)
        article.set_title(form.title.data)
        article.set_body(form.body.data)
        article.set_posted_on(func.now())
        db.session.add(article)
        db.session.commit()  # Create new article
        return redirect(url_for('main_bp.add_article'))
    return render_template(
        'add_article.jinja2',
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
    results = article.query.filter_by(author=current_user.name)
    headers = TABLE_HEADERS
    return render_template(
        'show_articles.jinja2',
        title='Article Table.',
        template='edit_article-template',
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
        print ("======================================")
        print (f"Article ID = {article_id}")
        print ("======================================")
        article = Article(
            id=article_id
        )
        content = article.query.filter_by(id=article_id).first()
        print ("======================================")
        print (f"content.id = {content.id}")
        print (f"content.title = {content.title}")
        print (f"content.body = {content.body}")
        print (f"content.posted_on = {content.posted_on}")
        print ("======================================")
        form.title.data = content.title 
        form.body.data = content.body 
    
    else: 
        if form.title.data and form.body.data is not None:
            article = Article(
                title=form.title.data
            )
            print (f"Article ID is None; article title = {form.title.data}")
            content = Article.query.filter_by(title=form.title.data).first()
            print (f"Article ID is None; content = {content}")
            print ("======================================")
            print (f"Form data is not None; article id = {content.id}")
            print (f"Form data is not None; article title = {form.title.data}")
            print (f"Form data is not None; article body = {form.body.data}")
            print ("======================================")
            article.set_id(content.id)
            article.set_author(current_user.name)
            article.set_title(form.title.data)
            article.set_body(form.body.data)
            article.set_posted_on(func.now())
            print ("Almost ready to commit")
            db.session.merge(article)  # Update article
            db.session.flush()  # Update article
            db.session.commit()  # Update article
            return redirect(url_for('main_bp.edit_article'))

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
