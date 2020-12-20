from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField


class SignForm(FlaskForm):
    submit = SubmitField('签到')


class SignOutForm(FlaskForm):
    submit = SubmitField('签退')


# replenish sign 补签
class ReplenishSignForm(FlaskForm):
    re_sign = SelectField('补签时长', coerce=int)
    submit = SubmitField('补签')

    def __init__(self, user, *args, **kwargs):
        super(ReplenishSignForm, self).__init__(*args, **kwargs)
        self.re_sign.choices = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        self.user = user


class ExcelForm(FlaskForm):
    submit = SubmitField('生成')
