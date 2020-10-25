"""Database models."""
import datetime
from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
	"""User account model."""

	__tablename__ = 'PB_User'
	id = db.Column(
		db.Integer,
		primary_key=True
	)
	name = db.Column(
		db.String(256),
		nullable=False,
		unique=False
	)
	email = db.Column(
		db.String(40),
		unique=True,
		nullable=False
	)
	password = db.Column(
		db.String(200),
		primary_key=False,
		unique=False,
		nullable=False
	)
	created_on = db.Column(
        	db.DateTime,
                default=datetime.datetime.utcnow,
        	index=False,
        	unique=False,
        	nullable=True
    	)
	last_login = db.Column(
        	db.DateTime,
        	index=False,
        	unique=False,
        	nullable=True
    	)

	def set_password(self, password):
		"""Create hashed password."""
		self.password = generate_password_hash(password, method='sha256')

	def check_password(self, password):
		"""Check hashed password."""
		return check_password_hash(self.password, password)

	def __repr__(self):
		return '<User {}>'.format(self.username)

class Article(db.Model):
	"""Article model."""

	__tablename__ = 'PB_Article'
	id = db.Column(
		db.Integer,
		primary_key=True
	)
	author = db.Column(
		db.String(256),
		nullable=False,
		unique=False
	)
	title = db.Column(
		db.String(256),
		nullable=False,
		unique=False
	)
	body = db.Column(
		db.String(4096),
		nullable=False,
		unique=False
	)
	posted_on = db.Column(
        	db.DateTime,
                default=datetime.datetime.utcnow,
        	index=False,
        	unique=False,
        	nullable=True
    	)
	def set_author(self, author):
		"""Set article author."""
		self.author = author

	def set_title(self, title):
		"""Set article title."""
		self.title = title

	def set_body(self, body):
		"""Set article body."""
		self.body = body

	def set_posted_on(self, posted_on):
		"""Set posted time."""
		self.posted_on = posted_on
