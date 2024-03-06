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

# for folder in folders:
#     print(f"Folder Name: {folder['name']}, Folder ID: {folder['id']}")

opstinsko_fajlovi = []
okruzno_fajlovi = []
drzavno_fajlovi = []
gama_fajlovi = []
# Prvo pronađite ID foldera pod nazivom "GAMA kategorija"
gama_folder_id = None
for folder in folders:
    if folder['mimeType'] == 'application/vnd.google-apps.folder' and 'GAMA kategorija' in folder['name']:
        gama_folder_id = folder['id']
        break

# Ako je pronađen folder, nastavite sa listanjem fajlova unutar njega
if gama_folder_id:
    gama_files = list_files(gama_folder_id)
    
    for file in gama_files:
        if file['mimeType'] == 'application/pdf':
            file_name = file['name']
            file_link = file['webViewLink']
            gama_fajlovi.append({'name': file_name, 'link': file_link})

# Nastavite sa pretragom ostalih fajlova
for folder in folders:
    if folder['mimeType'] == 'application/vnd.google-apps.folder':
        subfolder_id = folder['id']
        subfolder_name = folder['name']

        # List files in the subfolder
        files_in_subfolder = list_files(subfolder_id)

        for file in files_in_subfolder:
            if file['mimeType'] == 'application/pdf':
                file_name = file['name']
                file_link = file['webViewLink']
                
                # Extract year from the file name using a more robust method
                try:
                    year = int(file_name.split('_')[0])
                except ValueError:
                    year = 0  # Handle cases where the year is not an integer
                
                if 2017 <= year <= 2023:  # Adjust the range based on your needs
                    if 'opstinsko' in file_name:
                        opstinsko_fajlovi.append({'name': file_name, 'link': file_link})
                    elif 'republicko' in file_name:
                        drzavno_fajlovi.append({'name': file_name, 'link': file_link})
                    elif 'okruzno' in file_name:
                        okruzno_fajlovi.append({'name': file_name, 'link': file_link})
                    else:
                        # Files with names not matching specific categories go to "Ostalo" for "Drzavno"
                        ostalo_file = {'name': file_name, 'link': file_link}
                        drzavno_fajlovi.append(ostalo_file)

# Nastavite sa vašim postojećim kodom...


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
        if (len(trenutno[0]) > 2 and trenutno[0] not in godine): 
            godine.append(trenutno[0])
        elif (len(trenutno[1]) > 2 and trenutno[1] not in godine):
            godine.append(trenutno[1])
    godine.sort(reverse=True)
    prave_godine = []

    alfa_opstinsko = []
    beta_opstinsko = []
    gama_opstinsko = []  # Dodajte gama kategoriju
    ostalo_opstinsko = []

    for o in opstinsko_fajlovi:
        if 'BETA' in o['name'] or 'beta' in o['name'] or 'Beta' in o['name']:
            beta_opstinsko.append(o)
        elif 'ALFA' in o['name'] or 'alfa' in o['name'] or 'Alfa' in o['name']:
            alfa_opstinsko.append(o)
        elif 'opstinsko' in o['name'].lower():  # Dodajte proveru za "opstinsko"
            ostalo_opstinsko.append(o)

    for gama_file in gama_fajlovi:
        if 'opstinsko' in gama_file['name'].lower():  # Dodajte proveru za "opstinsko"
            gama_opstinsko.append(gama_file)

    for i in range(6):
        prave_godine.append(godine[i])

    alfa_opstinsko = sorted(alfa_opstinsko, key=lambda x: x['name'])
    beta_opstinsko = sorted(beta_opstinsko, key=lambda x: x['name'])
    gama_opstinsko = sorted(gama_opstinsko, key=lambda x: x['name'])
    ostalo_opstinsko = sorted(ostalo_opstinsko, key=lambda x: x['name'])

    return render_template('opstinsko_zadaci.html', godine=prave_godine, alfa=alfa_opstinsko, beta=beta_opstinsko, gama=gama_opstinsko, ostalo=ostalo_opstinsko)


