from logging import error
from flask import Flask, render_template, flash, redirect, url_for, session, logging, request, wrappers, jsonify
from functools import wraps
from mysql.connector.cursor import CursorBase, MySQLCursor
from mysql.connector.errors import Error
# from data import Articles
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
# from passlib.hash import sha256_crypt
import mysql.connector
from hashlib import sha256

app = Flask(__name__)

# Config MySQL
mydb = mysql.connector.connect(
    host="40.117.248.43",
    user="root",
    password="Pass@123r",
    port=3306,
    database="myflaskapp"
)

print(mydb)
mycursor = mydb.cursor()

# article = Articles()

# Home


@app.route('/')
def index():
    return render_template('home.html')

# about


@app.route('/about')
def about():
    return render_template('about.html')

# Articles


@app.route('/articles', methods=['GET'])
def articles():
    sql = "SELECT * FROM articles"

    try:
        mycursor.execute(sql)

        doc_2 = mycursor.fetchall()

        if doc_2:
            return render_template('articles.html', articles=doc_2)
            # return jsonify(data=doc_2)

        else:
            msg = 'No Articles Found'
            return render_template('articles.html', msg=msg)

    except Exception as e:
        print("error", e)

# View Article


@app.route('/article/<id>/', methods=['GET'])
def articled(id):
    sql = "SELECT * FROM articles WHERE id = %s"
    val = (id,)

    try:
        mycursor.execute(sql, val)

        doc = mycursor.fetchone()

        return render_template('article.html', article=doc)

    except Exception as e:
        print("error", e)


# Register Form
class RegisterFrom(Form):
    pass
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.data_required(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

# Register


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterFrom(request.form)
    if request.method == 'POST' and form.validate():
        print("will create the user")
        name = form.name.data
        email = form.email.data
        username = form.username.data
        # password = sha256_crypt.encrypt(str(form.password.data))
        password = form.password.data
        password = password.encode('utf-8')
        password = sha256(password).hexdigest()

        print(password)

        # Execute query
        sql = "INSERT INTO user(name, email, username, password) VALUES(%s, %s, %s, %s)"
        val = (name, email, username, password)

        try:
            mycursor.execute(sql, val)
            checkData = mycursor.fetchone()

            print(checkData)

            if checkData:
                flash('username or email already exist', 'danger')
            else:
                sql = "INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)"
                val = (name, email, username, password)

                try:
                    mycursor.execute(sql, val)

                except Exception as e:
                    print("error", e)

                mydb.commit()

                print(mycursor.rowcount, "record inserted.")

                flash('You are now registered and can log in', 'success')

                return redirect(url_for('index'))

        except Exception as e:
            print("error", e)

    return render_template('register.html', form=form)

# Login


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password_candidate = request.form.get('password')

        print(username)
        print(password_candidate)

        sql = "SELECT * FROM user WHERE username = %s"
        val = (username,)

        try:
            mycursor.execute(sql, val)

            doc = mycursor.fetchone()

            if doc:
                print(doc)
                hash_pass = doc[4]
                password = password_candidate.encode('utf-8')
                password = sha256(password).hexdigest()
                print(hash_pass)
                print(password)
                if password == hash_pass:
                    session['logged_in'] = True
                    session['username'] = username
                    app.logger.info('PASSWORD MATCHED')
                    flash('You are now logged in', 'success')
                    return redirect(url_for('dashboard'))
                else:
                    app.logger.info('PASSWORD NOT MATCHED')
                    error = 'Invalid Password'
                    return render_template('login.html', error=error)

            else:
                app.logger.info('NO USER IS MATCHED')
                error = 'Username is not found'
                return render_template('login.html', error=error)

        except Exception as e:
            print("error", e)

    return render_template('login.html')

# Check Session


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

# Logout


@app.route('/logout')
def logout():
    session.clear()
    flash('You are logged out', 'success')
    return redirect(url_for('login'))

# Change Password

# Dashboard


@app.route('/dashboard', methods=['GET', 'POST'])
@is_logged_in
def dashboard():
    sql = "SELECT * FROM articles"

    try:
        mycursor.execute(sql)

        doc_2 = mycursor.fetchall()

        if doc_2:
            return render_template('dashboard.html', articles=doc_2)

        else:
            msg = 'No Articles Found'
            return render_template('dashboard.html', msg=msg)

    except Exception as e:
        print("error", e)

# Article Form


class ArticleForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=200)])
    body = TextAreaField('Body', [validators.Length(min=30)])

# Add Article


@app.route('/add_article', methods=['GET', 'POST'])
@is_logged_in
def add_article():
    form = ArticleForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        body = form.body.data

        print(title)
        print(body)

        sql = "INSERT INTO articles(title, body, author) VALUES(%s, %s, %s)"
        val = (title, body, session['username'],)

        try:
            mycursor.execute(sql, val)

        except Exception as e:
            print("error", e)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

        flash('Article Created', 'success')

        return redirect(url_for('dashboard'))

    return render_template('add_article.html', form=form)

# Edit Article


@app.route("/edit_article/<id>/", methods=['GET', 'POST'])
@is_logged_in
def edit_article(id):
    mycursor.execute("SELECT * FROM articles WHERE id = %s", [id])

    article = mycursor.fetchone()

    form = ArticleForm(request.form)

    form.title.data = article[1]
    form.body.data = article[3]

    if request.method == 'POST' and form.validate():
        title = request.form.get('title')
        body = request.form.get('body')

        print(title)
        print(body)

        app.logger.info(title)

        sql = "UPDATE articles SET title=%s, body=%s WHERE id=%s"
        val = (title, body, id,)
        try:

            mycursor.execute(sql, val)
        except Exception as e:
            print("error", e)

        mydb.commit()

        print(mycursor.rowcount, "record(s) affected")

        flash('Article Updated', 'success')

        return redirect(url_for('dashboard'))

    return render_template('edit_article.html', form=form)


@app.route('/delete_article/<id>', methods=['GET', 'POST'])
def delete_article(id):
    sql = "DELETE FROM articles WHERE id = %s"
    val = (id,)
    try:
        mycursor.execute(sql, val)
    except Exception as e:
        print("error", e)
    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")

    flash('Article Deleted', 'success')

    return redirect(url_for('dashboard'))


app.secret_key = 'secret123'

if __name__ == '__main__':
    app.run(port=5001, debug=True)

# mydb.disconnect()
