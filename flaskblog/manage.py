from RealProject import create_app

app = create_app()

# 当运行这个文件的时候才执行run()方法
if __name__ == '__main__':
    app.run(debug=True)