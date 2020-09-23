from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required, DataRequired


class UpdateProfile(FlaskForm):
        bio = TextAreaField('Tell us about you.', validators=[DataRequired()])
        submit = SubmitField('Submit')


class PostForm(FlaskForm):
    category = SelectField('Category', choices=[('badjokes', 'badjokes'), ('asap', 'asap'), ('nightthoughts', 'nightthoughts')])
    title = StringField('Post title', validators=[DataRequired()])
    post = TextAreaField('Write your post', validators=[DataRequired()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('Write your comment',validators=[DataRequired()])
    submit = SubmitField('Submit')
