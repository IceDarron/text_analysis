from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test/')
@app.route('/test/<name>')
def show_test(name=None):
    return render_template('test.html', name=name)


if __name__ == '__main__':
    app.run()
