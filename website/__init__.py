from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hikmetapp'
    app.config['DATABASE_URI'] = f'postgres://wmpgbrbncsehuc:2960f1fd82fee4762c0eb17fbbc1a09277d0180aaf1df5a975facefe1b37ea98@ec2-34-207-12-160.compute-1.amazonaws.com:5432/d5g0q218b88fur'
    db.init_app(app)
    
    from .views import views
    
    app.register_blueprint(views,url_prefix='/')
    
    from .models import Url
    create_database(app)
    
    
    return app
    
def create_database(app):
    if not path.exists('website/'+DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
