from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/zadaci')
def zadaci():
    return render_template('zadaci.html')

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')

@app.route('/opste-informacije')
def opste_informacije():
    return render_template('opste_informacije.html')

app.run(debug=True)