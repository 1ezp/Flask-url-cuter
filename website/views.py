from flask import Blueprint,render_template,request,flash,redirect
from .models import Url
from main import db
import json,random
views = Blueprint('views',__name__)
randomletters = 'qwertyuiopasdfghjklzxcvbnm123456789'
@views.route('/')
def home():
    
    return render_template('base.html')

@views.route('/cute',methods=['GET','POST'])
def cute():
    if request.method == 'POST':
        url = request.form.get('url')
        
        while True:
            
            new_url = str("".join(random.choice(randomletters) for i in range(5)))
            y = Url.query.filter_by(url=new_url).first()
            if y:
                pass
            else:
                u = Url(url=url,new_url=new_url)
                db.session.add(u)
                db.session.commit()
                flash(request.base_url+new_url,category='success')
                break
        print(url)
    return render_template('base.html')

@views.route('/<string:url>')
def re(url):
    y = Url.query.filter_by(new_url=url).first()
    return redirect(y.url)
