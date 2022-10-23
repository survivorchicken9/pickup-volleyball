import os
from flask import Flask, render_template, request, redirect, url_for
from flask_session import Session
from models.admin import Admin
from views.games import games_blueprint
from views.admin import admin_blueprint
from flask_login import LoginManager
from flask_login import current_user


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = os.urandom(64)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return Admin.find_admin(id)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        auth = current_user.is_authenticated
        return render_template('index.html', auth=auth)


app.register_blueprint(games_blueprint, url_prefix='/games')
app.register_blueprint(admin_blueprint, url_prefix='/admin')

if __name__ == '__main__':
    app.run(debug=True)
