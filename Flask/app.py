from flask import Flask, render_template, url_for, request, redirect, session


app = Flask(__name__)
app.secret_key = 'secret_key'  # wird für session benötigt


@app.route("/", methods=["GET", "POST"])
def index():
    return redirect(url_for('index'))  # direkte Weiterleitung -> index


@app.route("/index", methods=["GET", "POST"])
def index():
    return render_template('start.html')  # Anzeige der Seite index.html


@app.route("/login", methods=["GET", "POST"])
def login():
    # GET
    if request.method == "GET":
        # Bereits angemeldet?
        try:
            if session['login_status']:  # True or False
                return r'Sie sind bereits angemeldet <a href="/">zurück</a>'
            else:
                return r'Sie sind noch nicht angemeldet <a href="/">zurück</a>'
        except KeyError:
            return r'Direkte URL-Eingabe wird geblockt! <a href="/">zurück</a>'
    # POST
    usr = request.form.get('usr')
    pwd = request.form.get('pwd')
    if (usr == 'admin') & (pwd == "password"):
        msg = 'Erfolgreich angemeldet :)'
        session['login_status'] = True
    else:
        msg = 'Username und/oder Passwort sind falsch. :/'
        session['login_status'] = False
    return f'{msg} <a href="/">zurück</a>'


# If the app.py run on local machine
if __name__ == '__main__':
    app.run(port=5000, debug=True)
