from flask import Flask, render_template, request, redirect, url_for
from os import urandom

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        name = request.form['entry_name']
        return redirect( url_for('sampler', name=name) )


@app.route('/sampler/<name>')
def sampler(name):
    colors = ['red-ish', 'yellow-ish', 'green-ish', 'purple-ish', 'brown-ish', 'blue-ish', 'pink-ish', 'orange-ish']
    return render_template('sampler.html', name=name, colors=colors)


if __name__ == '__main__':
    app.secret_key = urandom(25)
    app.run(
        debug=True,
        port=5060
        )