from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import column,Integer,String
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine
import pymysql

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1:3306/market"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = '4e663acccb544b4f8a9afeaac7e48e6f'

app.debug = True

db = SQLAlchemy(app)


# 管理员列表
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    tel = db.Column(db.Integer, unique=True)
    addtimer = db.Column(db.DateTime, index=True, default=datetime.now())

    # student = db.relationship('Student', backref="admin")

    def __repr__(self):
        return "<Admin %r>" % self.name

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)


# 员工列表
class Employee(db.Model):
    __tablename__ = "employee"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 姓名
    sex = db.Column(db.String(4))  # 性别
    old = db.Column(db.Integer)  # 年龄
    money = db.Column(db.String(100))  # 工资
    tel = db.Column(db.Integer, unique=True)  # 联系方式
    id_card = db.Column(db.Integer, unique=True)  # 身份证号

    def __repr__(self):
        return "<Employee %r>" % self.name


# 商品列表
class Goods(db.Model):
    __tablename__ = "goods"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100))
    ontimes = db.Column(db.Integer)  # 生产日期
    outtimes = db.Column(db.Integer)  # 有效期
    money = db.Column(db.Integer)  # 价格
    num = db.Column(db.Integer)  # 价格

    def __repr__(self):
        return "<Goods %r>" % self.name


# 会员列表
class Vip(db.Model):
    __tablename__ = "vip"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100))  # 姓名
    email = db.Column(db.String(100), unique=True)  # 邮箱
    tel = db.Column(db.String(11), unique=True) #联系方式
    pwd = db.Column(db.String(100))  # 密码
    addtimer = db.Column(db.DateTime, index=True, default=datetime.now())

    def __repr__(self):
        return "<Vip %r>" % self.name


# 供应商
class Sup(db.Model):
    __tablename__ = "sup"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100))  # 姓名
    goods_name = db.Column(db.String(100))  # 商品名称
    tel = db.Column(db.Integer, unique=True)  # 联系方式

    def __repr__(self):
        return "<Sup %r>" % self.name


if __name__ == "__main__":
    db.create_all()

    # goods = Goods(
    #         name ='测试1',outtimes='14',ontimes='15'
    # )
    # db.session.add(goods)
    # db.session.commit()  #增加一行元素

    # from werkzeug.security import generate_password_hash
    # admin = Admin(
    #      name="root",
    #      pwd=generate_password_hash("123456"),
    #      tel='123123'
    # )
    # db.session.add(admin)
    # db.session.commit()

# db.session.delete(Admin(id =='1'))
# sql=db.session.query(Admin)
# print('sql')
# db.session.query_property(Admin.id<2).delete()
# db.session.commint()


# Session = sessionmaker(bind=create_engine())
# session = Session()
#
# ob = Admin(id ='1',ad_name='11',ad_pwd='111',ad_tel='1111')
# session.commit()
