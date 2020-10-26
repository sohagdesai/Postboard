"""Logged-in page routes."""
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
def dashboard():
    """User Dashboard to post articles."""
    form = ArticleForm()
    if form.validate_on_submit():
        article = Article(
            author=current_user.name,
            title=form.title.data,
            body=form.body.data,
            posted_on=datetime.datetime.utcnow
        )
        article.set_author(current_user.name)
        article.set_title(form.title.data)
        article.set_body(form.body.data)
        article.set_posted_on(func.now())
        db.session.add(article)
        db.session.commit()  # Create new article
        return redirect(url_for('main_bp.dashboard'))
    return render_template(
        'dashboard.jinja2',
        title='Post Article Dashboard.',
        form=form,
        template='dashboard-template',
        current_user=current_user,
        body="You may now post an article!"
    )

@main_bp.route("/fetch", methods=['GET'])
@login_required
def articles():
    """Table to view user's articles."""
    form = ArticleForm()
    article = Article(
        author=current_user.name
    )
    results = article.query.filter_by(author=current_user.name)
    headers = TABLE_HEADERS
    return render_template(
        'articles.jinja2',
        title='Article Table.',
        template='dashboard-template',
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
    if form.validate_on_submit():
        article = Article(
            id = article_id,
            author=current_user.name,
            title=form.title.data,
            body=form.body.data,
            posted_on=datetime.datetime.utcnow
        )
        article.set_author(current_user.name)
        article.set_title(form.title.data)
        article.set_body(form.body.data)
        article.set_posted_on(func.now())
        db.session.add(article)
        db.session.commit()  # Update article
        return redirect(url_for('main_bp.dashboard'))
    return render_template(
        'dashboard.jinja2',
        title='Article Dashboard.',
        form=form,
        template='dashboard-template',
        current_user=current_user
    )

@main_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login'))
