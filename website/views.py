from flask import Blueprint,render_template,request,flash,redirect
from .models import Url
from . import db
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
                print(new_url,request.base_url)
                db.session.add(u)
                db.session.commit()
                if 'cute' in str(request.base_url):
                    base = str(request.base_url).split('/cute')[0]
                flash(base+'/'+new_url,category='success')
                break
        print(url)
    return render_template('base.html')

@views.route('/<string:ur>')
def re(ur):
    if 'cute' in ur:
        ur = ur.split('cute')[1]
    y = Url.query.filter_by(new_url=ur).first()
    
    return redirect(y.url)
