# -*-coding: utf-8-*-
from news.new.admin import admin
from flask import render_template as render, redirect, flash, request, session, url_for
from news.new.admin.forms import GoodsForm, EmployeeForm, SupForm, VipForm, AdminForm
from news.new.modelss import Goods, Employee, Sup, Vip, Admin
from functools import wraps
from news.new.modelss import db, app
from werkzeug.utils import secure_filename
import os
import uuid, datetime


def admin_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "admin" not in session:
            return redirect(url_for("admin.login", next=request.url))
        return f(*args, **kwargs)

    return decorated_function

# 员工列表
@admin.route('/employee/<int:page>', methods=['get', 'post'])
@admin_login_req
def employee(page=None):
    if page is None:
        page = 1
    page_data = Employee.query.order_by(

    ).paginate(page=page, per_page=10)
    return render("admin/employee.html", page_data=page_data)


# 员工添加
@admin.route('/employee/add/', methods=['GET', 'post'])
@admin_login_req
def employee_add():
    form = EmployeeForm()
    if form.validate_on_submit():
        data = form.data
        employee = Goods.query.filter_by(name=data['name']).count()
        if employee == 1:
            flash('名称已经存在', 'err')
            return redirect(url_for('admin.employee_add'))
        employee = Employee(
            name=data['name'],
            sex=data['sex'],
            old=data['old'],
            money=data['money'],
            tel=data['tel'],
            id_card=data['id_card']
        )
        db.session.add(employee)
        try:
            db.session.commit()
        except:
            db.session.rollback()
        flash('添加成功', 'ok')
        redirect(url_for('admin.employee_add'))

    return render('admin/employee_add.html', form=form)


# 编辑员工
@admin.route('/employee/edit/<int:id>/', methods=['POST', 'GET'])
@admin_login_req
def employee_edit(id=None):
    form = EmployeeForm()
    employee = Employee.query.get_or_404(id)
    if form.validate_on_submit():
        data = form.data
        employee_count = Employee.query.filter_by(name=data['name']).count()
        if employee.name != data['name'] and employee_count == 1:
            flash('名称已经存在', 'err')  # 无法判断是否存在  不会
            return redirect(url_for('admin.enployee_edit', id=id))
        employee.name = data['name']
        db.session.add(employee)
        try:
            db.session.commit()
        except:
            db.session.rollback()
        flash('修改成功', 'ok')
        return redirect(url_for('admin.employee_edit', id=id))
    return render("admin/employee_edit.html", form=form, employee=employee)


# 员工删除
@admin.route('/employee/del/<int:id>/', methods=['GET', 'post'])
@admin_login_req
def employee_del(id=None):
    employee = Employee.query.filter_by(id=id).first_or_404()
    db.session.delete(employee)
    db.session.commit()
    flash('删除成功', 'ok')
    return redirect(url_for('admin.employee', page=1))


# 商品列表
@admin.route('/goods/<int:page>/', methods=['GET'])
@admin_login_req
def goods(page=None):
    if page is None:
        page = 1
    page_data = Goods.query.order_by(
        Goods.id.desc()
    ).paginate(page=page, per_page=10)
    return render("admin/goods.html", page_data=page_data)


# 商品添加
@admin.route('/goods/add/', methods=['GET', 'post'])
@admin_login_req
def goods_add():
    form = GoodsForm()
    if form.validate_on_submit():
        data = form.data
        goods = Goods.query.filter_by(name=data['name']).count()
        if goods == 1:
            flash('名称已经存在', 'err')
            return redirect(url_for('admin.goods_add'))
        goods = Goods(
            name=data['name'],
            ontimes=data['ontimes'],
            outtimes=data['outtimes'],
            money=data['money'],
            num=data['num']
        )
        db.session.add(goods)
        try:
            db.session.commit()
        except:
            db.session.rollback()
        flash('添加成功', 'ok')
        redirect(url_for('admin.goods_add'))

    return render('admin/goods_add.html', form=form)


# 编辑商品
@admin.route('/goods/edit/<int:id>/', methods=['POST', 'GET'])
@admin_login_req
def goods_edit(id=None):
    form = GoodsForm()
    goods = Goods.query.get_or_404(id)
    if form.validate_on_submit():
        data = form.data
        goods_count = Goods.query.filter_by(name=data['name']).count()
        if goods.name != data['name'] and goods_count == 1:
            flash('名称已经存在', 'err')  # 无法判断是否存在  不会
            return redirect(url_for('admin.goods_edit', id=id))
        goods.name = data['name']
        db.session.add(goods)
        db.session.commit()
        flash('修改成功', 'ok')
        return redirect(url_for('admin.goods_edit', id=id))
    return render("admin/goods_edit.html", form=form, goods=goods)


# 商品删除
@admin.route('/goods/del/<int:id>/', methods=['GET', 'post'])
@admin_login_req
def goods_del(id=None):
    goods = Goods.query.filter_by(id=id).first_or_404()
    db.session.delete(goods)
    try:
        db.session.commit()
    except:
        db.session.rollback()
    flash('删除成功', 'ok')
    return redirect(url_for('admin.goods', page=1))


# 供货商列表
@admin.route('/sup/<int:page>/', methods=['GET'])
@admin_login_req
def sup(page=None):
    if page is None:
        page = 1
    page_data = Sup.query.order_by(
        Sup.id.desc()
    ).paginate(page=page, per_page=10)
    return render("admin/goods.html", page_data=page_data)


