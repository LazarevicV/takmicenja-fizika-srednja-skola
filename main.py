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

@app.route('/opste_informacije')
def opste_informacije():
    return render_template('opste_informacije.html')

@app.route('/sfo')
def sfo():
    return render_template('sfo.html')

@app.route('/opstinsko')
def opstinsko():
    return render_template('opstinsko.html')

@app.route('/drzavno')
def drzavno():
    return render_template('drzavno.html')

@app.route('/ipho')
def ipho():
    return render_template('ipho.html')

@app.route('/vesti')
def vesti():
    return render_template('vesti.html')

@app.route('/okruzno')
def okruzno():
    return render_template('okruzno.html')

app.run(debug=True)