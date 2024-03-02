from flask import Flask, render_template, url_for

from googleapiclient.discovery import build
import requests

API_KEY = 'AIzaSyAwS_DyrkREzuTmGhYneB97kkeOhd4-Tgc'

# ID of the Google Drive folder
DRIVE_FOLDER_ID = '1-VdVYddOYK-NjW9OgsWzxLs7Cw54bq0B'

def list_files(folder_id):
    files = []

    # Build the URL to list files in the folder
    url = f'https://www.googleapis.com/drive/v3/files?q=%27{folder_id}%27+in+parents&fields=files(id,name,mimeType,webViewLink)&key={API_KEY}&alt=json'

    response = requests.get(url)
    data = response.json()

    if 'files' in data:
        files.extend(data['files'])

    return files

folders = list_files(DRIVE_FOLDER_ID)

opstinsko_fajlovi = []
okruzno_fajlovi = []
drzavno_fajlovi = []

for folder in folders:
    if folder['mimeType'] == 'application/vnd.google-apps.folder':
        subfolder_id = folder['id']
        subfolder_name = folder['name']

        # print(f"Exploring subfolder: {subfolder_name}")

        # List files in the subfolder
        files_in_subfolder = list_files(subfolder_id)

        for file in files_in_subfolder:
            if file['mimeType'] == 'application/pdf':
                file_name = file['name']
                file_link = file['webViewLink']
                if 'opstinsko' in file_name:
                    opstinsko_fajlovi.append({'name': file_name, 'link':file_link})
                elif 'republicko' in file_name:
                    drzavno_fajlovi.append({'name': file_name, 'link':file_link})
                elif 'okruzno' in file_name:
                    okruzno_fajlovi.append({'name': file_name, 'link':file_link})
                # print(f"PDF File Name: {file_name}, Link: {file_link}")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/test')
# def test():
    

@app.route('/zadaci')
def zadaci():
    return render_template('zadaci_resenja.html')

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

@app.route('/pravilnici-o-takmicenjima')
def pravila():
    return render_template('vazna_dokumenta.html')

@app.route('/opstinsko_zadaci')
def opstinsko_zadaci():
    godine = []
    for o in opstinsko_fajlovi:
        trenutno = o['name'].split('_')
        if (len(trenutno[0])>2 and trenutno[0] not in godine): #or (len(trenutno[1])>2 and trenutno[1] not in godine):
            godine.append(trenutno[0])
        elif (len(trenutno[1])>2 and trenutno[1] not in godine):
            godine.append(trenutno[1])
    godine.sort(reverse=True)
    prave_godine = []
    for i in range(6):
        prave_godine.append(godine[i])
    
            
    return render_template('opstinsko_zadaci.html', godine=prave_godine, opstinsko=opstinsko_fajlovi)

@app.route('/drzavno_zadaci')
def drzavno_zadaci():
    godine = []
    for o in drzavno_fajlovi:
        trenutno = o['name'].split('_')
        if (len(trenutno[0])>2 and trenutno[0] not in godine): #or (len(trenutno[1])>2 and trenutno[1] not in godine):
            godine.append(trenutno[0])
        elif (len(trenutno[1])>2 and trenutno[1] not in godine):
            godine.append(trenutno[1])
    godine.sort(reverse=True)
    prave_godine = []
    n = len(drzavno_fajlovi)
    if (n < 6):
        for i in range(n):
            prave_godine.append(godine[i])
    else:
        for i in range(6):
            prave_godine.append(godine[i])
    
            
    return render_template('drzavno_zadaci.html', godine=prave_godine, drzavno=drzavno_fajlovi)

@app.route('/okruzno_zadaci')
def okruzno_zadaci():
    godine = []
    for o in okruzno_fajlovi:
        trenutno = o['name'].split('_')
        if (len(trenutno[0])>2 and trenutno[0] not in godine): #or (len(trenutno[1])>2 and trenutno[1] not in godine):
            godine.append(trenutno[0])
        elif (len(trenutno[1])>2 and trenutno[1] not in godine):
            godine.append(trenutno[1])
    godine.sort(reverse=True)
    prave_godine = []
    n = len(okruzno_fajlovi)
    if (n < 6):
        for i in range(n):
            prave_godine.append(godine[i])
    else:
        for i in range(6):
            prave_godine.append(godine[i])
    
            
    return render_template('okruzno_zadaci.html', godine=prave_godine, okruzno=okruzno_fajlovi)

# print(opstinsko_fajlovi)
# print('*' *50)
# print(drzavno_fajlovi)
print(len(okruzno_fajlovi))

app.run(debug=True, host='0.0.0.0')