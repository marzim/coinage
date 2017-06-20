from flask_wtf import Form
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import Length, InputRequired, DataRequired

class AddBlogForm(Form):
    title = StringField(
        'title',
        validators=[InputRequired(), Length(min=3, max=225)]
    )
    content = StringField(
        'content',
        validators=[InputRequired(), Length(min=3, max=225)]
    )
    posted_on = StringField(
        'posted_on')

    posted_by = StringField(
        'posted_by')

class EditBlogForm(Form):
    content = StringField(
        'content',
        validators=[InputRequired(), Length(min=3, max=225)]
    )
    posted_on = StringField(
        'posted_on')

    posted_by = StringField(
        'posted_by')