@app.route('/okruzno_zadaci')
def okruzno_zadaci():
    godine = []
    for o in okruzno_fajlovi:
        trenutno = o['name'].split('_')
        if (len(trenutno[0]) > 2 and trenutno[0] not in godine): 
            godine.append(trenutno[0])
        elif (len(trenutno[1]) > 2 and trenutno[1] not in godine):
            godine.append(trenutno[1])
    godine.sort(reverse=True)
    prave_godine = []

    alfa_okruzno = []
    beta_okruzno = []
    gama_okruzno = []  # Dodajte gama kategoriju
    ostalo_okruzno = []

    for o in okruzno_fajlovi:
        if 'BETA' in o['name'] or 'beta' in o['name'] or 'Beta' in o['name']:
            beta_okruzno.append(o)
        elif 'ALFA' in o['name'] or 'alfa' in o['name'] or 'Alfa' in o['name']:
            alfa_okruzno.append(o)
        elif 'okruzno' in o['name'].lower() and 'gama' not in o['name'].lower():  # Dodajte proveru za "okruzno"
            ostalo_okruzno.append(o)

    for gama_file in gama_fajlovi:
        if 'okruzno' in gama_file['name'].lower():  # Dodajte proveru za "okruzno"
            gama_okruzno.append(gama_file)

    for i in range(6):
        prave_godine.append(godine[i])

    alfa_okruzno = sorted(alfa_okruzno, key=lambda x: x['name'])
    beta_okruzno = sorted(beta_okruzno, key=lambda x: x['name'])
    gama_okruzno = sorted(gama_okruzno, key=lambda x: x['name'])
    ostalo_okruzno = sorted(ostalo_okruzno, key=lambda x: x['name'])

    return render_template('okruzno_zadaci.html', godine=prave_godine, alfa=alfa_okruzno, beta=beta_okruzno, gama=gama_okruzno, ostalo=ostalo_okruzno)



@app.route('/drzavno_zadaci')
def drzavno_zadaci():
    godine = []
    for o in drzavno_fajlovi:
        trenutno = o['name'].split('_')
        if (len(trenutno[0]) > 2 and trenutno[0] not in godine): 
            godine.append(trenutno[0])
        elif (len(trenutno[1]) > 2 and trenutno[1] not in godine):
            godine.append(trenutno[1])
    godine.sort(reverse=True)
    prave_godine = []

    alfa_drzavno = []
    beta_drzavno = []
    gama_drzavno = []  # Dodajte gama kategoriju
    ostalo_drzavno = []

    for o in drzavno_fajlovi:
        if 'BETA' in o['name'] or 'beta' in o['name'] or 'Beta' in o['name']:
            beta_drzavno.append(o)
        elif 'ALFA' in o['name'] or 'alfa' in o['name'] or 'Alfa' in o['name']:
            alfa_drzavno.append(o)
        elif 'okruzno' in o['name'].lower():
            ostalo_drzavno.append(o)
        else:
            ostalo_drzavno.append(o)

    for gama_file in gama_fajlovi:
        if 'drzavno' in gama_file['name'].lower():  # Dodajte proveru za "drzavno"
            gama_drzavno.append(gama_file)

    for i in range(6):
        prave_godine.append(godine[i])

    alfa_drzavno = sorted(alfa_drzavno, key=lambda x: x['name'])
    beta_drzavno = sorted(beta_drzavno, key=lambda x: x['name'])
    gama_drzavno = sorted(gama_drzavno, key=lambda x: x['name'])
    ostalo_drzavno = sorted(ostalo_drzavno, key=lambda x: x['name'])

    return render_template('drzavno_zadaci.html', godine=prave_godine, alfa=alfa_drzavno, beta=beta_drzavno, gama=gama_drzavno, ostalo=ostalo_drzavno)

# print(opstinsko_fajlovi)
# print('*' *50)
# print(drzavno_fajlovi)
# print(len(okruzno_fajlovi))

app.run(debug=True, host='0.0.0.0')