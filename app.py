import os
from flask import Flask, render_template, request, redirect, url_for
from flask_session import Session
from views.games import games_blueprint
from views.admin import admin_blueprint

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = os.urandom(64)
Session(app)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')


app.register_blueprint(games_blueprint, url_prefix='/games')
app.register_blueprint(admin_blueprint, url_prefix='/admin')

if __name__ == '__main__':
    app.run(debug=True)
