from flask import Flask, url_for, render_template, request, redirect, session
from kgmodel import (Foresatt, Barn, Soknad, Barnehage)
from kgcontroller import (form_to_object_soknad, insert_soknad, commit_all, select_alle_barnehager, diagram_for_valgt_kommune, vurder_soknad, select_alle_soknader)

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'  # nødvendig for session

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/barnehager')
def barnehager():
    information = select_alle_barnehager()
    return render_template('barnehager.html', data=information)

@app.route('/behandle', methods=['GET', 'POST'])
def behandle():
    if request.method == 'POST':
        sd = request.form
        soknad_obj = form_to_object_soknad(sd)
        insert_soknad(soknad_obj)  # Lagre søknaden
        session['information'] = sd
        
        # Bruk vurder_soknad til å avgjøre om søknaden får TILBUD eller AVSLAG
        resultat = vurder_soknad(sd)
        session['resultat'] = resultat  # Lagre resultatet i sesjonen for bruk i svar.html

        return redirect(url_for('svar'))
    else:
        return render_template('soknad.html')

@app.route('/svar')
def svar():
    information = session.get('information')
    resultat = session.get('resultat')  # Hent resultatet fra sesjonen
    return render_template('svar.html', data=information, resultat=resultat)  # Send resultat til malen

@app.route('/commit')
def commit():
    global forelder, barnehage, barn, soknad
    commit_all()  # Skriver alle data til Excel
    # Henter data fra alle dataframes for å sende til malen
    data = {
        'foresatt': forelder.to_dict('records') if 'forelder' in globals() else [],
        'barnehage': barnehage.to_dict('records') if 'barnehage' in globals() else [],
        'barn': barn.to_dict('records') if 'barn' in globals() else [],
        'soknad': soknad.to_dict('records') if 'soknad' in globals() else []
    }
    return render_template('commit.html', data=data)

@app.route('/soknader')
def soknader():
    alle_soknader = select_alle_soknader()
    return render_template('soknader.html', soknader=alle_soknader)

@app.route('/statistikk')
def statistikk():
    return render_template('statistikk.html')

@app.route('/vis', methods=['GET', 'POST'])
def vis():
    if request.method == 'POST':
        valgt_kommune = request.form['valgt_kommune']
        return diagram_for_valgt_kommune(valgt_kommune)
    return render_template('statistikk.html')

if __name__ == "__main__":
    app.run(port=5001)
    



