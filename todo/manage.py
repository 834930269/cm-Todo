#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
import os
if os.path.exists('config.env'):
    print('找到环境文件')
    for line in open('config.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]]=var[1]
from app import create_app, db

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from app.models import *

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()