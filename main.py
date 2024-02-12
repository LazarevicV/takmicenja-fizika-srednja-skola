from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/zadaci')
def zadaci():
    return render_template('zadaci.html')

app.run(debug=True)