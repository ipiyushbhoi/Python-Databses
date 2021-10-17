import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/GITHUB/Python-Databses/SQL-Alchemy/test.db'

#
# Alertnative way: use os.getcwd()
# current_path = os.getcwd
# database_name = test.db
# app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{current_path}/{database_name}
#

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = "student"

    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    age = db.Column(db.Integer)
    grade = db.Column(db.String)

    def __init__(self, userid, username, age, grade):
        self.userid = userid
        self.username = username
        self.age = age
        self.grade = grade

    def __repr__(self):
        return f"Student({self.username}, {self.age}, {self.grade})"

# CREATE TABLE "student"
db.create_all() 

# INSERT VALUES TO TABLE "student"
student1 = Student(300, 'Bill', 24, 'A+')
db.session.add(student1)
student2 = Student(301, 'Jason', 25, 'A')
db.session.add(student2)
db.session.commit()

# GET DATA FROM TABLE "student" 
print(Student.query.all()) 
print(Student.query.filter_by(userid=301).first())