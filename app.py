from enum import unique
from os import name
from warnings import catch_warnings
from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError, DataRequired, email_validator
import sqlalchemy
app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
setup_questions = []

#Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("Let's get you set up", validators=[DataRequired()])
    submit = SubmitField("Set up")


class SetupQuestion(db.Model):
    __tablename__ = 'setup_question'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(300), nullable=False, unique=True)
    Type = db.Column(db.String(50), nullable=False)
    ListValues = db.Column(db.String(300))
    ans1 = db.Column(db.String(50))
	

class Userquestion:
    def __init__(self):
        self.q_count=-1
        self.setup_questions = SetupQuestion.query.all()
        
    def counter():
        print("one")

    def __len__(self):
        return len(self.setup_questions)

user_question = Userquestion()


@app.route('/setup')
def setup():
    user_question.q_count += 1
    button_name = "Next"
    if user_question.q_count == len(user_question.setup_questions)-1:
        button_name = "submit"
    return render_template('setup.html', question=user_question.setup_questions[user_question.q_count].question,button_name=button_name,question_type = user_question.setup_questions[user_question.q_count].Type,listval = user_question.setup_questions[user_question.q_count].ListValues)

@app.route('/thanks')
def thanks():
    user_question.q_count = 0
    return render_template('thanksyou.html')

@app.route('/')
def index():
    return render_template("login.html")


# @app.route('/setup', methods=['POST','GET'])
# def setup():
#     # name = None
#     # form = NamerForm()
#     # if form.validate_on_submit():
#     #     name = form.name.data
#     #     form.name.data = ''
#     # return render_template("setup.html" ,form = form, name = name)
#     try:
#         global iterques
#         #if len(setup_questions)==0:
#         #setup_questions = SetupQuestion.query.all()
#         #a = next(iter(setup_questions))
#         #print(a.question)
#         print(type(setup_questions))
#         print(len(setup_questions))
        
#         #print(next(iter(setup_questions)).question)
#         print("1")
#         #a = next(iter(iterques))
#         print("2")
#         #print(a)
#         q_text = '<ul>'
#         q_text += '<li>' + next(iterques).question  + '</li>'
#         #q_text += '<li>' + "hello"  + '</li>'
#         q_text += '</ul>'  
#         print("hi")
#         print(q_text)
#         #for i in setup_questions:
#         #    q_text += '<li>' + a.question  + '</li>'
#         #    q_text += '</ul>'  
          
#         # myques = next(iter(setup_questions))
#         # print(myques.question)
#         # #setup_questions = SetupQuestion.query.all()
#         # q_text = '<ul>'
#         # q_text += '<li>' + myques.question + '</li>'
#         # q_text += '</ul>'
#         # print("hi")
#         return render_template("setup.html" ,q_text = q_text)
#     except Exception as e:
#         # e holds description of the error
#         error_text = "<p>The error:<br>" + str(e) + "</p>"
#         hed = '<h1>Something is broken.</h1>'
#         return hed + error_text


database={'tsai':'tsai99!'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
	    return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
	         return render_template('index.html',name=name1)

 #   return render_template("index.html")

@app.route('/next',methods=['POST'])
def next(self):
    print("dei")
    try:
        q_text = '<ul>'
        q_text += '<li>' + "ihjk" + '</li>'
        q_text += '</ul>'
        return redirect("setup.html" ,q_text = q_text)
    except StopIteration:
        print("vaada")

@app.route('/logout',methods=['POST','GET'])
def logout():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)