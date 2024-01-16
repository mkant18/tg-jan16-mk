from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mysite/data.sqlite'
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    # Add other fields as per your database schema

@app.route('/')
def index():
    messages = Message.query.all()
    # Pass additional data as needed for your template
    return render_template('mysite/template.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
