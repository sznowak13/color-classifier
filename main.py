from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from os import urandom
from uuid import uuid1
from logic import data_logic as dl

app = Flask(__name__)

COLOR_LABELS = ['red-ish', 'yellow-ish', 'green-ish', 'purple-ish', 'brown-ish', 'blue-ish', 'pink-ish', 'orange-ish', 'black-ish', 'white-ish']

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
        return render_template('sampler.html', colors=COLOR_LABELS)
    elif request.method == 'POST':
        data_entry = request.form.to_dict()
        data_entry['id'] = session['entry_uuid']
        return redirect( url_for('sampler') )


@app.route('/add-entry', methods=['POST'])
def add_entry():
    data_entry = request.get_json()
    data_entry['id'] = session['entry_uuid']
    data_entry['entry_name'] = session['name']
    result = dl.add_color_entry(data_entry)
    return jsonify({
        'status': result.status,
        'message': result.message,
        'body': result.body
    })

if __name__ == '__main__':
    app.secret_key = urandom(25)
    app.env = 'Development'
    app.run(
        debug=True,
        port=5060
        )
