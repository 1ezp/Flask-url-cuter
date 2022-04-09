import flask
from . import db

from .models import Url

db.create_all()