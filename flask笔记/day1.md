

## 准备工作

##### 1.选择一个文件夹，创建虚拟环境

**macOS/Liunx系统**

```
$ mkdir flaskBlog//文件名随意
$ cd flaskBlog
$ python3 -m venv venv
```

**Windows系统**

```
> mkdir flaskBlog
> cd flaskBlog
> py -m venv venv
```

 创建完会看见一个venv的文件夹在你刚创建的文件夹下面

##### 2.激活虚拟环境

**macOS/Liunx系统**

````
$ . venv/bin/activate
````

**Windows系统**

```
> venv\Scripts\activate
```

你终端的地址会显示你进入了虚拟环境（如下图）

![屏幕截图 2023-06-12 095231](D:\flask\图片\屏幕截图 2023-06-12 095231.png)

##### 3.安装flask

在激活的环境中，使用以下命令安装 Flask：

```
$ pip install Flask
```

##### 4.创建目录机构（项目目录和结构目录）

目录结构如下

![](D:\flask\图片\ml2.png)

然后将下面代码输入到RealProject的——init——.py文件中

```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

manage.py文件中代码如下

```
from RealProject import app

if __name__ == '__main__':
    app.run()//程序的入口文件
```

__以后每次都可以在终端输入py manage,py来启动程序__

另外还建议把debug改为true，这样返回到前端页面都可以随时看到更改

```
在app.py文件中

debug: bool | True = True,
```

##### 5.安装数据库

```
pip install flask-sqlalchemy
```

##### 6.安装Flask-Migrate、

```
pip install Flask-Migrate
```

