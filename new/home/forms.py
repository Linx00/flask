# time2018/1/21
# coding:utf-8
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Regexp, ValidationError, EqualTo
from news.new.modelss import Admin, Vip


class LoginForm(FlaskForm):
    """ 管理员登录表单"""
    account = StringField(
        label="账号",
        validators=[
            DataRequired("请输入账号")
        ],
        description="账号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号！",

        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("请输入密码")
        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码！",

        }
    )
    submit = SubmitField(
        '登录',
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
        }
    )

    def validate_account(self, field):
        account = field.data
        admin = Admin.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError("账号不存在")


class RegisterForm(FlaskForm):
    name = StringField(
        label="昵称",
        validators=[
            DataRequired("请输入昵称")
        ],
        description="昵称",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入昵称！",

        }
    )
    email = StringField(
        label="邮箱",
        validators=[
            DataRequired("请输入邮箱"),
            Email(message='邮箱格式不正确')
        ],
        description="邮箱",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入邮箱！",

        }
    )
    tel = StringField(
        label="联系方式",
        validators=[
            DataRequired("请输入联系方式"),
            Regexp('1[3458]\d{9}', message='手机格式不正确')
        ],
        description="联系方式",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入联系方式！",

        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("请输入密码")
        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码！",

        }
    )
    repwd = PasswordField(
        label="确认密码",
        validators=[
            DataRequired("请输入确认密码"),
            EqualTo('pwd', message='两次密码不一致')
        ],
        description="确认密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入确认密码！",

        }
    )
    submit = SubmitField(
        '注册',
        render_kw={
            'class': "btn btn-warning btn-block"
        }
    )

    def validate_name(self, field):
        name = field.data
        vip = Vip.query.filter_by(name=name).count()
        if vip == 1:
            raise ValidationError("昵称已经被使用")

    def validate_email(self, field):
        email = field.data
        vip = Vip.query.filter_by(email=email).count()
        if vip == 1:
            raise ValidationError("邮箱已经被使用")

    def validate_tel(self, field):
        tel = field.data
        vip = Vip.query.filter_by(tel=tel).count()
        if vip == 1:
            raise ValidationError("手机号已经被使用")
