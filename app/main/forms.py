from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField, \
    SubmitField, FileField
from wtforms.validators import DataRequired, Length, Email, Regexp
from wtforms import ValidationError
from flask_pagedown.fields import PageDownField
from ..models import Role, User


class NameForm(FlaskForm):
    name = StringField('你的名字', validators=[DataRequired()])
    submit = SubmitField('提交')


class EditProfileForm(FlaskForm):

    name = StringField('真实姓名', validators=[Length(0, 64)])
    s_class = StringField('班级', validators=[Length(0, 64)])
    about_me = TextAreaField('关于我')
    submit = SubmitField('提交')


class EditProfileAdminForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField('用户名', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               '用户名只能输入字母，数字，标点或者下划线')])
    confirmed = BooleanField('已认证')
    role = SelectField('权限', coerce=int)
    name = StringField('真实姓名', validators=[Length(0, 64)])
    s_class = StringField('班级', validators=[Length(0, 64)])
    about_me = TextAreaField('关于我')
    submit = SubmitField('提交')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已存在')

    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已存在')


class PostForm(FlaskForm):
    body = PageDownField("说说你的想法？", validators=[DataRequired()])
    submit = SubmitField('提交')


class CommentForm(FlaskForm):
    body = StringField('输入你的评论', validators=[DataRequired()])
    submit = SubmitField('提交')

class ChangeAvatarForm(FlaskForm):
    avatar = FileField('')
    submit = SubmitField('Submit')