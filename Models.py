from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #SQLAlchemy를 사용해 데이터베이스 저장

class User(db.Model): #데이터 모델을 나타내는 객체 선언
    __tablename__ = 'user_table' #테이블 이름  
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(32), unique=True, nullable=False)
    userid = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(8), nullable=False)
    re_password = db.Column(db.String(8), nullable=False)

