from flask import Blueprint, render_template



#we need to instantiate our Blueprint object
site = Blueprint('site', __name__, template_folder='site_templates') #telling your blueprint where to load the html files 



#create our first route
@site.route('/')
def shop():
    return render_template('shop.html')#basically displaying out shop.html page