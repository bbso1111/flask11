import os
from RealProject.settings import BASE_DIR
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# 实例化SQLAlchemy对象
db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    # create and configure the app
    ## instance_relative_config设置为True则代表开启从文件加载配置，默认为False
    app = Flask(__name__, instance_relative_config=True)
    # app.config其实调用的是flask类的config属性，该属性又被设置为了一个Config的类
    ## from_mapping则是该Config类下的一个方法，用来更新默认配置，返回值为True
    ## 至于Flask的默认配置项都有哪些，其实可以深入源码查看default_config属性所列出的项
    # 默认配置
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # )

    # 这里做了判断是否运行时传入了测试配置
    if test_config is None:
        CONFIG_PATH = BASE_DIR / 'RealProject/settings.py'
        # 如果没有传入，则从py文件加载配置，silent=True代表文件，文件加载成功则返回True
        app.config.from_pyfile('settings.py', silent=True)
    else:
        # 和最开始的配置意思一致
        app.config.from_mapping(test_config)
        
    db.init_app(app)
    #工厂函数里面实例化
    # 递归创建目录，确保项目文件存在
    migrate.init_app(app, db)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from app.blog import views as blog
    app.register_blueprint(blog.bp)
    

    from app.blog import models

    return app