from flask import Flask, render_template,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title ='home')

@app.route('/profile')
def profile():
    return render_template('profile.html', title ='home')

@app.route('/single')
def single():
    return render_template('single.html', title ='home')

@app.route('/login')
def login():
    return render_template('login.html', title ='home')
    

@app.route('/register')
def register():
    return render_template('register.html', title ='home')
    