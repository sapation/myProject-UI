from flask import Flask, render_template,url_for,flash,redirect
from app.forms import RegistrationForm, loginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e01a3e6fd7d396d2de7697c0d424fe6e'

@app.route('/')
def index():
    return render_template('index.html', title ='home')

@app.route('/profile')
def profile():
    return render_template('profile.html', title ='profile')

@app.route('/single')
def single():
    return render_template('single.html', title ='single')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        print(form)
        if form.email.data =="admin@gmail.com" and form.password.data =="password":
            return redirect(url_for('index'))
        else:
            flash("Please Check your Email or password", "danger")    
    return render_template('login.html', title ='login', form=form)
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash("Accounts Created Successfully Please Login with your Credentials", "success")
        return redirect(url_for('login'))
    return render_template('register.html', title ='Register', form=form)
    