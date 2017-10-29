from wtfforms.validators import Required,Length
from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from .. import photos
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_pagedown.fields import PageDownField
from ..models import Note,Category

class MarkdownForm(FlaskForm):
    title = StringField('标题',validators=[Length(0,50)])
    stage = PageDownField('think',validators=[Required()])
    ctype = SelectField('文章类型',coerce=int)
    submit = SubmitField('save')

    def __init__(self,*args,**kwargs):
        super(MarkdownForm,self).__init__(*args,**kwargs)
        self.ctype.choices = [(category.id,category.name) for category in Category.query.order_by(Category.name).all()]

class CanvasForm(FlaskForm):
    title = StringField('标题',validators=[Length(0,50)])
    stage = PageDownField('think',validators=[Required()])
    ctype = SelectField('文章类型',coerce=int)
    submit = SubmitField('save')