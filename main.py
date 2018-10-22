from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from os import urandom
from uuid import uuid1

from logic import data_logic as dl
from ml import ml_test
from util import COLOR_LABELS

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        if 'entry_uuid' in session:
            name = session['name']
            session.clear()
            flash(f"Thanks for sampling, {name}")
        return render_template('index.html')
    elif request.method == 'POST':
        session['name'] = request.form['entry_name']
        session['entry_uuid'] = str(uuid1())
        return redirect( url_for('sampler') )


@app.route('/sampler')
def sampler():
    return render_template('sampler.html', colors=COLOR_LABELS)


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


@app.route('/classifier')
def classifier():
    score, num_entries = ml_test.prepare_model()
    return render_template('classifier.html', score=score, entry_number=num_entries)


@app.route('/predict-color', methods=['POST'])
def predict_color():
    request_data = request.get_json()
    rgb_values = [[request_data['red'], request_data['green'], request_data['blue']]]
    res = ml_test.predict_color(rgb_values)
    return jsonify({
        'status': res.status,
        'message': res.message,
        'body': res.body
    })


if __name__ == '__main__':
    app.secret_key = urandom(25)
    app.env = 'Development'
    app.run(
        debug=True,
        port=5060
        )
