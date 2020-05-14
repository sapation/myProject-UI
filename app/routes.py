from flask import render_template,url_for,flash,redirect,request
from app.forms import RegistrationForm, loginForm, UpdateProfileForm
from app import app, db, bcrypt
from app.models import User
from flask_login import login_user,current_user,logout_user,login_required


@app.route('/')
def index():
    return render_template('index.html', title ='home')


@app.route('/profile/<username>', methods=['GET', 'POST'])
@login_required
def profile(username):
    form = UpdateProfileForm()
    image_file = url_for('static', filename='images/profile/' + current_user.image)
    return render_template('profile.html', title ='profile', image_file=image_file, form=form)

@app.route('/single')
def single():
    return render_template('single.html', title ='single')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash("Please Check your Email or password", "danger")    
    return render_template('login.html', title ='login', form=form)
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, username = form.username.data, email = form.email.data, password = hash_password)
        db.session.add(user)
        db.session.commit()
        flash("Accounts Created Successfully Please Login with your Credentials", "success")
        return redirect(url_for('login'))
    return render_template('register.html', title ='Register', form=form)
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))