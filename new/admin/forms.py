# time2018/2/23
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField, FileField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from news.new.modelss import Goods, Employee, Sup, Vip, Admin

goods = Goods.query.all()
employee = Employee.query.all()
sup = Sup.query.all()
vip = Vip.query.all()
admin = Admin.query.all()


class GoodsForm(FlaskForm):
    name = TextAreaField(
        label='名称',
        validators=[
            DataRequired('请输入名称')
        ],
        description='名称',
        render_kw={
            " class=": 'form - control',
            "row": 100

        }
    )

    ontimes = StringField(
        label='生产日期',
        validators=[
            DataRequired('请输入生产日期')
        ],
        description='生产日期',
        render_kw={
            " class=": 'form - control',
            " placeholder": '请输入生产日期！',
            "id": "input_ontimes"
        }
    )
    outtimes = StringField(
        label='保质期',
        validators=[
            DataRequired('请输入保质期')
        ],
        description='保质期',
        render_kw={
            " class=": 'form - control',
            " id=": 'input_name',
            " placeholder": '请输入保质期！'

        }
    )

    money = StringField(
        label='价格',
        validators=[
            DataRequired('请输入价格')
        ],
        description='价格',
        render_kw={
            " class=": 'form - control',
            " placeholder": '请输入价格！'

        }
    )

    num = StringField(
        label='数量',
        validators=[
            DataRequired('请输入数量')
        ],
        description='数量',
        render_kw={
            " class=": 'form - control',
            " placeholder": '请输入数量！'

        }
    )

    submit = SubmitField(
        '编辑',
        render_kw={
            "class": "btn btn-primary"
        }
    )


class EmployeeForm(FlaskForm):
    name = TextAreaField(
        label='姓名',
        validators=[
            DataRequired('请输入姓名')
        ],
        description='姓名',
        render_kw={
            " class=": 'form - control',
            "row": 100,
            " placeholder": '请输入姓名！',
        }
    )

    sex = StringField(
        label='性别',
        validators=[
            DataRequired('请输入性别')
        ],
        description='性别',
        render_kw={
            " class=": 'form - control',
            " placeholder": '请输入性别！',

        }
    )
    old = StringField(
        label='年龄',
        validators=[
            DataRequired('请输入年龄')
        ],
        description='年龄',
        render_kw={
            " class=": 'form - control',
            " id=": 'input_name',
            " placeholder": '请输入年龄！'

        }
    )

    money = StringField(
        label='工资',
        validators=[
            DataRequired('请输入工资')
        ],
        description='工资',
        render_kw={
            " class=": 'form - control',
            " placeholder": '请输入工资！'

        }
    )

    tel = StringField(
        label='联系方式',
        validators=[
            DataRequired('请输入联系方式')
        ],
        description='联系方式',
        render_kw={
            " class=": 'form - control',
            " placeholder": '请输入联系方式！'

        }
    )
    id_card = StringField(
        label='身份证号码',
        validators=[
            DataRequired('请输入身份证号码')
        ],
        description='身份证号码',
        render_kw={
            " class=": 'form - control',
            " placeholder": '请输入身份证号码！'

        }
    )

    submit = SubmitField(
        '编辑',
        render_kw={
            "class": "btn btn-primary"
        }
    )


class SupForm(FlaskForm):
    name = TextAreaField(
        label='名称',
        validators=[
            DataRequired('请输入名称')
        ],
        description='名称',
        render_kw={
            " class=": 'form - control',
            "row": 100

        }
    )

    goods_name = StringField(
        label='商品名称',
        validators=[
            DataRequired('请输入商品名称')
        ],
        description='商品名称',
        render_kw={
            " class=": 'form - control',
            " placeholder": '请输入商品名称！',

        }
    )
    tel = StringField(
        label='联系方式',
        validators=[
            DataRequired('请输入联系方式')
        ],
        description='联系方式',
        render_kw={
            " class=": 'form - control',
            " id=": 'input_name',
            " placeholder": '请输入联系方式！'

        }
    )

    submit = SubmitField(
        '编辑',
        render_kw={
            "class": "btn btn-primary"
        }
    )


class VipForm(FlaskForm):
    name = TextAreaField(
        label='昵称',
        validators=[
            DataRequired('请输入昵称')
        ],
        description='名称',
        render_kw={
            " class=": 'form - control',
            "row": 100,
            " placeholder": '请输入昵称！',
        }
    )

    email = StringField(
        label='邮箱',
        validators=[
            DataRequired('请输入邮箱')
        ],
        description='邮箱',
        render_kw={
            " class=": 'form - control',
            " placeholder": '请输入邮箱！',

        }
    )
    tel = StringField(
        label='联系方式',
        validators=[
            DataRequired('请输入联系方式')
        ],
        description='联系方式',
        render_kw={
            " class=": 'form - control',
            " placeholder": '请输入联系方式！'

        }
    )

    pwd = StringField(
        label='密码',
        validators=[
            DataRequired('请输入密码')
        ],
        description='密码',
        render_kw={
            " class=": 'form - control',
            " placeholder": '请输入密码！'

        }
    )

    submit = SubmitField(
        '编辑',
        render_kw={
            "class": "btn btn-primary"
        }
    )


class AdminForm(FlaskForm):
    name = StringField(
        label='账号',
        validators=[
            DataRequired('请输入账号')
        ],
        description='账号',
        render_kw={
            " class=": 'form - control',
            " placeholder": '请输入账号！'

        }
    )

    tel = StringField(
        label='联系方式',
        validators=[
            DataRequired('请输入联系方式')
        ],
        description='联系方式',
        render_kw={
            " class=": 'form - control',
            " placeholder": '请输入联系方式！'

        }
    )

    pwd = StringField(
        label='密码',
        validators=[
            DataRequired('请输入密码')
        ],
        description='密码',
        render_kw={
            " class=": 'form - control',
            " placeholder": '请输入密码！'

        }
    )

    repwd = StringField(
        label='重复密码',
        validators=[
            DataRequired('请输入重复密码'),
            EqualTo('pwd', message='两次密码不一致')
        ],
        description='重复密码',
        render_kw={
            " class=": 'form - control',
            " placeholder": '请输入重复密码！'

        }
    )

    submit = SubmitField(
        '编辑',
        render_kw={
            "class": "btn btn-info btn-group-justified"
        }
    )
