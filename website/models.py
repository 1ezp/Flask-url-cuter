from main import db
from sqlalchemy import func

class Url(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    url = db.Column(db.String(50))
    new_url = db.Column(db.String(50))
    date = db.Column(db.DateTime(timezone=True), default = func.now())
    
    