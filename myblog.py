from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '40f650329c81b4d8d5d6b4078bfb0a02'

posts = [
    {
    'title' : 'Post 1',
    'author' : 'Darshan',
    'content' : 'I am in possesion of 130,000 dollars or 95,00,000 rs per year.',
    'date_posted' : '25/3/2021'
    },
    {
    'title' : 'Post 1',
    'author' : 'Darshan',
    'content' : 'In return of this money I work for Google Mountain View California',
    'date_posted' : '25/3/2021'
    }
]

details = 'My name is Darshan, I am a succesful DataScientist and a self made Millionare.'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
