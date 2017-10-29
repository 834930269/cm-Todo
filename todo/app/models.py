# -*- coding: utf-8 -*- 
from . import db
from datetime import datetime
from markdown import markdown
import bleach
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

class Note(db.Model):
    __tablename__='notes'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(60),default='发表自: '+datetime.utcnow().strftime("%Y-%m-%d %H:%S:%M"))
    pub_time = db.Column(db.DateTime,default=datetime.utcnow)
    ntype = db.Column(db.Integer,default=1)
    imgurl = db.Column(db.String(200))
    content_text = db.Column(db.Text)
    content_html = db.Column(db.Text)
    alt_time = db.Column(db.DateTime,default=datetime.utcnow)
    category = db.Column(db.String(20),default='生活')

        #将Markdown转换为HTML
    @staticmethod
    def on_change_content(target,value,oldvalue,initiator):
        #允许的标签+属性类型
        attrs = {
            '*': ['class','style','width','height'],
            'a': ['href', 'rel'],
             'img': ['src', 'alt'],
        }
        #允许的标签类型
        allowed_tags = ['a','abbr','acronym','b','blockquote','code',
                        'em','i','li','ol','pre','strong','ul',
                        'h1','h2','h3','p','img','br']
        target.content_html = bleach.linkify(bleach.clean(
            markdown(value,output_format='html'),
            tags=allowed_tags, attributes=attrs,strip=True))

db.event.listen(Note.content_text,'set',Note.on_change_content)