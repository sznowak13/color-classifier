from flask import Flask, render_template, request, redirect, url_for, session, flash
from os import urandom
from uuid import uuid1
from persistence import db_manager

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        if 'entry_uuid' in session:
            flash(f"Thanks for sampling, {session['name']}")
            session.clear()
        return render_template('index.html')
    elif request.method == 'POST':
        session['name'] = request.form['entry_name']
        session['entry_uuid'] = str(uuid1())
        return redirect( url_for('sampler') )


@app.route('/sampler', methods=['POST', 'GET'])
def sampler():
    if request.method == 'GET':
        colors = ['red-ish', 'yellow-ish', 'green-ish', 'purple-ish', 'brown-ish', 'blue-ish', 'pink-ish', 'orange-ish']
        return render_template('sampler.html', colors=colors)
    elif request.method == 'POST':
        data_entry = request.form.to_dict()
        data_entry['id'] = session['entry_uuid']
        print(data_entry)
        db_manager.add_entry(entry=data_entry)
        return redirect( url_for('sampler') )


if __name__ == '__main__':
    app.secret_key = urandom(25)
    app.run(
        debug=True,
        port=5060
        )