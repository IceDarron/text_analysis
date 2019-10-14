from flask import Flask, json, render_template

from extract.extract_data import calc_key_word_count, calc_key_word_freq

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


@app.route('/page_key_word_count/')
@app.route('/page_key_word_count/<name>')
def show_key_word_count(name=None):
    return render_template('page_key_word_count.html', name=name)


@app.route('/key_word_count')
def get_key_word_count():
    key_word_count = calc_key_word_count()
    key_word = []
    key_word_count_value = []
    for key, value in key_word_count.items():
        if value < 10:
            continue
        key_word.append(key)
        key_word_count_value.append(str(value))
    return json.dumps({'key_word': key_word, 'value': key_word_count_value}, ensure_ascii=False)


@app.route('/page_key_word_freq/')
@app.route('/page_key_word_freq/<name>')
def show_key_word_freq(name=None):
    return render_template('page_key_word_freq.html', name=name)


@app.route('/key_word_freq')
def get_key_word_freq():
    key_word_freq = calc_key_word_freq()
    key_word = []
    key_word_freq_value = []
    for key, value in key_word_freq.items():
        if value < 1:
            continue
        key_word.append(key)
        key_word_freq_value.append(str(value))
    return json.dumps({'key_word': key_word, 'value': key_word_freq_value}, ensure_ascii=False)


if __name__ == '__main__':
    app.run()
