from market import app
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from market import db

#routes

#====home route======
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

#====market route=====
@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

#====register route=====
@app.route('/register', methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit(): #if user clicked SUBMIT
        user_to_create = User(username=form.username.data,
                                email=form.email.data,
                                password=form.password1.data)

        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    # if any of our validators fail, it will be stored in form.errors
    if form.errors != {}: #if there are no errors from the validations
        for error in form.errors.values():
            flash(f'There was an error: {error}', category="danger")
            # print("EERROORR: ",error)
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET','POST'])
def login_page():
    form = LoginForm()
    
    return render_template('login.html', form=form)