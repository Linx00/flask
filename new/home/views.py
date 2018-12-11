# -*-coding: utf-8-*-
from . import home
from flask import render_template, redirect, flash, request, session, url_for
from news.new.home.forms import LoginForm, RegisterForm
from news.new.modelss import Admin, Goods, Vip
from news.new.modelss import db


@home.route('/', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(name=data["account"]).first()
        if not admin.check_pwd(data['pwd']):
            flash('密码错误')
            return redirect(url_for("home.login"))
        session['admin'] = data['account']
        return redirect(url_for('admin.employee', page='1'))

    return render_template("home/login.html", form=form)


@home.route('/about/')
def about():
    return render_template('home/about.html')


@home.route('/check/')
def check():
    return render_template('home/check.html')


@home.route('/study/<int:page>/', methods=['GET', 'post'])
def study(page=None):
    if page is None:
        page = 1
    page_data = Goods.query.order_by(
        Goods.id.desc()
    ).paginate(page=page, per_page=10)
    return render_template('home/study.html', page_data=page_data)


@home.route('/get_back/')
def get_back():
    return render_template('home/get_back.html')


#
#
@home.route('/home/')
def _home():
    return render_template('home/home.html')


@home.route('/register/', methods=['post', 'get'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data
        vip = Vip(
            name=data['name'],
            email=data['email'],
            tel=data['tel'],
            pwd=data['pwd'],
        )
        db.session.add(vip)
        try:
            db.session.commit()
        except:
            db.session.rollback()
        flash('注册成功', 'ok')
    return render_template('home/register.html', form=form)

#
# @home.route('/<file>')
# def total(file):
#     if file.endswith('.html'):
#         username = request.args.get('home')
#         return render_template(file, username=username)
#     else:
#         return ''
