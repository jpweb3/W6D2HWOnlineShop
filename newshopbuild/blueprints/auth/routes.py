from flask import Blueprint,  render_template, redirect, url_for, flash, request 
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user

#internal imports

from newshopbuild.forms import RegisterForm, LoginForm
from newshopbuild.models import User, db

#instantiate our  auth blueprint
              #name of blueprint  #import location
auth = Blueprint ('auth', __name__, template_folder= 'auth_templates')

#creating our signgup route/endpoint
@auth.route('/signup', methods= [ 'GET', 'Post'])
def signup():

    registerform = RegisterForm()
    if request.method == 'POST' and registerform.validate_on_submit():
        first_name = registerform.first_name.data
        last_name= registerform.last_name.data
        username = registerform.username.data
        email = registerform.email.data
        password = registerform.password.data
        print(email, password)

        #check the database for the same username and/or email
        #querying thte database!
        if User.query.filter(User.username == username).first():
            flash(' Username already exists. Please try again')
            return redirect('/signup')

        if User.query.filter(User.email == email).first():
            flash('Email already exists. Please try again', category='warning')
            return redirect('/signup')
        

        user = User(username, email, password, first_name=first_name, last_name=last_name)
    
        db.session.add(user)
        db.session.commit()

        flash(f"You have successfully registered user {username}", category='success')
        return redirect('/signin') #we will add signin route 
    
    return render_template('sign_up.html', form=registerform)
