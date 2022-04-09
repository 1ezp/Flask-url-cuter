import flask
from main import db

from website.models import Url

db.create_all()