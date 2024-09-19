from flask import Flask, redirect, url_for
from app.routes import auth

app = Flask(__name__)
app.register_blueprint(auth)


@app.route('/')
def home():
    return redirect(url_for('auth.login'))


if __name__ == '__main__':
    app.run(debug=True)
