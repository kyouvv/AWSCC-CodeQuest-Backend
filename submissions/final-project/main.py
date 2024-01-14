from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fucku'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60))
    password = db.Column(db.String(20))
    website = db.Column(db.String(20))
    
@app.route('/', methods=['GET'])
def index():
    return render_template('accounts.html', users=User.query.all())


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        password = request.form["password"]
        email = request.form["email"]
        website = request.form["website"]
        if website and password and email:
            new_password = User(username=email, password=password, website=website )
            db.session.add(new_password)
            db.session.commit()

            return redirect(url_for('index'))
            
    return render_template('index.html')

@app.route('/remove/<int:id>', methods=['POST', 'GET'])
def remove(id):
    if request.method == 'POST':
        user_to_remove = User.query.get(id)
        if user_to_remove:
            db.session.delete(user_to_remove)
            db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['POST', 'GET'])
def edit(id):
    user_to_edit = User.query.get(id)
    if not user_to_edit:
        return redirect(url_for('index'))

    if request.method == 'POST':
        user_to_edit.username = request.form["new_username"]
        user_to_edit.password = request.form["new_password"]
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit.html', user=user_to_edit)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
