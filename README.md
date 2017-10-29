# cm-Todo
这是一款基于-Flask-Canvas-Mysql-Python3-Bootstrap-的TODO/记事本/交流 的Web App应用

其中记事本框的CSS和部分JS来自于 [youknowznm-vue-memo](https://github.com/youknowznm/vue-memo "youknowznm-vue-memo")

本地使用方法:

先在`config.py`中的:
   
> DATABASE_USERNAME=<br/>
> DATABASE_PASSWORD=

中输入你Mysql数据库的用户名和密码,并自行创建一个名为notebook的数据库.<br/>
(这里数据库自行选择,不同数据库的接口配置在`config.py`中进行)<br/><br/>
然后在当前目录下的命令行中执行以下命令:
<br/><br/>
    python manage.py db init<br/>
	python manage.py db migrate -m 'first'
	python manage.py db upgrade

最后在命令行中执行`manage.py`并通过`localhost:5000`进行访问即可.
	python manage.py runserver

注意,是python3.*,如果您是Linux用户,可能会需要修改以下Mysql数据库的所有编码方式为utf-8.


该App可以轻松集成到到您的Flask Web App中,至于如何集成,这里不再赘述.

`Demo`: [地平线上的一匹狼-日志](http://be-sunshine.cn:5100/notebooks "地平线上的一匹狼-日志")