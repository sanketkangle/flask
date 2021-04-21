from flask import render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog import app


#dummy data for now, as if we are getting it from DB
posts = [
    {
        'author': "sanket kangle",
        "title": "blog post 1",
        "content": "content for post no. 1",
        "date_posted": "April 20th, 2018"
    },
    {
        'author': "mayur kangle",
        "title": "blog post 2",
        "content": "content for post no. 2",
        "date_posted": "April 22th, 2018"
    }
]

#route for home
#both, "/" as wel as "/home"
@app.route("/")
@app.route("/home")
def home():
    '''
    A function for home page which takes no arguments
    :return: renders from html template and gives back home page
    This posts variable is accessible in the HTML code
    '''
    return render_template('home.html', posts=posts)

#route for about page
@app.route("/about")
def about():
    '''
    returns about page with the title
    :return:
    '''
    return render_template('about.html', title="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for('home'))

    return render_template('register.html', title="Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have logged in successfully!", "success")
            return redirect(url_for('home'))
        else:
            flash("Login Unsuccessful, Please check email and password", 'danger')
    return render_template('login.html', title="Login", form=form)