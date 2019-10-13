from flask import Flask, json, render_template

from extract.extract_data import extract_data

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test/')
@app.route('/test/<name>')
def show_test(name=None):
    return render_template('test.html', name=name)


@app.route('/get_data')
def get_data():
    language = ['python', 'java', 'c', 'c++', 'c#', 'php']
    value = ['100', '150', '100', '90', '80', '90']
    return json.dumps({'language': language, 'value': value}, ensure_ascii=False)  # 如果有中文的话，就需要ensure_ascii=False


@app.route('/key_word/')
@app.route('/key_word/<name>')
def show_key_word(name=None):
    return render_template('key_word.html', name=name)


@app.route('/freq_key_word')
def get_freq_key_word():
    key_word_count = extract_data()
    key_word = []
    key_word_count_value = []
    for key, value in key_word_count.items():
        if value < 10:
            continue
        key_word.append(key)
        key_word_count_value.append(str(value))
    return json.dumps({'key_word': key_word, 'value': key_word_count_value}, ensure_ascii=False)


if __name__ == '__main__':
    app.run()
