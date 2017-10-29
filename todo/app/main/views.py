from . import main
from flask import Flask,render_template
from flask import make_response,render_template, session, redirect, url_for, current_app,abort,flash,request
import json,os,base64 ,time
from datetime import datetime
from ..models import Note
from .. import db	

@main.route('/upload',methods=['POST'])
def index():
    """
    disturbing by jq
    this method cannot work
    """
    files=request.values.get('data')
    f=request.form['data'][23:]
    t=request.form['title']
    imgdata=base64.b64decode(f)
    nw=str(int(datetime.utcnow().timestamp()))
    now_=datetime.utcnow()
    url='/static/cv/'+nw+'.jpg'
    file=open('app'+url,'wb')
    file.write(imgdata)
    file.close()
    cate=request.form['category']

    note = Note(title=t,pub_time=now_,ntype=2,imgurl=url,alt_time=now_,category=cate)
    db.session.add(note)
    return '/'

@main.route('/create-content',methods=['POST'])
def edit_markdown():
    now_=datetime.utcnow()
    t=request.form['title']
    cate=request.form['category']
    tt=request.form['text']

    note=Note(title=t,pub_time=now_,ntype=1,content_text=tt,alt_time=now_,category=cate)
    db.session.add(note)
    return '/'
	
@main.route('/',methods=['GET'])
def show():
    query=Note.query
    note =request.args.get('page',1,type=int)
    pagination = query.order_by(Note.pub_time.desc()).paginate(
        note,per_page=8,
        error_out=False)
    notes = pagination.items
    return render_template('index.html',pagination=pagination,notes=notes,tsc=str(int(datetime.utcnow().timestamp())))

@main.route('/update-canvas',methods=['POST'])
def update_canvas():
    id = request.form['id']
    note = Note.query.filter_by(id=id).first()
    f=request.form['data'][23:]
    imgdata=base64.b64decode(f)
    imgurl = note.imgurl
    file=open('app'+imgurl,'wb')
    file.write(imgdata)
    file.close()

    note.title = request.form['title']
    note.alt_time = datetime.utcnow()
    note.category = request.form['category']
    db.session.add(note)
    flash('更新成功!')
    return '/'

@main.route('/update-markdown',methods=['POST'])
def update_markdown():
    id = request.form['id']
    note = Note.query.filter_by(id=id).first()
    note.title = request.form['title']
    note.content_text = request.form['text']
    note.category = request.form['category']
    note.alt_time = datetime.utcnow()
    db.session.add(note)
    return '/'