# 供货商添加
@admin.route('/sup/add/', methods=['GET', 'post'])
@admin_login_req
def sup_add():
    form = SupForm()
    if form.validate_on_submit():
        data = form.data
        sup = Sup.query.filter_by(name=data['name']).count()
        if sup == 1:
            flash('名称已经存在', 'err')
            return redirect(url_for('admin.sup_add'))
        sup = Sup(
            name=data['name'],
            goods_name=data['goods_name'],
            tel=data['tel'],

        )
        db.session.add(sup)
        try:
            db.session.commit()
        except:
            db.session.rollback()
        flash('添加成功', 'ok')
        return redirect(url_for('admin.sup_add'))

    return render('admin/sup_add.html', form=form)


# 编辑供货商
@admin.route('/sup/edit/<int:id>/', methods=['POST', 'GET'])
@admin_login_req
def sup_edit(id=None):
    form = GoodsForm()
    sup = Sup.query.get_or_404(id)
    if form.validate_on_submit():
        data = form.data
        sup_count = Sup.query.filter_by(name=data['name']).count()
        if sup.name != data['name'] and sup_count == 1:
            flash('名称已经存在', 'err')  # 无法判断是否存在  不会
            return redirect(url_for('admin.sup_edit', id=id))
        sup.name = data['name']
        db.session.add(sup)
        try:
            db.session.commit()
        except:
            db.session.rollback()
        flash('修改成功', 'ok')
        return redirect(url_for('admin.sup_edit', id=id))
    return render("admin/sup_edit.html", form=form, sup=sup)


# 供货商删除
@admin.route('/sup/del/<int:id>/', methods=['GET', 'post'])
@admin_login_req
def sup_del(id=None):
    sup = Sup.query.filter_by(id=id).first_or_404()
    db.session.delete(sup)
    try:
        db.session.commit()
    except:
        db.session.rollback()
    flash('删除成功', 'ok')
    return redirect(url_for('admin.sup', page=1))


# 会员列表
@admin.route('/vip/<int:page>/', methods=['get', 'post'])
@admin_login_req
def vip(page=None):
    if page is None:
        page = 1
    page_data = Vip.query.order_by(
        Vip.id.desc()
    ).paginate(page=page, per_page=10)
    return render('admin/vip.html', page_data=page_data)


# 会员添加
@admin.route('/vip/add/', methods=['GET', 'post'])
@admin_login_req
def vip_add():
    form = VipForm()
    if form.validate_on_submit():
        data = form.data
        vip = Vip.query.filter_by(name=data['name']).count()
        if vip == 1:
            flash('名称已经存在', 'err')
            return redirect(url_for('admin.vip_add'))
        vip = Vip(
            name=data['name'],
            email=data['email'],
            tel=data['tel'],
            pwd=data['pwd']

        )
        db.session.add(vip)
        try:
            db.session.commit()
        except:
            db.session.rollback()
        flash('添加成功', 'ok')
        return redirect(url_for('admin.vip_add'))

    return render('admin/vip_add.html', form=form)


# 编辑会员
@admin.route('/vip/edit/<int:id>/', methods=['POST', 'GET'])
@admin_login_req
def vip_edit(id=None):
    form = VipForm()
    vip = Vip.query.get_or_404(id)
    if form.validate_on_submit():
        data = form.data
        vip_count = Vip.query.filter_by(name=data['name']).count()
        if sup.name != data['name'] and vip_count == 1:
            flash('名称已经存在', 'err')  # 无法判断是否存在  不会
            return redirect(url_for('admin.vip_edit', id=id))
        vip.name = data['name']
        db.session.add(vip)
        try:
            db.session.commit()
        except:
            db.session.rollback()
        flash('修改成功', 'ok')
        return redirect(url_for('admin.vip_edit', id=id))
    return render("admin/vip_edit.html", form=form, vip=vip)


# 会员删除
@admin.route('/vip/del/<int:id>/', methods=['GET', 'post'])
@admin_login_req
def vip_del(id=None):
    vip = Vip.query.filter_by(id=id).first_or_404()
    db.session.delete(vip)
    try:
        db.session.commit()
    except:
        db.session.rollback()
    flash('删除成功', 'ok')
    return redirect(url_for('admin.vip', page=1))


# 管理员列表
@admin.route('/a_list/<int:page>/', methods=['get', 'post'])
@admin_login_req
def a_list(page=None):
    if page is None:
        page = 1
    page_data = Admin.query.order_by(
        Admin.id.desc()
    ).paginate(page=page, per_page=10)

    return render('admin/a_list.html', page_data=page_data)


@admin.route('/a/change/')
@admin_login_req
def a_change():
    return render('admin/a_change.html')


# 管理员添加
@admin.route('/a/add/', methods=['GET', 'post'])
@admin_login_req
def a_add():
    form = AdminForm()
    from werkzeug.security import generate_password_hash
    if form.validate_on_submit():
        data = form.data
        admin = Admin(
            name=data['name'],
            pwd=generate_password_hash(data['pwd']),
            tel=data['tel'],
        )
        db.session.add(admin)
        try:
            db.session.commit()
        except:
            db.session.rollback()
        flash('添加管理员成功', 'ok')
        return redirect(url_for('admin.a_add'))
    return render('admin/a_add.html', form=form)


@admin.route('/a/del/<int:id>/', methods=['GET', 'post'])
@admin_login_req
def a_del(id=None):
    admin = Admin.query.filter_by(id=id).first_or_404()
    db.session.delete(admin)
    try:
        db.session.commit()
    except:
        db.session.rollback()
    flash('删除成功', 'ok')
    return redirect(url_for('admin.a_list', page=1))


@admin.route('/login/')
def login():
    return render('admin/login.html')
