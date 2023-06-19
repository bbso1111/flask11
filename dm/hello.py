# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def index():
#     return '<h1>hello world </h1>'

from flask import Flask,request

app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'fefwld!'



# 带参数的url
@app.route('/blog/<blog_id>')
def blog_detail(blog_id):
    return '您访问的博客是:%s' % blog_id


# 查询字符串的方式传参
@app.route('/blog/list')
def blog_list():
    page = request.args.get("page",default=1,type=int)
    return f"您获取的是第{page}的图书列表"


if __name__ == '__main__':
    app.run()